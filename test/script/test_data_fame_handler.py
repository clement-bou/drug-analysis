import os

import pytest
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from src.tools.DataFrameHandler import DataFrameHandler


def test_to_date():
    """
    Test date conversion
    """
    df: DataFrame = pd.read_csv(os.getcwd() + "/test/sample/clinical_trials.csv")
    column: dict = {'name': 'date', 'type': 'date'}
    column: Series = DataFrameHandler.to_date(df, column)
    assert str(column.dtype) == "datetime64[ns, UTC]"


def test_to_correct_name():
    """
    Test name correction
    """
    df: DataFrame = pd.read_csv(os.getcwd() + "/test/sample/clinical_trials.csv")
    bad_name = 'scientific_title'
    correct_name = 'title'
    df: DataFrame = DataFrameHandler.correct_column_name(df, {'name': bad_name, 'correct_name': correct_name, 'type': 'str'})
    assert correct_name in df.columns


def test_to_dataframe():
    """
    Only json and CSV can be imported
    """
    with pytest.raises(Exception):
        DataFrameHandler.to_dataframe('data.txt')


def test_to_file():
    """
    Only json and CSV can be saved
    """
    with pytest.raises(Exception):
        df: DataFrame = pd.read_csv(os.getcwd() + "/test/sample/clinical_trials.csv")
        DataFrameHandler.to_file("/data/normalised/", 'data.txt', df)
