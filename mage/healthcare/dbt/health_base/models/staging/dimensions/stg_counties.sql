WITH source AS (
    SELECT * FROM {{ source('health', 'health_care_facilities') }}
),

stg_counties AS (
    SELECT DISTINCT
        county
    FROM source
),

county_mappings AS (
    SELECT * FROM (VALUES
        ('MOMBASA', '01'),
        ('KWALE', '02'),
        ('KILIFI', '03'),
        ('TANA RIVER', '04'),
        ('LAMU', '05'),
        ('TAITA TAVETA', '06'),
        ('GARISSA', '07'),
        ('WAJIR', '08'),
        ('MANDERA', '09'),
        ('MARSABIT', '10'),
        ('ISIOLO', '11'),
        ('MERU', '12'),
        ('THARAKA-NITHI', '13'),
        ('EMBU', '14'),
        ('KITUI', '15'),
        ('MACHAKOS', '16'),
        ('MAKUENI', '17'),
        ('NYANDARUA', '18'),
        ('NYERI', '19'),
        ('KIRINYAGA', '20'),
        ('MURANG''A', '21'),
        ('KIAMBU', '22'),
        ('TURKANA', '23'),
        ('WEST POKOT', '24'),
        ('SAMBURU', '25'),
        ('TRANS NZOIA', '26'),
        ('UASIN GISHU', '27'),
        ('ELEGEYO-MARAKWET', '28'),
        ('NANDI', '29'),
        ('BARINGO', '30'),
        ('LAIKIPIA', '31'),
        ('NAKURU', '32'),
        ('NAROK', '33'),
        ('KAJIADO', '34'),
        ('KERICHO', '35'),
        ('BOMET', '36'),
        ('KAKAMEGA', '37'),
        ('VIHIGA', '38'),
        ('BUNGOMA', '39'),
        ('BUSIA', '40'),
        ('SIAYA', '41'),
        ('KISUMU', '42'),
        ('HOMA BAY', '43'),
        ('MIGORI', '44'),
        ('KISII', '45'),
        ('NYAMIRA', '46'),
        ('NAIROBI', '47')
    ) AS county_mappings(county_name, county_id)
),

intermediate AS (
    SELECT DISTINCT
        md5(county_id::text) as county_hash,
        county_mappings.county_id,
        stg_counties.county AS county_name
    FROM
        stg_counties 
    JOIN
        county_mappings 
    ON
        stg_counties.county = county_mappings.county_name
    ORDER BY
        county_mappings.county_id ASC
)

SELECT * FROM intermediate


