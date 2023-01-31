import logging
import yaml


class ProcessLogger:
    """
        Personalized logger
    """

    with open("./config/config.yaml") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)
        logger_conf = conf['logger']

    @staticmethod
    def get_process_logger(source: str):
        logging.basicConfig(format=ProcessLogger.logger_conf['format'], level=logging.DEBUG)
        return logging.getLogger(source)

