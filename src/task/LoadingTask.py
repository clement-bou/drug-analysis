from src.task.Task import Task
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
        
        """
        pass