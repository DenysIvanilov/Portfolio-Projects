import pickle
import pandas as pd
import streamlit as st
from predict import predict_charge

# Load Model And Scaler
model_filename = "C:/Users/suo/Desktop/Portfolio Projects/Medical Insurance Charges Regression/Notebook And " \
                 "Model/trained_model.pkl "
scaler_filename = "C:/Users/suo/Desktop/Portfolio Projects/Medical Insurance Charges Regression/Notebook And " \
                  "Model/trained_scaler.pkl "

loaded_model = pickle.load(open(model_filename, "rb"))
loaded_scaler = pickle.load(open(scaler_filename, "rb"))


# Streamlit App
def main():
    st.title("Medical Insurance Price Prediction In USA")

    age = int(st.slider("Select your age:", 18, 100))
    bmi = float(st.text_input("Your BMI Index"))
    children = int(st.text_input("Number of children covered by health insurance"))
    male_female = st.selectbox("Pick your sex", ["male", "female"])
    smoking = st.selectbox("Do you smoke?", ["Yes", "No"])
    region = st.selectbox("What region of USA do you live in?", ["Southeast", "Southwest",
                                                                 "Northeast", "Northwest"])

    # Converting Categorical Values To Numeric,i.e. data preprocessing
    if male_female == "male":
        male_female = 1
    else:
        male_female = 0

    if smoking == "yes":
        smoking = 1
    else:
        smoking = 0

    regions_dict = {"Northwest": 0, "Southeast": 0, "Southwest": 0}
    for key in regions_dict.items():
        if key == region:
            regions_dict[key] = 1

    prediction = ""

    if st.button("Predict Price"):
        data = {"age": [age], "bmi": [bmi], "children": [children], "sex_male": [male_female], "smoker_yes": [smoking],
                "region_northwest": [regions_dict["Northwest"]],
                "region_southeast": [regions_dict["Southeast"]], "region_southwest": [regions_dict["Southwest"]]}
        prediction = predict_charge(data)

    st.success(prediction)


if __name__ == "__main__":
    main()
