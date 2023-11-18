import pandas


def read_csv_file(file_path):
    pandas_df = pandas.read_csv(file_path, delimiter=";")
    return pandas_df