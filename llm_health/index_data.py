from elasticsearch import Elasticsearch, helpers

# Elasticsearch client setup
es_client = Elasticsearch('http://localhost:9200')

# Check if the index exists
index_name = 'medical_facilities'
if not es_client.indices.exists(index=index_name):
    # Create the index
    es_client.indices.create(index=index_name)

# Data to be indexed
data = [
    {
        "Code": 22998,
        "Name": "Kaka Medical Clinic",
        "Registration_number": None,
        "Keph_level": "Level 2",
        "Facility_type": "Dispensaries and clinic-out patient only",
        "Owner": "Private Practice - Medical Specialist",
        "Regulatory_body": None,
        "Beds": 0,
        "Cots": 0,
        "County": "KAKAMEGA",
        "Constituency": "LURAMBI",
        "Sub_county": "lurambi",
        "Ward": "SHEYWE",
        "Operation_status": "Operational",
        "Open_whole_day": "No",
        "Open_public_holidays": "No",
        "Open_weekends": "No",
        "Open_late_night": "No",
        "Service_names": None,
        "Approved": "Yes",
        "Public_visible": "Yes",
        "Closed": "No"
    },
    {
        "Code": 22985,
        "Name": "KOPANGA DISPENSARY",
        "Registration_number": None,
        "Keph_level": "Level 2",
        "Facility_type": "Basic primary health care facility",
        "Owner": "Ministry of Health",
        "Regulatory_body": None,
        "Beds": 2,
        "Cots": 1,
        "County": "MIGORI",
        "Constituency": "SUNA WEST",
        "Sub_county": "suna west sub county",
        "Ward": "WASIMBETE",
        "Operation_status": "Operational",
        "Open_whole_day": "No",
        "Open_public_holidays": "No",
        "Open_weekends": "No",
        "Open_late_night": "No",
        "Service_names": None,
        "Approved": "Yes",
        "Public_visible": "Yes",
        "Closed": "No"
    },
    {
        "Code": 22977,
        "Name": "Fairview Medical Centre",
        "Registration_number": None,
        "Keph_level": "Level 2",
        "Facility_type": "Secondary care hospitals",
        "Owner": "Private Practice - Unspecified",
        "Regulatory_body": "Nursing Council of Kenya (Private Practice)",
        "Beds": 4,
        "Cots": 0,
        "County": "NAIROBI",
        "Constituency": "EMBAKASI CENTRAL",
        "Sub_county": "embakasi central",
        "Ward": "KAYOLE SOUTH",
        "Operation_status": "Operational",
        "Open_whole_day": "No",
        "Open_public_holidays": "No",
        "Open_weekends": "Yes",
        "Open_late_night": "No",
        "Service_names": None,
        "Approved": "Yes",
        "Public_visible": "Yes",
        "Closed": "No"
    },
    {
        "Code": 22976,
        "Name": "RADIANT GROUP OF HOSPITALS-UMOJA",
        "Registration_number": None,
        "Keph_level": "Level 3",
        "Facility_type": "Secondary care hospitals",
        "Owner": "Private Practice - Unspecified",
        "Regulatory_body": "Kenya MPDB - Private Practice",
        "Beds": 34,
        "Cots": 0,
        "County": "NAIROBI",
        "Constituency": "EMBAKASI WEST",
        "Sub_county": "embakasi west",
        "Ward": "UMOJA II",
        "Operation_status": "Operational",
        "Open_whole_day": "Yes",
        "Open_public_holidays": "Yes",
        "Open_weekends": "Yes",
        "Open_late_night": "Yes",
        "Service_names": None,
        "Approved": "Yes",
        "Public_visible": "Yes",
        "Closed": "No"
    }
]

# Indexing data
actions = [
    {
        "_index": index_name,
        "_source": entry
    }
    for entry in data
]

helpers.bulk(es_client, actions)

# Verification
print("Data indexed successfully.")
