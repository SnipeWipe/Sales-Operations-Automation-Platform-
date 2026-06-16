import streamlit as st
import sqlite3
import pandas as pd

st.title(
    "Sales KPI Dashboard"
)

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

total_leads = len(
    leads
)

total_revenue = (
    opps["expected_revenue"]
    .sum()
)

won_deals = len(
    opps[
        opps["stage"] ==
        "Won"
    ]
)

col1,col2,col3 = st.columns(3)

col1.metric(
    "Total Leads",
    total_leads
)

col2.metric(
    "Won Deals",
    won_deals
)

col3.metric(
    "Revenue",
    f"${total_revenue:,.0f}"
)