WITH stg_facilities AS (
    SELECT * FROM {{ source('health', 'health_care_facilities')}}
),

staged AS (
    SELECT
        code,
        _name,
        facility_type,
        _owner,
        regulatory_body
    FROM stg_facilities
)

SELECT * FROM staged