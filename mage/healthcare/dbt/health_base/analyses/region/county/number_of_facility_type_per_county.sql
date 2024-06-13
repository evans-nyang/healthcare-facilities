SELECT 
    l.county,
    f.facility_type,
    COUNT(*) AS num_facilities
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
GROUP BY 
    l.county, f.facility_type
ORDER BY 
    l.county, num_facilities DESC;
