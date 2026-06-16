import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "database/salesops.db"
)

tables = {

    "sales_reps":
    "datasets/sales_reps.csv",

    "leads":
    "datasets/leads.csv",

    "opportunities":
    "datasets/opportunities.csv",

    "activities":
    "datasets/activities.csv",

    "sla_tracking":
    "datasets/sla_tracking.csv"
}

for table, file in tables.items():

    df = pd.read_csv(file)

    df.to_sql(
        table,
        conn,
        if_exists="replace",
        index=False
    )

    print(
        f"{table} Loaded"
    )

conn.commit()

conn.close()