WITH source AS (
    SELECT * FROM {{ source('health', 'health_care_facilities') }}
),

stg_healthcare AS (
    SELECT
        code,
        md5(code::text) as code_hash,
        md5(_name::text) as name_hash,
        md5(county::text) as county_hash,
        md5(constituency::text) as constituency_hash,
        md5(sub_county::text) as sub_county_hash,
        md5(ward::text) as ward_hash
    FROM source
)

SELECT * FROM stg_healthcare