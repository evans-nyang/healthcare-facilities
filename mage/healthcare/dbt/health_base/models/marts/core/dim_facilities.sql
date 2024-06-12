{{
    config(
        materialized='incremental',
        unique_key='facility_hash'
    )
}}

WITH stg_facilities AS (
    SELECT * FROM {{ ref("stg_facilities") }}
),

dim_facilities AS (
    SELECT 
        facility_hash,
        facility_name,
        facility_type,
        ownership,
        regulatory_body,
        operation_status,
        open_whole_day,
        open_public_holidays,
        open_weekends,
        open_late_night
    FROM stg_facilities
    {{ check_incremental('facility_hash') }}
)

SELECT * FROM dim_facilities