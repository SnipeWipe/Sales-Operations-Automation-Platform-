import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("SLA Monitoring")

conn = sqlite3.connect(
    "database/salesops.db"
)

df = pd.read_sql(
    "SELECT * FROM sla_tracking",
    conn
)

total = len(df)

met = len(
    df[
        df["sla_status"]=="Met"
    ]
)

breached = len(
    df[
        df["sla_status"]=="Breached"
    ]
)

compliance = (
    met / total
)*100

c1,c2,c3 = st.columns(3)

c1.metric(
    "Total Tickets",
    total
)

c2.metric(
    "Met SLA",
    met
)

c3.metric(
    "Compliance %",
    f"{compliance:.2f}%"
)

status = (
    df["sla_status"]
    .value_counts()
    .reset_index()
)

status.columns = [
    "Status",
    "Count"
]

fig = px.pie(
    status,
    names="Status",
    values="Count",
    title="SLA Status"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
