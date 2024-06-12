WITH myhealthcare AS (
    SELECT * FROM {{ source('health', 'health_care_facilities') }}
),

stg_constituencies AS (
    SELECT DISTINCT
        md5(constituency::text) as constituency_hash,
        constituency
    FROM myhealthcare
)

SELECT * FROM stg_constituencies