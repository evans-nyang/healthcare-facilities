import pandas as pd
import minsearch

def transform_data(df:pd.DataFrame)-> pd.DataFrame:
    df.drop_duplicates(subset='Name')

    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # List of columns to drop
    columns_to_drop = ['registration_number', 'service_names']

    # Drop the specified columns
    df.drop(columns=columns_to_drop)

    df = df.dropna(subset=['regulatory_body', 'keph_level'])

    df.insert(0, 'id', df.index)

def load_data(data_path='../data/kenya_health_facilities_clean.csv'):
    df = pd.read_csv(data_path)

    # transform_data(df)

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
