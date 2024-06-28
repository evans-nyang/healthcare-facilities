SELECT 
    l.county,
    f.keph_level,
    f.ownership,
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
    l.county, f.keph_level, f.ownership
ORDER BY 
    l.county, f.keph_level, f.ownership;
