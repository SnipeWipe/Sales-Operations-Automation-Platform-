import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("Pipeline Monitoring")

conn = sqlite3.connect(
    "database/salesops.db"
)

df = pd.read_sql(
    "SELECT * FROM opportunities",
    conn
)

total_pipeline = df[
    "expected_revenue"
].sum()

avg_deal_size = df[
    "expected_revenue"
].mean()

won_deals = len(
    df[df["stage"]=="Won"]
)

total_deals = len(df)

win_rate = (
    won_deals /
    total_deals * 100
)

c1,c2,c3 = st.columns(3)

c1.metric(
    "Pipeline Value",
    f"${total_pipeline:,.0f}"
)

c2.metric(
    "Average Deal Size",
    f"${avg_deal_size:,.0f}"
)

c3.metric(
    "Win Rate",
    f"{win_rate:.2f}%"
)

stage_count = (
    df["stage"]
    .value_counts()
    .reset_index()
)

stage_count.columns = [
    "Stage",
    "Count"
]

fig = px.bar(
    stage_count,
    x="Stage",
    y="Count",
    title="Pipeline by Stage"
)

st.plotly_chart(
    fig,
    use_container_width=True
)