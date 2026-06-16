import streamlit as st
import sqlite3
import pandas as pd

st.title(
    "Opportunity Management"
)

conn = sqlite3.connect(
    "database/salesops.db"
)

df = pd.read_sql(
    "SELECT * FROM opportunities",
    conn
)

st.dataframe(
    df,
    use_container_width=True
)

stage_count = (
    df["stage"]
    .value_counts()
)

st.bar_chart(
    stage_count
)