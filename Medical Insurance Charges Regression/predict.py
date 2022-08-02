import numpy as np
import pickle
import pandas as pd

model_filename = "C:/Users/suo/Desktop/Portfolio Projects/Medical Insurance Charges Regression/Notebook And " \
                 "Model/trained_model.pkl "
scaler_filename = "C:/Users/suo/Desktop/Portfolio Projects/Medical Insurance Charges Regression/Notebook And " \
                  "Model/trained_scaler.pkl "

loaded_model = pickle.load(open(model_filename, "rb"))
loaded_scaler = pickle.load(open(scaler_filename, "rb"))


def predict_charge(data):
    data = {"age": [19], "bmi": [27.9], "children": [0], "sex_male": [0], "smoker_yes": [1], "region_northwest": [0],
            "region_southeast": [0], "region_southwest": [1]}
    data = pd.DataFrame.from_dict(data)
    scaled_data = loaded_scaler.transform(data)
    return loaded_model.predict(scaled_data)[0]
