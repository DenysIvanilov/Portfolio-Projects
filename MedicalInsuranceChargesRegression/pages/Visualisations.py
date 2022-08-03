import streamlit as st

heatmap = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/heatmap.png"


def main():
    st.title("Visualisation and EDA of Medical Insurance Charges Data")

    st.image(heatmap, caption="Instantly, smoking is hugely correlated with a price of insurance. "
                              "Also, as we can see we have some positive correlation between age and charges,"
                              "as well as bmi and charges. "
                              "This means as either of the values rises,"
                              "the other one will rise as well. Let's look at the pairplot.")


if __name__ == "__main__":
    main()