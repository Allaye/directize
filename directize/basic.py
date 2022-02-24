import os
import json
import argparse


def basicproject(project_name=None):
    """
    Creates a basic data science project directory. This helps in
     rapid prototyping, easy reproducibility and fast iteration.

    The directory structure is by no means the best folder structure there is, but
    it helps if the project is a small project

    PROJECT STRUCTURE:

            ├── data
            │   ├── processed
            │   └── raw
             │  └── training set
                └── testing set
            ├── src
            │   ├── scripts
            ├   ├── notebooks
            │   └── notebooks
            └── reports/documentation

            DETAILS:
            data: Stores data used for the project, including raw and intermediate processed data.
                processed: stores all processed data files after cleaning, analysis, feature creation etc.
                raw: Stores all raw data obtained from databases, file storages, etc.
                training: contains cleaning data prepared for training of the model
                test: contains data to test model after training

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

    description = '''Creates a basic AI/ML/DS project directory. This helps in
                    easy team collaboration, rapid prototyping, easy reproducibility and fast iteration.       
                    The directory structure is by no means a globally recognized standard, but was inspired by the software 
                    community choices for project structure.
                  '''
    name = ''
    if project_name:
        name = project_name
    else:
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument('project_name', help='Name of the project directory to create.')
        args = parser.parse_args()
        name = args.project_name

    print('Creating project directory: {}'.format(name))

    base_path = os.path.abspath(os.path.join(os.getcwd(), name))
