# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:24:43 2026

@author: NgogodoN
"""

import streamlit as st
import pandas as pd

# --------------------------------------------------
# App configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Predicting soil properties using Spectroscopy & Machine learning algorithms",
    layout="wide"
)

# --------------------------------------------------
# Sidebar navigation
# --------------------------------------------------
st.sidebar.title("Dashboard")
section = st.sidebar.radio(
    "Go to",
    [
        "Researcher Profile",
        "Research Background",
        "Data & Methods",
        "Model Results",
        "Key Findings",
        "Contact"
    ]
)

# --------------------------------------------------
# Researcher Profile
# --------------------------------------------------
if section == "Researcher Profile":
    st.title("Researcher Profile")

    st.subheader("Nomaxabiso Ngogodo")
    st.write("**Institution:** University of Johannesburg")
    st.write("**Field:** Soil Spectroscopy, Remote Sensing & Machine Learning")

    st.markdown("""
    I am a researcher focusing on **predicting soil properties using spectroscopy and machine learning algorithms**.  
    My work evaluates the performance of **PLSR and SVM models** using **MIR and VNIR–SWIR spectral regions**.
    """)

    st.image(
        "https://cdn.pixabay.com/photo/2016/11/18/16/19/soil-1836334_1280.jpg",
        caption="Soil analysis and spectroscopy (Pixabay)",
        use_container_width=True
    )

# --------------------------------------------------
# Research Background
# --------------------------------------------------
elif section == "Research Background":
    st.title("Research Background")

    st.markdown("""
    ### Why Soil Spectroscopy?
    Soil spectroscopy provides a **rapid, non-destructive, and cost-effective** method for estimating soil properties.

    ### Research Focus
    - Predicting soil properties such as **pH and texture**
    - Comparing **MIR vs VNIR–SWIR spectroscopy**
    - Evaluating **linear (PLSR)** and **non-linear (SVM)** machine learning models
    """)

# --------------------------------------------------
# Data & Methods
# --------------------------------------------------
elif section == "Data & Methods":
    st.title("Data & Methods")

    st.markdown("""
    ### Spectral Data
    - **MIR (Mid-Infrared)**
    - **VNIR–SWIR (Visible–Near Infrared to Shortwave Infrared)**

    ### Modelling Approaches
    - **PLSR (Partial Least Squares Regression)**  
      - Suitable for linear relationships  
    - **SVM (Support Vector Machine)**  
      - Effective for non-linear soil–spectral relationships  

    ### Spectral Pre-processing
    - Applied to improve model robustness
    - Particularly beneficial for **non-linear models**
    """)

# --------------------------------------------------
# Model Results
# --------------------------------------------------
elif section == "Model Results":
    st.title("Model Results")

    st.markdown("Upload your model performance CSV files below:")

    uploaded_file = st.file_uploader(
        "Upload PLSR or SVM results (CSV)",
        type="csv"
    )

    if uploaded_file is not None:
        results = pd.read_csv(uploaded_file)

        st.subheader("Model Performance Metrics")
        st.dataframe(results, use_container_width=True)

        # Optional filtering
        st.subheader("Filter Results")
        column = st.selectbox("Select column to filter", results.columns)
        value = st.text_input("Enter value to filter by")

        if value:
            filtered = results[
                results[column].astype(str).str.contains(value, case=False)
            ]
            st.dataframe(filtered, use_container_width=True)

# --------------------------------------------------
# Key Findings
# --------------------------------------------------
elif section == "Key Findings":
    st.title("Key Research Findings")

    st.success("Summary of Key Results")

    st.markdown("""
    - **MIR spectroscopy generally outperformed VNIR–SWIR** for most soil properties  
    - **PLSR performed better for soil pH prediction**  
    - **SVM showed superior performance for soil texture (sand) prediction**  
    - **Spectral pre-processing improved non-linear model performance** in several cases  
    """)

# --------------------------------------------------
# Contact
# --------------------------------------------------
elif section == "Contact":
    st.title("Contact Information")

    st.markdown("""
    **Nomaxabiso Ngogodo**  
    University of Johannesburg  

    📧 Email: *nomangogodo@gmail.com*  
    🌍 Research Area: Soil Spectroscopy, Remote Sensing, Machine Learning
    """)

    st.info("This app was developed using **Streamlit** and deployed on **Streamlit Cloud**.")
