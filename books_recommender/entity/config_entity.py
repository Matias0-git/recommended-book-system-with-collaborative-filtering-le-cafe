from collections import namedtuple

DataIngestionConfig = namedtuple("DatasetConfig", ["data_download_url", "ingested_dir", "raw_data_dir"])
