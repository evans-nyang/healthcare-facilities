WITH stg_facilities AS (
    SELECT * FROM {{ source('health', 'health_care_facilities')}}
),

staged AS (
    SELECT
        md5(trim(name)) AS name_hash
        lower(_name) AS facilityName,
        lower(facility_type) AS facilityType,
        lower(_owner) AS ownership,
        lower(regulatory_body) AS regulatoryBody
    FROM stg_facilities
)

SELECT * FROM staged