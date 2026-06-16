import sqlite3

conn = sqlite3.connect(
    "database/salesops.db"
)

cursor = conn.cursor()

# ==========================
# SALES REPS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_reps(
    rep_id INTEGER PRIMARY KEY,
    rep_name TEXT,
    region TEXT,
    experience_years INTEGER,
    status TEXT
)
""")

# ==========================
# LEADS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads(
    lead_id INTEGER PRIMARY KEY,
    industry TEXT,
    lead_source TEXT,
    company_size TEXT,
    annual_revenue REAL,
    region TEXT,
    created_date DATE
)
""")

# ==========================
# OPPORTUNITIES
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS opportunities(
    opportunity_id INTEGER PRIMARY KEY,
    lead_id INTEGER,
    rep_id INTEGER,
    expected_revenue REAL,
    stage TEXT,
    created_date DATE,
    FOREIGN KEY(rep_id) REFERENCES sales_reps(rep_id),
    FOREIGN KEY(lead_id) REFERENCES leads(lead_id))
""")

# ==========================
# ACTIVITIES
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS activities(
    activity_id INTEGER PRIMARY KEY,
    lead_id INTEGER,
    rep_id INTEGER,
    activity_type TEXT,
    activity_date DATE,
    FOREIGN KEY(lead_id) REFERENCES leads(lead_id),
    FOREIGN KEY(rep_id) REFERENCES sales_reps(rep_id)
)
""")

# ==========================
# SLA TRACKING
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS sla_tracking(
    lead_id INTEGER PRIMARY KEY,
    created_date DATE,
    first_contact_date DATE,
    FOREIGN KEY(lead_id) REFERENCES leads(lead_id)
)
""")

# ==========================
# UPLOAD HISTORY
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS upload_history(

    upload_id INTEGER PRIMARY KEY AUTOINCREMENT,

    file_name TEXT,

    upload_timestamp DATETIME
        DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

conn.close()

print(
    "Database Created Successfully"
)