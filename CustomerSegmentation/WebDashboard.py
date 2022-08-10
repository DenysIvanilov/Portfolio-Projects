import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Dataframes for plotting
original_data = pd.read_csv("CustomerSegmentation/NotebookAndModel/DATA/marketing_campaign.csv", sep="\t")
no_clusters_PCA = pd.read_csv("CustomerSegmentation/NotebookAndModel/DATA/no_clusters_pca.csv")
clustered_PCA = pd.read_csv("CustomerSegmentation/NotebookAndModel/DATA/clustered_pca.csv")
clustered_data = pd.read_csv("CustomerSegmentation/NotebookAndModel/DATA/clustered_data.csv")


def main():
    st.title("Interactive Data Dashboard For Customer Segmentation")
    st.caption("Full notebook with analysis and model creation is [here]"
               "(https://github.com/DenysIvanilov/Portfolio-Projects/blob/main/CustomerSegmentation/"
               "NotebookAndModel/Customer_Segmentation.ipynb)")

    st.header("Original Data")
    st.dataframe(original_data)
    st.caption("You can look at what each feature means [here]"
               "(https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)")

    st.subheader("Visualization of data after some Feature Engineering and PCA Dimensionality Reduction")
    fig1 = px.scatter_3d(no_clusters_PCA, x="col1", y="col2", z="col3")
    st.plotly_chart(fig1)
    st.caption("Next I used Elbow Method to get optimal number of clusters and used Bisecting K-Means Clustering.")

    st.subheader("Data points after Clustering")
    fig2 = px.scatter_3d(clustered_PCA, x="col1", y="col2", z="col3", color="Clusters",
                         color_continuous_scale=["orange", "red", "green", "blue"])
    st.plotly_chart(fig2)

    st.subheader("Profiling customers by clusters")

    fig3 = px.pie(clustered_data, values=clustered_data.Clusters.value_counts(), names=clustered_data.Clusters.unique(),
                  title="Distribution of clusters")
    st.plotly_chart(fig3)

    fig4 = px.scatter(clustered_data, x="Spent", y="Income", color="Clusters",
                      color_continuous_scale=["orange", "red", "green", "blue"])
    st.plotly_chart(fig4)

    fig5 = px.scatter_3d(clustered_data, x="TotalPurchases", y="Spent", z="Income", color="Clusters",
                         color_continuous_scale=["orange", "red", "green", "blue"])
    st.plotly_chart(fig5)

    to_plot = ["Income", "Spent", "Age", "TotalPurchases", "Is_Parent"]
    fig6 = px.parallel_coordinates(clustered_data, color="Clusters", dimensions=to_plot,
                                   color_continuous_scale=["orange", "red", "green", "blue"])
    st.plotly_chart(fig6)

    #fig7 = px.

if __name__ == "__main__":
    main()
