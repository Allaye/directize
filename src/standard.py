import os
import argparse
import json
# import joblib
import pickle
# import pandas as pd
from pathlib import Path
import logging
import argparse


def startproject(project_name=None):
    """
    Creates a standard data science project directory. This helps in
    easy team collaboration, rapid prototyping, easy reproducibility and fast iteration.

    The directory structure is by no means a globally recognized standard, but was inspired by
    the folder structure created by the Azure team (https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/overview)
    and Edward Ma (https://makcedward.github.io/) of OOCL.

    PROJECT STRUCTURE:

            ├── data
            │   ├── processed
            │   └── raw
            ├── models
            │   ├── cat_detect.001.pki
            ├── src
            │   ├── scripts
            │       ├── training.py
            │       ├── inference.py
            │       ├── preparation.py
            │       ├── test.py
            ├── notebooks
            ├── reports/documentation
                ├── Readme.md
            ├── pipelines


            DETAILS:
            data: Stores data used for the experiments, including raw and intermediate processed data.
                processed: stores all processed data files after cleaning, analysis, feature creation etc.
                raw: Stores all raw data obtained from databases, file storages, etc.
            models: Stores all models trained during the experiments.
            src: Stores all source code including scripts and notebook experiments.
                scripts: Stores all code scripts usually in Python/R format. This is usually refactored from the notebooks.
                    modeling: Stores all scripts and code relating to model building, evaluation and saving.
                    preparation: Stores all scripts used for data preparation and cleaning.
                    ingest: Stores all scripts used for reading in data from different sources like databases, web or file storage.
                    test: Stores all test files for code in scripts.
                notebooks: Stores all jupyter notebooks used for experimentation.

    Parameters:
    -------------
        project_name: String, Filepath
            Name of filepath of the directory to initialize and create folders.

    Returns:
    -------------
        None
    """

    DESCRIPTION = '''Creates a standard data science project directory. This helps in
                    easy team collaboration, rapid prototyping, easy reproducibility and fast iteration.       
                    The directory structure is by no means a globally recognized standard, but was inspired by
                    the folder structure created by the Azure team (https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/overview)
                  '''
    name = ''
    if project_name:
        name = project_name
    else:
        parser = argparse.ArgumentParser(prog='project', description=DESCRIPTION)
        parser.add_argument('name', default='data_project', type=str, help='Name of directory to contain folders')
        args = parser.parse_args()
        name = args.name

    print("Creating standard project structure for {}".format(name))

    base_path = os.path.join(os.getcwd(), name)
    data_path = os.path.join(base_path, 'data')
    model_path = os.path.join(base_path, 'models')
    src_path = os.path.join(base_path, 'src')
    notebook_path = os.path.join(base_path, 'notebooks')
    report_path = os.path.join(base_path, 'reports')
    pipeline_path = os.path.join(base_path, 'pipelines')

    # create data directory ####
    os.makedirs(data_path, exist_ok=True)
    os.makedirs(os.path.join(data_path, 'raw'), exist_ok=True)
    os.makedirs(os.path.join(data_path, 'processed'), exist_ok=True)

    # create models directory
    os.makedirs(os.path.join(model_path), exist_ok=True)

    # create src directory
    os.makedirs(os.path.join(src_path), exist_ok=True)
    os.open(model_path + '/inference.py', os.O_CREAT)
    os.open(src_path + '/training.py', os.O_CREAT)
    os.open(src_path + '/preparation.py', os.O_CREAT)
    os.open(src_path + '/test.py', os.O_CREAT)
    os.open(src_path + '/modeling.py', os.O_CREAT)

    # create notebooks directory
    os.makedirs(notebook_path, exist_ok=True)

    # create reports directory
    os.makedirs(report_path, exist_ok=True)

    # create pipeline directory
    os.makedirs(pipeline_path, exist_ok=True)
    # os.makedirs(os.path.join(scripts_path), exist_ok=True)
    # os.makedirs(os.path.join(scripts_path, 'ingest'), exist_ok=True)
    # os.makedirs(os.path.join(scripts_path, 'preparation'), exist_ok=True)
    # os.makedirs(os.path.join(scripts_path, 'modeling'), exist_ok=True)
    # os.makedirs(os.path.join(scripts_path, 'test'), exist_ok=True)

    # project configuration settings
    standard_config = dict(description="This object contains all configuration settings for this module.",
                           basepath=base_path, datapath=data_path, srcpath=src_path, modelpath=model_path,
                           reportpath=report_path, pipelinepath=pipeline_path, notebookpath=notebook_path)

    # create a readme.txt file to explain the folder structure
    with open(os.path.join(base_path, "README.txt"), 'w') as readme:
        readme.write(DESCRIPTION)

    with open(os.path.join(base_path, "config.txt"), 'w') as configfile:
        json.dump(standard_config, configfile)

    print("Project created successfully in {}".format(base_path))



