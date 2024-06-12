if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import numpy as np
import pandas as pd
# from datetime import datetime

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # transformation logic
    # Add a new column 'crawled_at' with the current date and time
    # data.insert(0, "crawled_at", datetime.now(), True)
    data['Registration_number'].fillna('Unknown', inplace=True)
    data['Keph level'] = data['Keph level'].str.replace('Level ', '')
    data['Keph level'].replace('None', np.nan, inplace=True)
    data['Keph level'] = data['Keph level'].astype(float).astype("Int32")
    data['Keph level'].fillna(0, inplace=True)
    data['Regulatory body'].fillna('Unknown', inplace=True)
    data['Service_names'].replace(np.nan, 'Not Provided', inplace=True)

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output.isnull().sum().sum() == 0, 'There are still missing values in the dataframe'