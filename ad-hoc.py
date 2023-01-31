import json
import os
from logging import Logger

import yaml
import pandas as pd
from functools import reduce

from pandas import DataFrame

from src.tools.ProcessLogger import ProcessLogger


def get_normalised_data(graph_df: DataFrame) -> list:
    """
        Merge all sources in one df
    """

    sources_df: DataFrame = graph_df.drop('drug', axis=1)
    source_df_list: list = []
    for source in sources_df.columns:
        source_df_list.append(pd.json_normalize(data, record_path=[source]))

    return source_df_list


def count_references(source_list: list) -> DataFrame:
    """
        Count number of row by journal
    """

    all_sources_df: DataFrame = pd.concat(source_list).drop_duplicates()
    all_sources_df["count"] = all_sources_df.groupby(["journal"], as_index=False)["journal"].transform('count')
    all_sources_df: DataFrame = all_sources_df.drop(['title', 'date'], axis=1)
    return all_sources_df.drop_duplicates()


if __name__ == '__main__':

    # Set loader
    with open("config/config.yaml") as conf_file:
        conf: dict = yaml.load(conf_file, Loader=yaml.FullLoader)
        logger: Logger = ProcessLogger.get_process_logger("Ad-Hoc")

    # Import Graph
    graph_path: str = os.getcwd() + conf['path']['result_dir'] + 'drug_graph.json'
    with open(graph_path) as data_file:
        data: dict = json.load(data_file)
        graph: DataFrame = pd.read_json(graph_path, orient='records')

    # Process
    source_df_list: list = get_normalised_data(graph)
    source_df: DataFrame = count_references(source_df_list)

    # Return the journal with maximum of rows
    result: DataFrame = (source_df[source_df['count'] == source_df['count'].max()])
    logger.info(f"The journal with max drug references is '{result.iloc[0]['journal']}' with '{result.iloc[0]['count']}' references")

