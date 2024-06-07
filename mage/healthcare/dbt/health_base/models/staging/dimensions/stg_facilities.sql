WITH stg_facilities AS (
    SELECT * FROM {{ source('health', 'health_care_facilities')}}
),

staged AS (
    SELECT
        md5(trim(_name)) AS facility_hash,
        lower(_name) AS facility_name,
        lower(facility_type) AS facility_type,
        lower(_owner) AS ownership,
        lower(regulatory_body) AS regulatory_body
    FROM stg_facilities
)

SELECT * FROM staged