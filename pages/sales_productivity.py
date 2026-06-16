import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title(
    "Sales Productivity Analytics"
)

conn = sqlite3.connect(
    "database/salesops.db"
)

activities = pd.read_sql(
    "SELECT * FROM activities",
    conn
)

activity_count = (
    activities
    .groupby("rep_id")
    .size()
    .reset_index(
        name="Activities"
    )
)

fig = px.bar(
    activity_count,
    x="rep_id",
    y="Activities",
    title="Activities by Sales Rep"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

top_rep = (
    activity_count
    .sort_values(
        "Activities",
        ascending=False
    )
    .head(10)
)

st.subheader(
    "Top Performing Reps"
)

st.dataframe(
    top_rep,
    use_container_width=True
)
