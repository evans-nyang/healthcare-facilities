WITH top_10_percent_facilities AS (
    SELECT 
        f.facility_hash,
        f.facility_name,
        f.facility_type,
        f.ownership,
        f.beds,
        f.open_weekends,
        f.open_public_holidays,
        l.county
    FROM 
        dim_facilities f
    INNER JOIN 
        fact_healthcare fh
    ON 
        f.facility_hash = fh.facility_hash
    INNER JOIN 
        dim_locations l
    ON 
        fh.code_hash = l.code_hash
    WHERE 
        f.beds >= (
            SELECT 
                MIN(beds)
            FROM (
                SELECT 
                    beds,
                    NTILE(10) OVER (ORDER BY beds DESC) AS decile
                FROM 
                    dim_facilities
            ) AS bed_distribution
            WHERE 
                decile = 1
        )
)
SELECT 
    facility_name,
    facility_type,
    ownership,
    beds,
    county,
    open_weekends,
    open_public_holidays
FROM 
    top_10_percent_facilities
ORDER BY 
    beds DESC;
