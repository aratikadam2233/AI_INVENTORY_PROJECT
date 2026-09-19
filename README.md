# 📦 FORESIGHT
## AI-Powered Demand & Inventory Intelligence Platform

FORESIGHT is an AI-powered demand forecasting and inventory intelligence platform designed to help businesses predict product demand, identify stockout risks, estimate inventory requirements, and generate actionable replenishment recommendations.

The system combines **Machine Learning, Time-Series Feature Engineering, Inventory Analytics, Dynamic Simulation, and an Interactive Streamlit Dashboard** into a single platform.

---

## 🚀 Project Overview

Managing inventory efficiently is a major challenge for retail businesses.

Too much inventory can increase holding costs, while insufficient inventory can lead to stockouts and lost sales.

FORESIGHT addresses this problem by using historical retail data and machine learning to:

- Predict future product demand
- Analyze demand trends
- Estimate required safety stock
- Calculate reorder points
- Detect potential stockouts
- Simulate future inventory levels
- Recommend replenishment quantities
- Prioritize urgent inventory actions
- Provide interactive business intelligence through a dashboard

---

# 🎯 Key Objectives

The main objectives of FORESIGHT are:

 Analyze historical retail inventory data.
 Engineer meaningful demand forecasting features.
 Train a machine learning model for demand prediction
 Generate future demand forecasts.
 Simulate inventory movement over the forecast period.
 Detect stockout and inventory risks.
 Calculate safety stock and reorder points.
 Generate recommended order quantities.
 Provide interactive analytics through a web dashboard.
 Help users make data-driven inventory decisions.

---

# 🧠 System Architecture

```text
                    ┌──────────────────────┐
                    │   Retail Dataset     │
                    │  Sales + Inventory   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Data Preprocessing   │
                    │ & Cleaning           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Feature Engineering  │
                    │                      │
                    │ Lag Features         │
                    │ Rolling Statistics   │
                    │ Calendar Features    │
                    │ Inventory Features   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Chronological Split  │
                    │ Train / Test         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ XGBoost Regression   │
                    │ Demand Prediction    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Future Forecasting   │
                    │ 7-Day Recursive      │
                    │ Prediction           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Inventory Simulation │
                    │                      │
                    │ Safety Stock         │
                    │ Reorder Point        │
                    │ Inventory Coverage   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Risk Detection       │
                    │                      │
                    │ Stockout Risk        │
                    │ Reorder Priority     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ AI Recommendations   │
                    │ Replenishment        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    └──────────────────────┘