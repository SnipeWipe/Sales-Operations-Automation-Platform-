import streamlit as st
import sqlite3
import pandas as pd

st.title("Reporting Automation")

conn = sqlite3.connect(
    "database/salesops.db"
)

# ==========================
# LOAD DATA
# ==========================

leads = pd.read_sql(
    "SELECT * FROM leads",
    conn
)

opportunities = pd.read_sql(
    "SELECT * FROM opportunities",
    conn
)

activities = pd.read_sql(
    "SELECT * FROM activities",
    conn
)

sla = pd.read_sql(
    "SELECT * FROM sla_tracking",
    conn
)

# ==========================
# REPORT PREVIEW
# ==========================

report_type = st.selectbox(
    "Select Report",
    [
        "Leads Report",
        "Opportunities Report",
        "Activities Report",
        "SLA Report"
    ]
)

if report_type == "Leads Report":
    report_df = leads

elif report_type == "Opportunities Report":
    report_df = opportunities

elif report_type == "Activities Report":
    report_df = activities

else:
    report_df = sla

st.subheader("Report Preview")

st.dataframe(
    report_df,
    use_container_width=True
)

# ==========================
# REPORT SUMMARY
# ==========================

st.subheader("Summary")

col1, col2 = st.columns(2)

col1.metric(
    "Total Records",
    len(report_df)
)

col2.metric(
    "Columns",
    len(report_df.columns)
)

# ==========================
# DOWNLOAD CSV
# ==========================

csv = report_df.to_csv(
    index=False
)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name=report_type.lower().replace(
        " ",
        "_"
    ) + ".csv",
    mime="text/csv"
)

# ==========================
# DOWNLOAD EXCEL
# ==========================

excel_file = report_df.to_excel(
    "temp_report.xlsx",
    index=False
)

with open(
    "temp_report.xlsx",
    "rb"
) as f:

    st.download_button(
        label="Download Excel Report",
        data=f,
        file_name=report_type.lower().replace(
            " ",
            "_"
        ) + ".xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )