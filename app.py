import streamlit as st
import pandas as pd
from parser import extract_results
import matplotlib.pyplot as plt

st.title("📊 Student Result Analyzer")

uploaded_file = st.file_uploader("Upload your result PDF", type="pdf")

if uploaded_file:
    results = extract_results(uploaded_file)

    if results:
        df = pd.DataFrame(results, columns=["Name", "Total"])
        df = df.sort_values(by="Total", ascending=False)
        df["Rank"] = range(1, len(df)+1)

        st.subheader("🏆 Rankings")
        st.dataframe(df)

        # Stats
        st.subheader("📈 Insights")
        st.write("Average Marks:", df["Total"].mean())
        st.write("Highest Marks:", df["Total"].max())
        st.write("Lowest Marks:", df["Total"].min())

        # Chart
        st.subheader("📊 Distribution")
        fig, ax = plt.subplots()
        ax.hist(df["Total"], bins=10)
        st.pyplot(fig)

    else:
        st.error("No valid data found in PDF")