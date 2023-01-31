from src.task.Task import Task
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

        """
        pass
