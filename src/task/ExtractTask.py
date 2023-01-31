from src.task.Task import Task

class ExtractTask(Task):
    """
    Extract data from several sources to generate a linkage graph of drug presence in scientific journals
    """

    def __init__(self, conf: dict):
        super().__init__(conf)

    def run(self, results: dict) -> dict:
        """

        """
        pass