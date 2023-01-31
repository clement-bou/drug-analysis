from abc import ABC, abstractmethod


class Task(ABC):
    """
        Abstract class to conformism Task format
    """
    def __init__(self, conf: dict):
        """
        :param conf: format conf for personalised logger
        """
        self.conf = conf

    @abstractmethod
    def run(self, results: dict) -> dict:
        """
        method that can't be implemented, here for Inheritance
        :param results: dict of data
        :return: dict of data
        """
        pass
