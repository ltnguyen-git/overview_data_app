# Overview_data_app

This code is a Streamlit app that allows users to perform simple Exploratory Data Analysis (EDA) tasks on their datasets. It has several components:

It imports the necessary libraries including Streamlit, Pandas, os, codecs and Sweetviz.

It defines a function called "st_display_sweetviz" which takes in a Sweetviz HTML file, opens it and displays its contents using the "components.html" function from Streamlit.

It creates a sidebar using the "st.sidebar" function from Streamlit, which contains an image, a title and a radio button allowing the user to select one of four options: "Upload", "Profiling", "Sweetviz" or "About".

If the user selects "Upload", they are prompted to upload a CSV file which is then read using Panda's "read_csv" function, displayed using the "dataframe" function from Streamlit and saved as a file called "sourcedata.csv".

If the user selects "Profiling", the app generates a report on the dataset using Pandas Profiling library and displays the report using the "st_profile_report" function from Streamlit.

If the user selects "Sweetviz", the app generates a report on the dataset using Sweetviz library by clicking a button and displays the report using the "st_display_sweetviz" function defined earlier.

If the user selects "About", some information about the app is displayed.

## In summary, this app provides a simple way for users to upload, visualize and summarize their datasets with easy-to-use interactive tools.

