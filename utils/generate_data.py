from faker import Faker
import pandas as pd
import numpy as np
import random
import os

fake = Faker()

# Parent directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Dataset folder
DATASET_DIR = os.path.join(
    BASE_DIR,
    "datasets"
)

# Create folder if not exists
os.makedirs(
    DATASET_DIR,
    exist_ok=True
)

# ==========================
# SALES REPS
# ==========================

regions = [
    "East",
    "West",
    "North",
    "South"
]

sales_reps = []

for i in range(1, 51):

    sales_reps.append({

        "rep_id": i,

        "rep_name": fake.name(),

        "region": random.choice(
            regions
        ),

        "experience_years": random.randint(
            1,
            15
        ),

        "status": random.choice(
            [
                "Active",
                "Active",
                "Active",
                "Inactive"
            ]
        )
    })

sales_rep_df = pd.DataFrame(
    sales_reps
)

sales_rep_df.to_csv(
    os.path.join(
        DATASET_DIR,
        "sales_reps.csv"
    ),
    index=False
)

# ==========================
# LEADS
# ==========================

industries = [
    "Retail",
    "Healthcare",
    "Finance",
    "Technology",
    "Manufacturing"
]

sources = [
    "Website",
    "Referral",
    "Campaign",
    "Partner",
    "Cold Call"
]

leads = []

for i in range(1, 10001):

    leads.append({

        "lead_id": i,

        "industry": random.choice(
            industries
        ),

        "lead_source": random.choice(
            sources
        ),

        "company_size": random.choice(
            [
                "Small",
                "Medium",
                "Large"
            ]
        ),

        "annual_revenue": random.randint(
            100000,
            10000000
        ),

        "region": random.choice(
            regions
        ),

        "lead_status": random.choice(
        [
            "New",
            "Contacted",
            "Qualified",
            "Converted",
            "Lost"
        ])       ,

        "created_date": fake.date_between(
            start_date="-365d",
            end_date="today"
        )
    })

lead_df = pd.DataFrame(
    leads
)

lead_df.to_csv(
    os.path.join(
        DATASET_DIR,
        "leads.csv"
    ),
    index=False
)

# ==========================
# OPPORTUNITIES
# ==========================

stages = [
    "Lead",
    "Qualified",
    "Proposal",
    "Negotiation",
    "Won",
    "Lost"
]

opportunities = []

for i in range(1, 5001):

    opportunities.append({

        "opportunity_id": i,

        "lead_id": random.randint(
            1,
            10000
        ),

        "assigned_rep": random.randint(
            1,
            50
        ),

        "expected_revenue": random.randint(
            5000,
            500000
        ),

        "stage": random.choice(
            stages
        ),

        "probability": random.randint(
            10,
            100
        ),

        "created_date": fake.date_between(
            start_date="-365d",
            end_date="today"
        ),

        "expected_close_date":
        fake.date_between(
            start_date="today",
            end_date="+180d"
        )
    })

opportunity_df = pd.DataFrame(
    opportunities
)

opportunity_df.to_csv(
    os.path.join(
        DATASET_DIR,
        "opportunities.csv"
    ),
    index=False
)

# ==========================
# ACTIVITIES
# ==========================

activity_types = [
    "Call",
    "Email",
    "Meeting",
    "Demo"
]

activities = []

for i in range(1, 30001):

    activities.append({

        "activity_id": i,

        "lead_id": random.randint(
            1,
            10000
        ),

        "rep_id": random.randint(
            1,
            50
        ),

        "activity_type": random.choice(
            activity_types
        ),

        "activity_outcome":random.choice(
            [
                "Positive",
                "Neutral",
                "Negative"
            ]
        ),

        "activity_date": fake.date_between(
            start_date="-365d",
            end_date="today"
        )
    })

activity_df = pd.DataFrame(
    activities
)

activity_df.to_csv(
    os.path.join(
        DATASET_DIR,
        "activities.csv"
    ),
    index=False
)

# ==========================
# SLA
# ==========================

sla = []

for i in range(1,10001):

    created = fake.date_between(
        start_date="-365d",
        end_date="today"
    )

    due_date = created + pd.Timedelta(
        days=2
    )

    completion_date = created + pd.Timedelta(
        days=random.randint(
            0,
            5
        )
    )

    sla_status = (
        "Met"
        if completion_date <= due_date
        else "Breached"
    )

    sla.append({

        "ticket_id": i,

        "lead_id": i,

        "created_date": created,

        "due_date": due_date,

        "completion_date":
        completion_date,

        "sla_status":
        sla_status
    })
    
sla_df = pd.DataFrame(
    sla
)

sla_df.to_csv(
    os.path.join(
        DATASET_DIR,
        "sla_tracking.csv"
    ),
    index=False
)

print(
    "Datasets Created Successfully"
)