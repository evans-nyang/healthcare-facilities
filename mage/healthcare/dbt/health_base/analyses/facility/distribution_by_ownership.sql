SELECT 
    f.ownership,
    COUNT(*) AS num_facilities
FROM
    fact_healthcare fh
INNER JOIN 
    dim_facilities f
ON 
    fh.facility_hash = f.facility_hash
GROUP BY 
    f.ownership
ORDER BY 
    num_facilities DESC;
