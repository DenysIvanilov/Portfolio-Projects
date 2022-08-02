import streamlit as st
from predict import predict_charge


# Streamlit App
def main():
    st.title("Medical Insurance Price Prediction In USA")

    age = st.slider("Select your age:", 18, 100)
    bmi = st.text_input("Your BMI Index")
    children = st.text_input("Number of children covered by health insurance")
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
        data = {"age": [int(age)], "bmi": [float(bmi)], "children": [children], "sex_male": [male_female],
                "smoker_yes": [int(smoking)],
                "region_northwest": [regions_dict["Northwest"]],
                "region_southeast": [regions_dict["Southeast"]], "region_southwest": [regions_dict["Southwest"]]}
        prediction = predict_charge(data)

    st.success(prediction)

    st.write(
        "You can check out EDA and Model Creation [here.]"
        "(https://github.com/DenysIvanilov/Portfolio-Projects/blob/main/"
        "Medical%20Insurance%20Charges%20Regression/Notebook%20And%20Model/Medical_Insurance_Charges.ipynb)")


if __name__ == "__main__":
    main()
