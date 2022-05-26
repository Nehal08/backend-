import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from tensorflow.python.keras.models import load_model
import matplotlib.pyplot as plt
import os

root = os.getcwd()

MODEL_PATH0 = os.path.join(root, 'model.h5')
MODEL_PATH1 = os.path.join(root, 'model1.h5')
MODEL_PATH2 = os.path.join(root, 'model2.h5')


def calculate(eq1,eq2,id):

    if id==0:
        model = load_model(MODEL_PATH0)
        results = model.predict(eq1)
    elif id == 1:
        model = load_model(MODEL_PATH1)
        results = model.predict(eq1)
    else:
        model = load_model(MODEL_PATH2)
        results = model.predict(eq1,eq2)
    return results

