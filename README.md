# Sales Operations Automation Platform

## App Link - https://evrhyk9le98j7ktk5aqddx.streamlit.app

## Overview

The Sales Operations Automation Platform is an end-to-end analytics and workflow automation solution built using Python, SQL, SQLite, Streamlit, and Pandas.

The platform simulates real-world sales operations processes including lead allocation, opportunity tracking, pipeline monitoring, SLA compliance management, sales productivity analytics, KPI reporting, and automated stakeholder reporting.

This project demonstrates how organizations can streamline sales operations, improve visibility into business performance, and automate reporting through interactive dashboards.

---

## Features

### Lead Allocation Dashboard
- Lead distribution analysis
- Lead source tracking
- Lead repository management
- Interactive visualizations

### Opportunity Management
- Opportunity tracking
- Deal stage monitoring
- Revenue opportunity analysis
- Sales pipeline visibility

### Pipeline Monitoring
- Total pipeline value tracking
- Average deal size analysis
- Win rate monitoring
- Opportunity stage distribution

### SLA Monitoring Dashboard
- SLA compliance tracking
- Breached vs. met SLA analysis
- Operational performance monitoring
- SLA status reporting

### Sales Productivity Analytics
- Sales activity tracking
- Representative performance analysis
- Productivity monitoring
- Top performer identification

### Executive KPI Dashboard
- Total leads generated
- Pipeline revenue value
- Win rate calculation
- Executive business metrics

### Reporting Automation
- Automated report generation
- CSV report downloads
- Business data exports
- Stakeholder reporting support

---

## Technology Stack

- Python
- SQL
- SQLite
- Streamlit
- Pandas
- Plotly
- Faker

---

## Project Architecture

```text
Sales Operations Automation Platform
│
├── app.py
│
├── database
│   └── salesops.db
│
├── datasets
│   ├── leads.csv
│   ├── opportunities.csv
│   ├── activities.csv
│   ├── sales_reps.csv
│   └── sla_tracking.csv
│
├── pages
│   ├── 1_Lead_Allocation.py
│   ├── 2_Opportunity_Management.py
│   ├── 3_Pipeline_Monitoring.py
│   ├── 4_SLA_Monitoring.py
│   ├── 5_Sales_Productivity.py
│   ├── 6_KPI_Dashboard.py
│   └── 7_Reporting_Automation.py
│
├── utils
│   ├── generate_data.py
│   ├── create_db.py
│   ├── load_data.py
│   └── test_db.py
│
├── requirements.txt
└── README.md
```

---

## Datasets Used

### Leads Dataset
Contains information about incoming business leads.

| Column |
|----------|
| lead_id |
| industry |
| lead_source |
| company_size |
| annual_revenue |
| region |
| lead_status |
| created_date |

### Opportunities Dataset
Tracks sales opportunities and revenue potential.

| Column |
|----------|
| opportunity_id |
| lead_id |
| assigned_rep |
| expected_revenue |
| stage |
| probability |
| created_date |
| expected_close_date |

### Activities Dataset
Captures sales activities performed by representatives.

| Column |
|----------|
| activity_id |
| lead_id |
| rep_id |
| activity_type |
| activity_outcome |
| activity_date |

### SLA Tracking Dataset
Monitors service level agreement performance.

| Column |
|----------|
| ticket_id |
| lead_id |
| created_date |
| due_date |
| completion_date |
| sla_status |

---

## Key Business Metrics

The platform tracks:

- Total Leads
- Pipeline Revenue
- Average Deal Size
- Win Rate
- Lead Source Performance
- Opportunity Stage Distribution
- SLA Compliance Percentage
- Sales Activity Volume
- Representative Productivity

---

## Dashboard Screens

### Lead Allocation Dashboard
Provides visibility into lead volume and source distribution.

### Opportunity Management
Tracks opportunities across different sales stages.

### Pipeline Monitoring
Monitors pipeline health, revenue potential, and conversion performance.

### SLA Monitoring Dashboard
Measures SLA compliance and identifies operational bottlenecks.

### Sales Productivity Analytics
Evaluates sales activity and representative performance.

### Executive KPI Dashboard
Presents high-level business metrics for management reporting.

### Reporting Automation
Enables report generation and data exports.

---

## Business Impact

- Automated lead allocation workflows
- Improved sales pipeline visibility
- Reduced manual reporting effort
- Enhanced SLA compliance monitoring
- Better sales performance tracking
- Faster stakeholder reporting
- Centralized business intelligence platform

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/sales-operations-automation-platform.git
cd sales-operations-automation-platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## Future Enhancements

- Automated lead assignment engine
- Revenue forecasting models
- Sales performance scorecards
- Email notification workflows
- Predictive opportunity scoring
- Executive PDF reporting
- Cloud database integration

---

## Author

**Akhilesh Pal**

Aspiring Data Scientist | Data Analyst | Machine Learning Enthusiast

GitHub: https://github.com/SnipeWipe 
Resume: https://acesse.one/oavhgh8
