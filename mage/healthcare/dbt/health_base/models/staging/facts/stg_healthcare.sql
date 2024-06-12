WITH source AS (
    SELECT * FROM {{ source('health', 'health_care_facilities') }}
),

stg_healthcare AS (
    SELECT
        code,
        _name,
        md5(code::text) as code_hash,
        md5(_name::text) as facility_hash,
        md5(county::text) as county_hash,
        md5(constituency::text) as constituency_hash,
        md5(sub_county::text) as sub_county_hash,
        md5(ward::text) as ward_hash
    FROM source
),

inter_proxy AS (
    SELECT
        stg_healthcare.*,
        {{ dbt_utils.generate_surrogate_key(['code', '_name']) }} AS code_name_hash
    FROM stg_healthcare
),

final AS (
    SELECT
        inter_proxy.*,
        ROW_NUMBER() OVER (PARTITION BY code_name_hash) AS entry_order
    FROM inter_proxy
)

SELECT * FROM final WHERE entry_order = 1