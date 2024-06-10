{{
    config(
        materialized='incremental',
        unique_key='code_hash'
    )
}}

WITH stg_locations AS (
    SELECT * FROM {{ ref("stg_locations") }}
),

dim_locations AS (
    SELECT 
        code_hash,
        code,
        county,
        constituency,
        sub_county,
        ward
    FROM stg_locations
    {{ check_incremental('code_hash') }}
)

SELECT * FROM dim_locations