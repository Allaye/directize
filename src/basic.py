
def basicproject(project_name):
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
                test: contains data to test model after traning

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


