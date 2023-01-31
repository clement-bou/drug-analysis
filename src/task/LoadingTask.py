import os

import pandas as pd
from pandas import DataFrame
from src.task.Task import Task
from src.tools.DataFrameHandler import DataFrameHandler
from src.tools.ProcessLogger import ProcessLogger


class LoadingTask(Task):
    """
        Import DataSet from JSON and CSV file and merge same data even if the format is different
    """

    def __init__(self, conf: dict):
        super().__init__(conf)
        self.logger = ProcessLogger.get_process_logger("LoadingTask")

    def run(self, results: dict) -> dict:
        """
        Loaded each file and merged them if it is from the same source. Store results in new files.
        :param results: Nothing because it's the first task of the pipeline
        :return:dict paths of loaded data frame
        """

        dataframes = {}
        for data in self.conf['data']:
            dataframe: DataFrame = self.to_dataframe(data["file"])
            dataframes[data["source"]] = dataframe

        paths = self.to_file(dataframes)
        self.logger.info('Loading task finished')
        return paths

    def to_dataframe(self, files: dict):
        """
        Load dataframe from each same source data set. Concatenate them to build only one DataFrame
        :param files: files from the same source
        :return: concatenated dataframe
        """

        dataframes: list = []
        for file in files:
            path: str = os.getcwd() + self.conf["path"]["data_dir"] + file["name"]
            df: DataFrame = DataFrameHandler.to_dataframe(path)
            dataframes.append(df)
        dataframe: DataFrame = pd.concat(dataframes, ignore_index=True)
        return dataframe

    def to_file(self, dataframes: dict):
        """
        Export DataFrame to csv file
        :param dataframes: dataframe to store
        :return: path of stored file
        """

        paths: dict = {}
        for source in dataframes:
            base_path: str = self.conf["path"]["loaded_dir"]
            paths[source] = DataFrameHandler.to_file(base_path, source + ".csv", dataframes[source])

        return paths
