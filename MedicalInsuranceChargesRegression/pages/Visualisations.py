import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("/app/portfolio-projects/MedicalInsuranceChargesRegression/NotebookAndModel/DATA/insurance.csv")
# heatmap = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/heatmap.png"
# **** Encoding Categorical Data For Heatmap ****
data_encoded = data.copy()
le = LabelEncoder()
le.fit(data_encoded.sex.drop_duplicates())
data_encoded.sex = le.transform(data_encoded.sex)
le.fit(data_encoded.smoker.drop_duplicates())
data_encoded.smoker = le.transform(data_encoded.smoker)
le.fit(data_encoded.region.drop_duplicates())
data_encoded.region = le.transform(data_encoded.region)
# *************************************************


def main():
    st.title("Visualisation and EDA of Medical Insurance Charges Data")
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(sns.heatmap(data=data_encoded.select_dtypes(include=[np.number]).corr(), annot=True))
    st.pyplot(fig, caption="Instantly, smoking is hugely correlated with a price of insurance. "
                               "Also, as we can see we have some positive correlation between age and charges,"
                               "as well as bmi and charges. "
                               "This means as either of the values rises,"
                               "the other one will rise as well. Let's look at the pairplot.")


if __name__ == "__main__":
    main()
