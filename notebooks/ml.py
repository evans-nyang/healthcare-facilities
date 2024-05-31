from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

@transformer
def transform(data, *args, **kwargs):
    # Specify your transformation logic here
    data['Registration_number'].fillna('Unknown', inplace=True)
    data['Keph level'].fillna(data['Keph level'].mode()[0], inplace=True)
    data['Regulatory body'].fillna('Unknown', inplace=True)
    data['Service_names'].replace(np.nan, 'Not Provided', inplace=True)

    # Define preprocessing for numeric columns (scale them)
    numeric_features = data.select_dtypes(include=['int64', 'float64']).columns
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())])

    # Define preprocessing for categorical features (encode them)
    categorical_features = data.select_dtypes(include=['object']).drop(['Service_names'], axis=1).columns
    categorical_transformer = Pipeline(steps=[
        ('encoder', OneHotEncoder(handle_unknown='ignore'))])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    # Preprocessing
    data = preprocessor.fit_transform(data)

    return data

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'


X = df.drop('Service_names', axis=1)
y = df['Service_names']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)





SELECT county, 
       COUNT(_name) AS govFacilityCount, 
       (SELECT COUNT(*) FROM health_care_facilities WHERE county = hcf.county) - COUNT(_name) AS otherFacilityCount 
FROM health_care_facilities AS hcf
WHERE _owner LIKE 'Ministry%'  
GROUP BY county 
ORDER BY govFacilityCount DESC