WITH myhealthcare AS (
    SELECT * FROM {{ source('health', 'health_care_facilities') }}
),

stg_sub_counties AS (
    SELECT DISTINCT
        md5(sub_county::text) as sub_county_hash,
        sub_county
    FROM myhealthcare
)

SELECT * FROM stg_sub_counties