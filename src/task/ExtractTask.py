from src.task.Task import Task
from src.tools.ProcessLogger import ProcessLogger

class ExtractTask(Task):
    """
    Extract data from several sources to generate a linkage graph of drug presence in scientific journals
    """

    def __init__(self, conf: dict):
        super().__init__(conf)
        self.logger = ProcessLogger.get_process_logger("ExtractTask")


    def run(self, results: dict) -> dict:
        """

        """
        pass