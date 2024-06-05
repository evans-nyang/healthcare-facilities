WITH stg_locations(
    SELECT * FROM {{ source('health', 'health_care_facilities')}}
),

staged AS (
    SELECT
        code,
        county,
        constituency,
        sub_county,
        ward
    FROM stg_locations
)

SELECT * FROM staged