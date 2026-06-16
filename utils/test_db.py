import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/salesops.db"
)

query = """
SELECT *
FROM leads
LIMIT 10
"""

df = pd.read_sql(
    query,
    conn
)

print(df)

conn.close()