from src.task.Task import Task

class ExportTask(Task):
    """
        Export result to file
    """

    def __init__(self, conf: dict):
        super().__init__(conf)

    def run(self, results: dict) -> dict:
        """

        """
        pass
