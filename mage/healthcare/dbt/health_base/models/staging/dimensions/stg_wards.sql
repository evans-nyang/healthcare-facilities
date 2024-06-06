WITH myhealthcare AS (
    SELECT * FROM {{ source('health', 'health_care_facilities') }}
),

stg_wards AS (
    SELECT DISTINCT
        md5(ward::text) as ward_hash,
        ward
    FROM myhealthcare
)

SELECT * FROM stg_wards