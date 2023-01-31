from src.task.Task import Task
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

        """
        pass


