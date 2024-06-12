WITH source AS (
    SELECT * FROM {{ source('health', 'health_care_facilities') }}
),

stg_wards AS (
    SELECT DISTINCT
        md5(ward::text) as ward_hash,
        ward
    FROM source
)

SELECT * FROM stg_wards