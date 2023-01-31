import pandas as pd
from pandas import DataFrame
from functools import reduce

from src.task.Task import Task
from src.tools.DataFrameHandler import DataFrameHandler
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
        Generate linkage graph of drug presence in scientific journals
        :param results: dict path of normalised data
        :return: linkage graph of the drug presence in scientific journals
        """

        graph_data: dict = {}

        dataframes_path: dict = results['normalisation']
        drugs_df = DataFrameHandler.to_dataframe(dataframes_path['drugs'])
        dataframes_path.pop('drugs')

        df_to_merge: list = []
        for source in dataframes_path:
            source_df = DataFrameHandler.to_dataframe(dataframes_path[source])
            source_merged = self.get_linkage_graph(drugs_df, source_df, source)
            df_to_merge.append(source_merged)

        merged_dataframe: DataFrame = reduce(lambda df1, df2: pd.merge(df1, df2, on='drug', how='right'), df_to_merge)
        graph_data['dataframe'] = merged_dataframe
        self.logger.info('Drug Graph generated')
        return graph_data

    def get_linkage_graph(self, drug_df: DataFrame, source_df: DataFrame, source_name: str) -> DataFrame:
        """

        :param drug_df: drugs dataframe
        :param source_df: scientific journal dataframe
        :param source_name:
        :return:
        """

        # Browse drug name inside title name to keep only those with drug inside
        drugs_title_df = pd.merge(drug_df, source_df, how="cross")
        drugs_title_df = drugs_title_df[drugs_title_df.apply(
            lambda df_merged_e: df_merged_e.drug.upper() in df_merged_e.title.upper(), axis=1
        )]

        # Concatenate row in one column to be values. The key is the drug name
        columns = ['title', 'journal', "date"]
        drugs_title_df = (
            drugs_title_df.groupby(['drug'])
            .apply(lambda x: x[columns].to_dict('records'))
            .reset_index()
            .rename(columns={0: source_name})
        )

        DataFrameHandler.logger.info(f"Linkage graph of {source_name} source generated ")
        return drugs_title_df


