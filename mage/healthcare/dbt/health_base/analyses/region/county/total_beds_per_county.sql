WITH source AS (
  SELECT * FROM fact_healthcare
),

locations AS (
  SELECT * FROM dim_locations 
),

facilities AS (
  SELECT * FROM dim_facilities 
),

proxy AS (
  SELECT 
    source.code_hash,
    locations.county,
    facilities.ownership
  FROM source
  INNER JOIN locations 
  ON source.code_hash = locations.code_hash
  INNER JOIN facilities 
  ON source.stg_facilities
)

SELECT * FROM proxy

SELECT  FROM source