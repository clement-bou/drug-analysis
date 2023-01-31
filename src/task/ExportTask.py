import os

from src.task.Task import Task
from src.tools.DataFrameHandler import DataFrameHandler
from src.tools.ProcessLogger import ProcessLogger


class ExportTask(Task):
    """
        Export result to file
    """

    def __init__(self, conf: dict):
        super().__init__(conf)
        self.logger = ProcessLogger.get_process_logger("ExportTask")

    def run(self, results: dict) -> dict:
        """
        Export result to json file
        :param results: linkage graph of the drug presence in several sources scientific journals
        :return: linkage graph file path
        """
        path: dict = {}

        dataframe = results['extract']['dataframe']
        final_path: str = os.getcwd() + self.conf['path']['result_dir'] + self.conf['result']['name']
        DataFrameHandler.to_file(self.conf['path']['result_dir'], self.conf['result']['name'], dataframe)

        path['path'] = final_path
        self.logger.info(f"Result exported to {final_path}")
        return path
