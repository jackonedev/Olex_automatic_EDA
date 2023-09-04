from ydata_profiling import ProfileReport
import pandas as pd
import os


def from_dataframe_to_report(df:pd.DataFrame, title:str, output_file:str) -> dict:
    output_file = absolute_output_path(output_file=output_file)
    profile = ProfileReport(df, title=title)
    profile.to_file(output_file)
    return profile.to_json()

def absolute_output_path(output_file:str) -> str:
    return os.path.abspath(output_file)