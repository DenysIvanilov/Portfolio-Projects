import numpy as np
import pickle
import pandas as pd

model_filename = "/MedicalInsuranceChargesRegression/Notebook And " \
                 "Model/trained_model.pkl "
scaler_filename = "/MedicalInsuranceChargesRegression/Notebook And " \
                  "Model/trained_scaler.pkl "

loaded_model = pickle.load(open(model_filename, "rb"))
loaded_scaler = pickle.load(open(scaler_filename, "rb"))


def predict_charge(data):
    data = pd.DataFrame.from_dict(data)
    scaled_data = loaded_scaler.transform(data)
    return loaded_model.predict(scaled_data)[0]
