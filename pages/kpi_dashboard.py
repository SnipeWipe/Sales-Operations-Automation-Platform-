import streamlit as st
import sqlite3
import pandas as pd

st.title("Executive KPI Dashboard")

conn = sqlite3.connect(
    "database/salesops.db"
)

leads = pd.read_sql(
    "SELECT * FROM leads",
    conn
)

opps = pd.read_sql(
    "SELECT * FROM opportunities",
    conn
)

total_leads = len(leads)

pipeline_value = (
    opps["expected_revenue"]
    .sum()
)

won = len(
    opps[
        opps["stage"]=="Won"
    ]
)

win_rate = (
    won /
    len(opps)
)*100

c1,c2,c3 = st.columns(3)

c1.metric(
    "Total Leads",
    total_leads
)

c2.metric(
    "Pipeline Value",
    f"${pipeline_value:,.0f}"
)

c3.metric(
    "Win Rate",
    f"{win_rate:.2f}%"
)
