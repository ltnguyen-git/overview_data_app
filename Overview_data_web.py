import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

import codecs
# import sweetviz as sv

# Import profiling capability
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# ML stuff
import pycaret 
from pycaret.classification import *
# setup, compare_models, pull, save_model

def st_display_sweetviz(report_html,width=1000, height=1200):
    report_file = codecs.open(report_html, "r")
    page = report_file.read()
    components.html(page, width = width , height = height, scrolling =True)

with st.sidebar:
    st.image("https://s3.amazonaws.com/libapps/accounts/31258/images/Overviewlogo.png")
    st.title("Simple Exploratory Data Analysis")
    choice = st.radio("Navigation",["Upload","Profiling","Sweetviz","About"])
    st.info("EDA stands for Exploratory Data Analysis. It is an approach to analyzing and understanding data by summarizing its main characteristics and identifying patterns and relationships within it. EDA involves visualizing data using various techniques such as histograms, scatter plots, box plots, and heat maps, among others. It helps to identify outliers, missing data, and other anomalies that may affect the quality of the data. EDA is an important step in the data analysis process as it helps to inform the selection of appropriate statistical methods and models for further analysis.")

if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col= None)

if choice == "Upload":
    st.image("https://www.phpuncle.com/wp-content/uploads/2017/07/importcsv.png")
    st.title("Upload Your Data for Modelling!")
    file = st.file_uploader("Upload Your Dataset Here")
    if file:
        df = pd.read_csv(file, index_col= None)
        df.to_csv("sourcedata.csv", index =None)
        st.dataframe(df)

if choice == "Profiling":
    st.image("https://editor.analyticsvidhya.com/uploads/74223Pandas%20Profiling.png")
    st.title("Automated Exploratory Dataa Analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)


if choice == "Sweetviz":
    st.title("Sweetviz Data Analysis")
    sweetviz_button =  st.button('Sweetviz analysis') 
    if sweetviz_button:
        analyze_report = sv.analyze(df)
        # analyze_report.show_html(layout='vertical')
        st_display_sweetviz("SWEETVIZ_REPORT.html")
if choice == "About":
    st.title("Some information about me")
    st.write("Thanks for spending time on my project")
    pass
