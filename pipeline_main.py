import yaml
from logging import Logger

from src.tools.ProcessLogger import ProcessLogger
from src.task.LoadingTask import LoadingTask


if __name__ == '__main__':
    with open("./config/config.yaml") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)

    logger: Logger = ProcessLogger.get_process_logger("Pipeline")

    pipeline: dict = {
        "load": LoadingTask(conf),
    }

    logger.info("Start of pipeline")

    response: dict = {}
    for task in pipeline:
        logger.info(f"Launch {task} task")
        response[task] = pipeline[task].run(response)

    logger.info("End of pipeline")

