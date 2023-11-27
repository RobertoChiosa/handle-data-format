# Author:       Roberto Chiosa
# Copyright:    Roberto Chiosa, © 2023
# Email:        roberto.chiosa@gmail.com
#
# Created:      26/11/23
# Script Name:  main.py
# Path:         
#
# Script Description:
#
#
# Note: the bigger the file gets the more convenient it is to use parquet
# files. For small files the loading time is comparable, or even better for csv files.

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
import time

if __name__ == '__main__':
    # Load and convert csv file into parquet
    csv_file_path = "./data/data.csv"
    df = pd.read_csv(csv_file_path, sep=";", decimal=",")
    table = pa.Table.from_pandas(df)
    parquet_file_path = "./data/data.parquet"
    pq.write_table(table, parquet_file_path)

    # Print file sizes
    print("CSV file size: ", os.path.getsize(csv_file_path) / 1024, "KB")
    print("Parquet file size: ", os.path.getsize(parquet_file_path) / 1024, "KB")

    # Read files and print loading times
    tic = time.time()
    df = pd.read_csv(csv_file_path, sep=";", decimal=",")
    toc = time.time()
    print("CSV file read time: ", toc - tic)

    tic = time.time()
    table = pq.read_table(parquet_file_path)
    toc = time.time()
    print("Parquet file read time: ", toc - tic)
