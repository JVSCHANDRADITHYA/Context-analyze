import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Context Analyze UI", layout="centered")

st.title("Context Analyze")

# Upload Dialog box
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    # Read Excel
    df = pd.read_excel(uploaded_file)
    st.write("Preview of uploaded data:")
    st.dataframe(df.head())
    if st.button("Start Calculation"):
        st.write("")
        with st.spinner("Calculating... Please wait ⏳"):
            time.sleep(3)  # pprocessing delay
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
        st.success("Calculation Completed!")
        
        
        st.write("### Results:")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")