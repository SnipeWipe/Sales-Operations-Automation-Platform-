import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("Lead Allocation Dashboard")

conn = sqlite3.connect(
    "database/salesops.db"
)

query = """
SELECT *
FROM leads
"""

df = pd.read_sql(
    query,
    conn
)

st.dataframe(
    df,
    use_container_width=True
)

st.metric(
    "Total Leads",
    len(df)
)

lead_source = (
    df["lead_source"]
    .value_counts()
    .reset_index()
)

lead_source.columns = [
    "Lead Source",
    "Count"
]

fig = px.pie(
    lead_source,
    names="Lead Source",
    values="Count",
    title="Lead Distribution by Source",
    hole=0.3
)

fig.update_traces(
    textinfo="percent+label"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
