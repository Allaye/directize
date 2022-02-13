import json


def save_model(model, name='model', method='jb'):
    '''
    Save a trained machine learning model in the models folder.
    Folders must be initialized using the datasist start_project function.
    Creates a folder models if datasist standard directory is not provided.

    Parameters:
    ------------
        model: binary file, Python object

            Trained model file to save in the models folder.

        name: string

            Name of the model to save it with.

        method: string

            Format to use in saving the model. It can be one of [joblib, pickle or keras].

    Returns:
    ---------
        None

    '''

    if model is None:
        raise ValueError("model: Expecting a binary model file, got 'None'")

    try:
        model_path = os.path.join(_get_path('modelpath'), name)

        if method is 'jb':
            filename = model_path + '.jbl'
            joblib.dump(model, filename)
        elif method is 'pickle':
            filename = model_path + '.pkl'
            pickle.dump(model, filename)

        elif method is 'keras':
            filename = model_path + '.h5'
            model.save(filename)

        else:
            logging.error(
                "{} not supported, specify one of [joblib, pickle, keras]".
                    format(method))

    except FileNotFoundError as e:
        msg = "models folder does not exist. Saving model to the {} folder. It is recommended that you start your " \
              "project using datasist's start_project function".format(
            name)
        logging.info(msg)

        if method is 'jb':
            filename = name + '.jbl'
            joblib.dump(model, filename)
        elif method is 'pickle':
            filename = name + '.pkl'
            pickle.dump(model, filename)

        elif method is 'keras':
            filename = name + '.h5'
            model.save(filename)

        else:
            logging.error(
                "{} not supported, specify one of [joblib, pickle, keras]".
                    format(method))


def save_data(data, name='processed_data', method='csv', loc='processed'):
    '''
    Saves data in the data folder. The data folder contains the processed and raw subfolders.

    The processed sub folder holds data that have been processed by some methods and can be used for later computation. Files like
    feature matrixes, clean data files etc.

    The raw subfolder contains data in the raw format. This can be in the form of sql tables, csv files raw texts etc.
    Folders must be initialized using the datasist start_project function.

    Parameters:
    ------------
        data: binary strings, CSV, txt

            Data to save in the specified folder

        name: string, Default proc_data

            Name of the data file to save.

        method: string, Default None

            Format to use in saving the data. If it is csv, we use the Pandas to_csv function, else we serialize with joblib.

        loc: string, Default processed.

            subfolder to save the data file to. Can be one of [processed, raw ]

    Returns:
    ---------
    None

    '''
    if data is None:
        raise ValueError("data: Expecting a dataset, got 'None'")

    if loc not in ['processed', 'raw']:
        raise ValueError(
            "loc: location not found, expecting one of [processed , raw] got {}"
                .format(loc))

    try:
        data_path = os.path.join(_get_path('datapath'), loc)

        if method is 'jb':
            filename = os.path.join(data_path, name) + '.jbl'
            joblib.dump(data, filename)

        else:
            try:
                data.to_csv(os.path.join(data_path, name) + '.csv',
                            index=False)

            except AttributeError as e:
                logging.error(
                    "The file to save must be a Pandas DataFrame. Otherwise, change method parameter to joblib")
                logging.error(e)

    except FileNotFoundError as e:
        msg = "data folder does not exist. Saving data to the {} folder. It is recommended that you start your " \
              "project using datasist's start_project function".format(
            name)
        logging.info(msg)

        if method is 'jb':
            filename = name + '.jbl'
            joblib.dump(data, filename)
        else:
            try:
                data.to_csv(name + '.csv', index=False)
            except AttributeError as e:
                logging.info(
                    "The file to save must be a Pandas DataFrame, else change method to joblib "
                )
                logging.error(e)


def save_outputs(data=None, name='proc_outputs', method='jb'):
    '''
    Saves files like vocabulary, class labels, mappings, encodings, images etc. in the outputs folder.

    Parameters:
    ------------
        data: binary strings, CSV, txt

            Data to save in the folder

        name: string, Default proc_outputs

            Name of the data file to save.

        method: string, Default joblib

            Format to use in saving the data. It can be one of [csv, joblib, pickle].

    Returns:
    ---------
    None

    '''
    if data is None:
        raise ValueError("data: Expecting a dataset, got 'None'")

    if method not in ['csv', 'jb', 'pickle']:
        raise ValueError(
            "method: Expecting one of ['csv', 'jb', 'pickle'] got {}".
                format(method))

    try:
        outputs_path = _get_path('outputpath')

        if method is 'jb':
            filename = os.path.join(outputs_path, name) + '.jbl'
            joblib.dump(data, filename)
        elif method is 'pickle':
            filename = os.path.join(outputs_path, name) + '.pkl'
            pickle.dump(data, filename)
        elif method is 'csv':
            data.to_csv(os.path.join(outputs_path, name) + '.csv', index=False)
        else:
            logging.error("An error occurred while saving the file")

    except FileNotFoundError as e:
        msg = "outputs folder does not exist. Saving data to the current folder. It is recommended that you start " \
              "your project using datasist's start_project function "
        logging.info(msg)

        if method is 'jb':
            filename = name + '.jbl'
            joblib.dump(data, filename)
        elif method is 'pickle':
            filename = name + '.pkl'
            pickle.dump(data, filename)
        elif method is 'csv':
            data.to_csv(name + '.csv', index=False)
        else:
            logging.error("An error occured while savng the file")


def get_data(name=None, path=None, loc='processed', method='jb'):
    '''
    Gets the specified data from the data directory. Directory structure must have been created using the datasist start_project function.

    Parameter:
    ------------------
        name: String, List
            name or list of dataset to retrieve from the data folder.

        path: String path, Default None
            Absolute path to the dataset

        loc: String, Default "processed"
            One of [processed, raw]. Location of the dataset in the data folder. Defaults to the 'processed'.

        method: String, Default 'jb'
            Data serialization format. Can be either jb (joblib) or csv.

    Returns:
    -------------------
        data or list of data objects
    '''
    if path:
        data_path = path
    else:
        data_path = os.path.join(_get_path('datapath'), loc, name)

    try:
        if method is 'csv':
            data = pd.read_csv(data_path)
            return data

        elif method is 'jb':
            data = joblib.load(data_path)
            logging.info(data_path)
            return data
        else:
            raise AttributeError("Method: Could not read file. File must be saved as either csv or joblib.")

    except FileNotFoundError as e:
        logging.error(e)


def get_model(name=None, path=None, method='jb'):
    '''
    Gets the specified model from the outputs/models directory. Directory structure must have been created using the datasist start_project function.

    Parameter:
    ------------------
        name: String
            name of model to retrieve from the models folder.

        path: String path, Default None
            Absolute path to the dataset

        method: String, Default 'jb'
            Data serialization format. Can be either jb (joblib) or csv.

    Returns:
    -------------------
        model or list of models objects
    '''
    if path:
        model_path = path
    else:
        model_path = os.path.join(_get_path('modelpath'), name)

    try:
        if method is 'keras':
            pass
        elif method is 'jb':
            model = joblib.load(model_path)
            return model
        elif method is 'pickle':
            model = pickle.load(model_path)
            return model
        else:
            raise AttributeError(
                "Method: Could not read object. Model must be serialized with joblib, pickle or keras.")

    except FileNotFoundError as e:
        logging.error(e)


def get_output(name=None, path=None, method='jb'):
    '''
    Gets the specified object from the outputs directory. Directory structure must have been created using the datasist start_project function.

    Parameter:
    ------------------
        name: String
            name of object to retrieve from the output folder.

        path: String path, Default None
            Absolute path to the object

        method: String, Default 'jb'
            Object serialization format. Can either be jb (joblib) or csv.

    Returns:
    -------------------
        model or list of models objects
    '''
    if path:
        output_path = path
    else:
        output_path = os.path.join(_get_path('outputpath'), name)

    try:
        if method is 'keras':
            pass
        elif method is 'jb':
            model = joblib.load(output_path)
            return model
        elif method is 'pickle':
            model = pickle.load(output_path)
            return model
        else:
            raise AttributeError(
                "Method: Could not read object. Object must be serialized with joblib, pickle or keras.")

    except FileNotFoundError as e:
        logging.error(e)


def _get_home_path(filepath):
    if filepath.endswith('src'):
        indx = filepath.index("src")
        path = filepath[0:indx]
        return path
    elif filepath.endswith('src/scripts/ingest'):
        indx = filepath.index("src/scripts/ingest")
        path = filepath[0:indx]
        return path
    elif filepath.endswith('src/scripts/preparation'):
        indx = filepath.index("src/scripts/preparation")
        path = filepath[0:indx]
        return path
    elif filepath.endswith("src/scripts/modeling"):
        indx = filepath.index("src/scripts/modeling")
        path = filepath[0:indx]
        return path
    elif filepath.endswith("src/notebooks"):
        indx = filepath.index("src/notebooks")
        path = filepath[0:indx]
        return path
    else:
        return filepath


def _get_path(dir=None):
    homedir = _get_home_path(os.getcwd())
    config_path = os.path.join(homedir, 'config.txt')

    with open(config_path) as configfile:
        config = json.load(configfile)

    path = config[dir]
    return path