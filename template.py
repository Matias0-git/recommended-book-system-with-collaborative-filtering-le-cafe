import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "books_recommender"

# folder structure - creates folders and files it will create, its standardized based on conventions
# data ingestion ingest the data from url or excel
# data validation
# data transformation apply feature engineering pywod table conversion
# train the model
# you can also have model evaluation, model push. This is your design pipeline
# all the files for end to end machine learning model
# modular coding and easy to manage why we manage it like that for the feature update so as to make it easier
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/stage_00_data_ingestion.py",
    f"{project_name}/components/stage_01_data_validation.py",
    f"{project_name}/components/stage_02_data_transformation.py",
    f"{project_name}/components/stage_03_model_trainer.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception_handler.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/log.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/util.py",
    "config/config.yaml",
    ".dockerignore",
    "app.py", # endpoint of he app
    "Dockerfile", # where we will contain the application
    "setup.py"


]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")


    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")


    else:
        logging.info(f"{filename} is already created")
