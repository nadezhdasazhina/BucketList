import pickle
import os
from bucketListManager import *

def save_list(bucketListManager):
    with open('file.pickle', 'wb') as file:
        pickle.dump(bucketListManager, file)


def load_list():
    if os.path.exists('file.pickle'):
        with open('file.pickle', 'rb') as file:
            bucketListManager = pickle.load(file)
            return bucketListManager
    return BucketListManager()
