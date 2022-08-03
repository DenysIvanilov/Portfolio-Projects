import streamlit as st

heatmap = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/heatmap.png"
pairplot = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/pairplot.png"
dist1 = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/overalldist.png"
dist2 = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/mfdist.png"
dist3 = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/smokedist.png"
age = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/age.png"
age_smoke = "/app/portfolio-projects/MedicalInsuranceChargesRegression/graphs/agesmoke.png"


def main():
    st.title("Visualisation and EDA of Medical Insurance Charges Data")
    st.subheader("Correlation Matrix")
    st.image(image=heatmap)
    st.write("Instantly, smoking is hugely correlated with a price of insurance. "
             "Also, as we can see we have some positive correlation between age and charges,as well as bmi and charges."
             "This means as either of the values rises,the other one will rise as well. "
             "Let's look at the pairplot."
             "Note: in the pairplot 0 in smoker represents 'Not a smoker' and 1 represents 'Is a smoker'")
    st.subheader("Pairplot")
    st.image(image=pairplot)
    st.write("Just as a confirmation, we can see that for lower BMI scores charges are lower. "
             "Also, we can see prices tilting to the right as age increases.")
    st.write("As expected, charges for smokers are much bigger on average.")
    st.subheader("Distribution of Charges")
    st.image(image=dist1)
    st.image(image=dist2)
    st.write("Women tend to pay less for insurance overall.")
    st.image(image=dist3)
    st.write("This is a very strong correlation between prices of insurance and being a smoker. Almost everyone who "
             "pays cheaper don't smoke.")
    st.subheader("Scatter plots")
    st.image(image=age)
    st.write("Here we can see how age impacts prices.")
    st.image(image=age_smoke)
    st.write("And here is the same plot but for smokers vs non-smokers. Clearly smoking does have a great impact on the"
             "charges.")
    st.caption("For more analysis and conclusion you can check out whole notebook [here.]"
               "(https://github.com/DenysIvanilov/Portfolio-Projects/blob/main/"
               "MedicalInsuranceChargesRegression/NotebookAndModel/Medical_Insurance_Charges.ipynb)")


if __name__ == "__main__":
    main()
