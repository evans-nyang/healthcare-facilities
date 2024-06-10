WITH source AS (
    SELECT * FROM {{ source('health', 'health_care_facilities')}}
),

stg_locations AS (
    SELECT
        md5(code::text) as code_hash,
        code,
        county,
        constituency,
        sub_county,
        ward
    FROM source
)

SELECT * FROM stg_locations