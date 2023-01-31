from src.task.Task import Task

class LoadingTask(Task):
    """
        Import DataSet from JSON and CSV file and merge same data even if the format is different
    """

    def __init__(self, conf: dict):
        super().__init__(conf)

    def run(self, results: dict) -> dict:
        """
        
        """
        pass