from src.task.Task import Task

class NormalisationTask(Task):
    """
    Normalised data to share data format between each source
    """

    def __init__(self, conf: dict):
        super().__init__(conf)

    def run(self, results: dict) -> dict:
        """

        """
        pass


