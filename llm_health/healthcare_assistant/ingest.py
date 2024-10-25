import pandas as pd
import minsearch


def load_data(data_path='../data/kenya_health_facilities_clean.csv'):
    df = pd.read_csv(data_path)

    documents = df.to_dict(orient='records')

    index = minsearch.Index(
        text_fields=['name', 'keph_level', 'facility_type',
        'owner', 'regulatory_body', 'county', 'constituency',
        'sub_county', 'ward', 'operation_status', 'open_whole_day',
        'open_public_holidays', 'open_weekends', 'open_late_night', 
        'approved', 'public_visible', 'closed'],
        keyword_fields=['id']
    )

    index.fit(documents)

    return index
