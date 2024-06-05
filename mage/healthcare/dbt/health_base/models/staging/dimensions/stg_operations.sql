WITH stg_operations (
    SELECT * FROM {{ source('health', 'health_care_facilities')}}
),

staged AS (
    SELECT
        code,
        operation_status,
        open_whole_day,
        open_public_holidays,
        open_weekends,
        open_late_night
    FROM stg_operations
)

SELECT * FROM staged