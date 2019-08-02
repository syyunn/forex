import pickle


def pickle_object(python_obj, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(python_obj, f)
    return True


def load_pickle(pickle_path):
    with open(pickle_path, 'rb') as f:
        python_obj = pickle.load(f)
    return python_obj


if __name__ == "__main__":
    data = load_pickle("KRW_USD_2017.pkl")
    print(data)
