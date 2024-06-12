{{
    config(
        materialized='incremental',
        unique_key='code_name_hash'
    )
}}

WITH stg_healthcare AS (
    SELECT * FROM {{ ref ('stg_healthcare') }}
),

dim_facilities AS (
    SELECT * FROM {{ ref ('dim_facilities') }}
),

dim_locations AS (
    SELECT * FROM {{ ref ('dim_locations') }}
),

proxy AS (
    SELECT
        *
    FROM stg_healthcare
    INNER JOIN dim_facilities using (facility_hash)
    INNER JOIN dim_locations using (code_hash)
),

fact_healthcare AS (
    SELECT DISTINCT
        code_name_hash,
        code_hash,
        facility_hash
    FROM proxy
    {{ check_incremental('code_name_hash') }}
)

SELECT * FROM fact_healthcare