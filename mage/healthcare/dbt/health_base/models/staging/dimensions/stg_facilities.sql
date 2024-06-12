WITH stg_facilities AS (
    SELECT * FROM {{ source('health', 'health_care_facilities')}}
),

staged AS (
    SELECT
        md5(trim(_name)) AS facility_hash,
        lower(_name) AS facility_name,
        lower(facility_type) AS facility_type,
        lower(_owner) AS ownership,
        lower(regulatory_body) AS regulatory_body,
        keph_level,
        beds,
        cots,
        lower(operation_status) AS operation_status,
        lower(open_whole_day) AS open_whole_day,
        lower(open_public_holidays) AS open_public_holidays,
        lower(open_weekends) AS open_weekends,
        lower(open_late_night) AS open_late_night,
        lower(approved) AS approved,
        lower(public_visible) AS public_visibility,
        lower(closed) AS closed
    FROM stg_facilities
)

SELECT * FROM staged