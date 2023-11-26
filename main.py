# Author:       Roberto Chiosa
# Copyright:    Roberto Chiosa, © 2023
# Email:        roberto.chiosa@pinvision.it
#
# Created:      26/11/23
# Script Name:  main.py
# Path:         
#
# Script Description:
#
#
# Notes:

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

if __name__ == '__main__':
    csv_file_path = "./data/data.csv"
    df = pd.read_csv(csv_file_path, sep=";", decimal=",")
    table = pa.Table.from_pandas(df)
    parquet_file_path = "./data/data.parquet"
    pq.write_table(table, parquet_file_path)


