# A Python guide to compress CSV Data into Parquet

This repository contains the code for the Medium article [A Python guide to compress CSV Data into Parquet](https://robertochiosa.medium.com/a-python-guide-to-compress-csv-data-into-parquet-8c797136aa38).
It shows how to load csv file and save it in parquet format. This allows to speed up the data analytics pipeline and
save space on disk. 

This code uses the python libraries [pandas](https://pandas.pydata.org/)
and [pyarrow](https://arrow.apache.org/docs/python/) to perform data loading, handling and saving.

## Setup

* Create virtual environment
    ```bash
    python3 -m venv .venv
    ```
* Install requirements
    ```bash
    pip install -r requirements.txt
    ```

* Put a csv file in [data](./data) folder and name it `data.csv`. (You can use the example file in this repository if you want)
* Run the [main.py](main.py) script
    ```bash
    python main.py
    ```

## Data Availability

The csv file [`data.csv`](./data/data.csv) used in this repository in the is a subset of the Double Duct AHU dataset
contained in the
LBNL Fault Detection and Diagnostics Data Sets. The full dataset can be found at https://faultdetection.lbl.gov/data/
and is open source, all rights reserved.


