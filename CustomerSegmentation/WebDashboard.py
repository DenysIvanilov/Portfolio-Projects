import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

# Dataframes for plotting
original_data = pd.read_csv("/app/CustomerSegmentation/NotebookAndModel/DATA/marketing_campaign.csv", sep="\t")
no_clusters_PCA = pd.read_csv("/app/CustomerSegmentation/NotebookAndModel/DATA/no_clusters_pca.csv")
clustered_PCA = pd.read_csv("/app/CustomerSegmentation/NotebookAndModel/DATA/clustered_pca.csv")
clustered_data = pd.read_csv("/app/CustomerSegmentation/NotebookAndModel/DATA/clustered_data.csv")


def main():
    st.set_page_config(
        page_title="Web Dashboard",
        layout="wide"
    )
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
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("Next I used Elbow Method to get optimal number of clusters and used Bisecting K-Means Clustering.")

    st.subheader("Data points after Clustering")
    fig2 = px.scatter_3d(clustered_PCA, x="col1", y="col2", z="col3", color="Clusters",
                         color_continuous_scale=["orange", "red", "green", "blue"])
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Profiling")

    fig3 = px.pie(clustered_data, values=clustered_data.Clusters.value_counts(), names=clustered_data.Clusters.unique(),
                  title="Distribution of Clusters")
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.scatter(clustered_data, x="Spent", y="Income", color="Clusters",
                      color_continuous_scale=["orange", "red", "green", "blue"], title="Income vs Spent by Clusters")
    st.plotly_chart(fig4, use_container_width=True)

    fig5 = px.scatter_3d(clustered_data, x="TotalPurchases", y="Spent", z="Income", color="Clusters",
                         color_continuous_scale=["orange", "red", "green", "blue"],
                         title="Income vs Spent vs TotalPurchases by Clusters")
    st.plotly_chart(fig5, use_container_width=True)

    to_plot1 = ["Income", "Spent", "Age", "TotalPurchases", "Is_Parent"]
    st.caption("Is_Parent = 1 if True, 0 otherwise")
    fig6 = px.parallel_coordinates(clustered_data, color="Clusters", dimensions=to_plot1,
                                   color_continuous_scale=["orange", "red", "green", "blue"],
                                   title="Parallel Coordinates")
    st.plotly_chart(fig6, use_container_width=True)

    to_plot2 = ["Education", "Marital_Status", "Age", "Children", "Customer_For", "Is_Parent"]
    st.caption("Education = 0 means Post Graduate, Education = 1 means Under Graduate")
    st.caption("Marital Status = 0 means in Relationship, 1 means Single")
    for feature in to_plot2:
        st.plotly_chart(px.density_contour(clustered_data, x=feature, y="Spent", marginal_x="histogram", height=800,
                                           color_discrete_map={1: "orange", 2: "red", 3: "green", 4: "blue"},
                                           marginal_y="histogram", color="Clusters"), use_container_width=True)

    st.caption("[You can check out full work and summary here.](https://github.com/DenysIvanilov/Portfolio-Projects/"
               "blob/main/CustomerSegmentation/NotebookAndModel/Customer_Segmentation.ipynb)")


if __name__ == "__main__":
    main()
