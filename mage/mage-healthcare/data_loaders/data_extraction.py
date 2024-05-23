import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = "https://data.humdata.org/dataset/7b9c2851-dc37-4a88-9dcb-62e55eb91baf/resource/df6bfc55-3b25-4309-a1b4-74afba434956/download/kenya-health-facilities-2017_08_02.xlsx"

    response = requests.get(url)

    return pd.read_excel(io.BytesIO(response.content))


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
