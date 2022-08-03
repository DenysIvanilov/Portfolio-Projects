import streamlit as st
import pandas as pd

data = pd.read_csv("/app/portfolio-projects/MedicalInsuranceChargesRegression/NotebookAndModel/DATA/insurance.csv")


def main():
    st.title("Dataset used for EDA and training the model")

    st.dataframe(data=data)

if __name__ == "__main__":
    main()