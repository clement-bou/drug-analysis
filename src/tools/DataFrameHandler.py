import pandas as pd
import os
import yaml
from pandas import DataFrame, Series

from src.tools.ProcessLogger import ProcessLogger


class DataFrameHandler:
    """
    Common method to handle dataframe in several tasks
    """

    logger = ProcessLogger.get_process_logger("DataFrameHandler")
    with open("./config/config.yaml") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)

    @staticmethod
    def to_dataframe(file_path: str) -> DataFrame:
        """
        Convert file to dataframe
        :param file_path: file to convert
        :return: dataframe imported
        """

        dataframe: DataFrame
        if file_path.endswith(".csv"):
            dataframe = pd.read_csv(file_path)

        elif file_path.endswith("json"):
            dataframe = pd.read_json(file_path)

        else:
            raise Exception(f"Bad extension file {file_path} !")

        DataFrameHandler.logger.info(f"DataFrame imported from {file_path}")
        return dataframe

    @staticmethod
    def to_file(base_path: str, file_name: str, dataframe: DataFrame) -> str:
        """
        Convert dataframe to file
        :param base_path: directory path
        :param file_name: file name
        :param dataframe: dataframe to convert
        :return: path of converted dataframe
        """

        dir_path = os.getcwd() + base_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            DataFrameHandler.logger.info(f"Directory created : {dir_path}")

        path = dir_path + file_name
        if file_name.endswith(".csv"):
            dataframe.to_csv(path, index=False)
        elif file_name.endswith(".json"):
            dataframe.to_json(path, orient="records", indent=2)
        else:
            raise Exception(f"Extension is not recognise as a valid extension.")

        DataFrameHandler.logger.info(f"DataFrame exported : {path}")
        return path
    
    @staticmethod
    def to_date(dataframe: DataFrame, col: dict) -> Series:
        """
        Convert string date to date time.
        :param dataframe: dataframe with date
        :param col: column to convert to date datetime
        :return:
        """
        return pd.to_datetime(dataframe[col["name"]], infer_datetime_format=True, utc=True, dayfirst=True)

    @staticmethod
    def correct_column_name(dataframe: DataFrame, col: dict) -> DataFrame:
        """
        Correct name of a column by another name set in setting file
        :param dataframe: dataframe concerned by the name correction
        :param col: column need to be corrected
        :return: dataframe with corrected name
        """
        DataFrameHandler.logger.info(f"column {col['name']} name change to {col['correct_name']} ")
        return dataframe.rename(columns={col["name"]: col["correct_name"]})

