import streamlit as st
import pandas as pd

st.title(
    "SLA Monitoring"
)

df = pd.read_csv(
    "datasets/sla_tracking.csv"
)

st.dataframe(
    df
)

violations = len(
    df[
        df["sla_status"]
        == "Breached"
    ]
)

st.metric(
    "SLA Breaches",
    violations
)