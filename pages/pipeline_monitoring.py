import streamlit as st
import sqlite3
import pandas as pd

st.title(
    "Pipeline Monitoring"
)

conn = sqlite3.connect(
    "database/salesops.db"
)

df = pd.read_sql(
    "SELECT * FROM opportunities",
    conn
)

pipeline = (
    df.groupby(
        "stage"
    )["expected_revenue"]
    .sum()
)

st.bar_chart(
    pipeline
)

st.dataframe(df)