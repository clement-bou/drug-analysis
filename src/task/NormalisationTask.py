import pandas as pd
from pandas import DataFrame
from src.task.Task import Task
from src.tools.DataFrameHandler import DataFrameHandler
from src.tools.ProcessLogger import ProcessLogger


class NormalisationTask(Task):
    """
    Normalised data to share data format between each source
    """

    def __init__(self, conf: dict):
        super().__init__(conf)
        self.logger = ProcessLogger.get_process_logger("NormalisationTask")

    def run(self, results: dict) -> dict:
        """
        Normalised data to have common date format and title name
        :param results: dict path of dataframe to normalised
        :return: dict paths of dataframe normalised
        """
        normalised_df_paths: dict = {}
        loaded_df_paths: dict = results["load"]

        for source in loaded_df_paths:
            dataframe: DataFrame = DataFrameHandler.to_dataframe(loaded_df_paths[source])
            datas = [file for file in self.conf['data'] if file['source'] == source]
            columns = datas[0]["column"]

            for column in columns:
                if column['name'] == "date":
                    dataframe['date'] = DataFrameHandler.to_date(dataframe, column)
                if column.get('correct_name', False):
                    dataframe: DataFrame = DataFrameHandler.correct_column_name(dataframe, column)

            dataframe_path = DataFrameHandler.to_file(DataFrameHandler.conf['path']['normalised_dir'],
                                                      source + ".csv", dataframe)
            normalised_df_paths[source] = dataframe_path

        self.logger.info('Data format of each sources are normalised')
        return normalised_df_paths



