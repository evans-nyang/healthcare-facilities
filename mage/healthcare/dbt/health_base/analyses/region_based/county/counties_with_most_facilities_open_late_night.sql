SELECT 
    l.county,
    COUNT(*) AS num_facilities_open_late
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
    f.open_late_night = 'yes'
GROUP BY 
    l.county
ORDER BY 
    num_facilities_open_late DESC;
