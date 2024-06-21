WITH source AS(
  SELECT
    l.county,
    f.ownership, 
    SUM(f.beds) as bed_count
  FROM 
    fact_healthcare fh
  INNER JOIN 
    dim_locations l
  ON 
    fh.code_hash = l.code_hash
  INNER JOIN 
    dim_facilities f
  ON 
    fh.facility_hash = f.facility_hash
  WHERE
    f.ownership LIKE '%ministry%'
  GROUP BY 
    l.county, f.ownership
),

ranked AS (
  SELECT *, RANK() OVER(ORDER BY bed_count DESC) as rank
  FROM source
)

SELECT * FROM ranked
WHERE rank <= 5