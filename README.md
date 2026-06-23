# 🏗️ NMDC-02 Project Controls Dashboard

## Overview

The NMDC-02 Project Controls Dashboard is a dynamic project monitoring and reporting platform developed using Python, Streamlit, Pandas, and Plotly.

The dashboard was designed to support large-scale Data Center Infrastructure Projects by providing real-time visibility into:

- Design Progress Tracking
- Construction Progress Monitoring
- Procurement Status Management
- Manpower Deployment Analytics
- Milestone Monitoring
- Risk Register Analysis
- Executive Project Health Reporting

The application automatically reads weekly project reports from Excel files and updates all KPIs, charts, and visualizations without requiring code modifications.

---

## Business Problem

Project teams often maintain project information in multiple Excel trackers:

- Design Registers
- Procurement Logs
- Construction Reports
- Risk Registers
- Milestone Trackers
- Manpower Reports

Manual consolidation consumes significant effort and increases reporting delays.

This solution automates project controls reporting by transforming raw project data into executive-level dashboards.

---

## Key Features

### Executive Summary

Provides management with:

- Planned Progress
- Actual Progress
- Design Progress
- Procurement Progress
- Execution Progress

Includes project-wide KPI monitoring and S-Curve visualization.

---

### Design Tracker

Tracks:

- Total Drawings
- Approved Drawings
- Pending Drawings
- Discipline-wise Design Deliverables

Provides visibility into engineering progress.

---

### Work Progress Dashboard

Monitors:

- Planned vs Actual Progress
- Construction Performance
- Schedule Variance

Helps identify execution delays early.

---

### Procurement Dashboard

Tracks:

- Package Completion
- Material Delivery Status
- Procurement Progress

Supports supply chain visibility.

---

### Manpower Dashboard

Provides:

- Discipline-wise Resource Allocation
- Workforce Trends
- Deployment Analytics

Supports labor planning and productivity reviews.

---

### Milestone Dashboard

Tracks:

- Baseline Dates
- Forecast Dates
- Delay Days
- Critical Milestones

Provides milestone delay analysis and schedule monitoring.

---

### Risk Register Dashboard

Features:

- Risk Heat Map
- Probability vs Impact Analysis
- Risk Scoring
- Critical Risk Monitoring

Supports proactive risk management.

---

### Project Health Dashboard

Provides an executive view of:

- Design Health
- Procurement Health
- Construction Health
- Overall Project Performance

Uses KPI gauges and health indicators.

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Data Processing | Pandas |
| Visualization | Plotly |
| Data Source | Excel |
| Language | Python |

---

## Dynamic Excel Architecture

The dashboard reads project information dynamically using:

```python
pd.read_excel(
    uploaded_file,
    sheet_name=None
)
```

This enables:

- Automatic weekly updates
- No hardcoded datasets
- Dynamic reporting
- Scalable project monitoring

---

## Project Workflow

Excel Weekly Report
↓
Pandas Data Processing
↓
KPI Calculation
↓
Plotly Visualization
↓
Executive Dashboard

---

## Future Enhancements

- SQL Database Integration
- Power BI Integration
- Primavera P6 Connectivity
- Automated Email Reporting
- Predictive Analytics
- AI-Based Risk Forecasting

---

## To Run this code 
- streamlit run apps.py

## Author

Vishwa DN

Junior PMO Analyst | Project Controls | Data Analyst

GitHub:
https://github.com/Vishwa31262

LinkedIn: https://www.linkedin.com/in/vishwa-dn-473549323


---
