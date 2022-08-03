import streamlit as st
import pandas as pd

data = pd.read_csv("/app/portfolio-projects/MedicalInsuranceChargesRegression/NotebookAndModel/DATA/insurance.csv")


def main():
    st.title("Dataset used for EDA and training the model")

    st.dataframe(data=data)
    st.subheader("Features:")
    st.write(f"age: age of primary beneficiary")
    st.write(f"sex: insurance contractor gender, female, male")
    st.write(f"bmi: Body mass index, providing an understanding of body, weights that are "
             f"relatively high or low relative to height,objective index of body weight (kg / m ^ 2) "
             f"using the ratio of height to weight, ideally 18.5 to 24.9")
    st.write(f"children: Number of children covered by health insurance / Number of dependents")
    st.write(f"smoker: Smoking")
    st.write(f"region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.")
    st.write(f"charges: Individual medical costs billed by health insurance")


if __name__ == "__main__":
    main()
