import pickle


def pickle_object(python_obj, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(python_obj, f)
    return True
