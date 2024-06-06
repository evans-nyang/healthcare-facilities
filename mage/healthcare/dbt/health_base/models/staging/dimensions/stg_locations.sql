WITH stg_locations AS (
    SELECT * FROM {{ source('health', 'health_care_facilities')}}
),

staged AS (
    SELECT
        md5(code::text) as code_hash,
        code,
        county,
        constituency,
        sub_county,
        ward
    FROM stg_locations
)

SELECT * FROM staged