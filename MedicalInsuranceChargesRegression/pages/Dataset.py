import streamlit as st
import pandas as pd

data = pd.read_csv("/app/portfolio-projects/MedicalInsuranceChargesRegression/NotebookAndModel/DATA/insurance.csv")


def main():
    st.title("Dataset used for EDA and training the model")

    st.dataframe(data=data)
    st.write(f"age: age of primary beneficiary\n"
             f"sex: insurance contractor gender, female, male\n"
             f"bmi: Body mass index, providing an understanding of body, weights that are relatively high or low "
             f"relative to height, "
             f"objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9\n"
             f"children: Number of children covered by health insurance / Number of dependents\n"
             f"smoker: Smoking\n"
             f"region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.\n"
             f"charges: Individual medical costs billed by health insurance\n")


if __name__ == "__main__":
    main()
