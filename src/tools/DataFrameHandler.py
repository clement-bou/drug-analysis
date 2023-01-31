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

