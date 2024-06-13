SELECT 
    f.ownership,
    f.facility_type,
    COUNT(*) AS num_facilities
FROM
    fact_healthcare fh
INNER JOIN 
    dim_facilities f
ON 
    fh.facility_hash = f.facility_hash
GROUP BY 
    f.ownership, f.facility_type
ORDER BY 
    f.ownership, num_facilities DESC;
