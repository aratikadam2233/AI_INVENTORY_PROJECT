import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="FORESIGHT | AI Inventory Intelligence",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
       ====================================================== */

    .stApp {
        background: #f4f7fb;
    }

    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1550px;
    }

    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {
        background: #0f172a;
    }

    section[data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    section[data-testid="stSidebar"] label {
        font-weight: 600;
    }

    /* ======================================================
       MAIN HEADER
       ====================================================== */

    .hero {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #1e3a8a 55%,
            #2563eb 100%
        );

        padding: 34px 38px;
        border-radius: 22px;
        margin-bottom: 28px;

        box-shadow:
            0 10px 30px rgba(15, 23, 42, 0.16);
    }

    .hero-title {
        color: white !important;
        font-size: 42px;
        font-weight: 850;
        margin: 0;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        color: #dbeafe !important;
        font-size: 16px;
        margin-top: 8px;
    }

    .hero-badges {
        margin-top: 18px;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.14);
        color: white !important;
        border: 1px solid rgba(255,255,255,0.20);
        padding: 7px 13px;
        border-radius: 999px;
        margin-right: 8px;
        font-size: 12px;
        font-weight: 650;
    }

    /* ======================================================
       SECTION HEADINGS
       ====================================================== */

    .section-heading {
        color: #0f172a !important;
        font-size: 25px;
        font-weight: 800;
        margin-top: 32px;
        margin-bottom: 16px;
    }

    .section-description {
        color: #64748b !important;
        font-size: 14px;
        margin-top: -7px;
        margin-bottom: 18px;
    }

    /* ======================================================
       KPI CARDS
       ====================================================== */

    .kpi-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 21px;
        min-height: 145px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.07);

        transition: 0.2s ease;
    }

    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow:
            0 9px 25px rgba(15, 23, 42, 0.11);
    }

    .kpi-icon {
        font-size: 23px;
        margin-bottom: 7px;
    }

    .kpi-title {
        color: #64748b !important;
        font-size: 12px;
        font-weight: 750;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .kpi-value {
        color: #0f172a !important;
        font-size: 30px;
        font-weight: 850;
        margin-top: 7px;
    }

    .kpi-subtitle {
        color: #94a3b8 !important;
        font-size: 12px;
        margin-top: 5px;
    }

    /* ======================================================
       TRAINING / TESTING
       ====================================================== */

    .training-card {
        background: #ffffff !important;
        border: 1px solid #dbe3ef;
        border-radius: 18px;
        padding: 22px;
        min-height: 135px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.06);
    }

    .training-icon {
        font-size: 25px;
        margin-bottom: 9px;
    }

    .training-label {
        color: #64748b !important;
        font-size: 12px;
        font-weight: 750;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

    .training-value {
        color: #0f172a !important;
        font-size: 27px;
        font-weight: 850;
        margin-top: 7px;
    }

    .training-subtitle {
        color: #64748b !important;
        font-size: 12px;
        margin-top: 5px;
    }

    .training-banner {
        background: linear-gradient(
            135deg,
            #eff6ff,
            #f8fafc
        ) !important;

        border: 1px solid #bfdbfe;
        border-left: 5px solid #2563eb;

        border-radius: 16px;
        padding: 20px 22px;
        margin-bottom: 18px;
    }

    .training-banner-title {
        color: #1e3a8a !important;
        font-size: 17px;
        font-weight: 800;
    }

    .training-banner-text {
        color: #475569 !important;
        font-size: 13px;
        margin-top: 7px;
        line-height: 1.7;
    }

    /* ======================================================
       FORECAST BANNER
       ====================================================== */

    .forecast-banner {
        background: linear-gradient(
            135deg,
            #eef2ff,
            #f8fafc
        ) !important;

        border: 1px solid #c7d2fe;
        border-left: 5px solid #6366f1;

        border-radius: 18px;
        padding: 23px;

        margin-bottom: 20px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .forecast-title {
        color: #312e81 !important;
        font-size: 19px;
        font-weight: 800;
    }

    .forecast-text {
        color: #475569 !important;
        font-size: 13px;
        line-height: 1.7;
        margin-top: 7px;
    }

    .forecast-meta {
        color: #334155 !important;
        font-size: 13px;
        margin-top: 13px;
        font-weight: 650;
    }

    /* ======================================================
       RECOMMENDATION CARDS
       ====================================================== */

    .recommendation-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 18px 21px;
        margin-bottom: 13px;

        box-shadow:
            0 3px 12px rgba(15, 23, 42, 0.05);
    }

    .recommendation-title {
        color: #0f172a !important;
        font-size: 16px;
        font-weight: 800;
        margin-bottom: 9px;
    }

    .recommendation-text {
        color: #475569 !important;
        font-size: 13px;
        line-height: 1.65;
        margin-top: 9px;
    }

    .recommendation-metrics {
        color: #64748b !important;
        font-size: 12px;
        line-height: 1.8;
    }

    /* ======================================================
       RISK BADGES
       ====================================================== */

    .risk-high {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 999px;
        background: #fee2e2 !important;
        color: #b91c1c !important;
        font-size: 10px;
        font-weight: 800;
    }

    .risk-medium {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 999px;
        background: #fef3c7 !important;
        color: #92400e !important;
        font-size: 10px;
        font-weight: 800;
    }

    .risk-low {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 999px;
        background: #dcfce7 !important;
        color: #166534 !important;
        font-size: 10px;
        font-weight: 800;
    }

    /* ======================================================
       MODEL INFORMATION
       ====================================================== */

    .info-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0;
        border-radius: 17px;
        padding: 23px;
        min-height: 180px;

        box-shadow:
            0 4px 15px rgba(15, 23, 42, 0.05);
    }

    .info-card-title {
        color: #0f172a !important;
        font-size: 17px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .info-card-text {
        color: #64748b !important;
        font-size: 13px;
        line-height: 1.75;
    }

    /* ======================================================
       MODEL METRIC
       ====================================================== */

    .model-metric {
        background: #ffffff !important;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 18px;
        text-align: center;

        box-shadow:
            0 4px 14px rgba(15, 23, 42, 0.05);
    }

    .model-metric-label {
        color: #64748b !important;
        font-size: 12px;
        font-weight: 700;
    }

    .model-metric-value {
        color: #0f172a !important;
        font-size: 25px;
        font-weight: 850;
        margin-top: 6px;
    }

    /* ======================================================
       FOOTER
       ====================================================== */

    .footer-box {
        background: linear-gradient(
            135deg,
            #0f172a,
            #1e293b
        );

        color: white !important;
        border-radius: 18px;
        padding: 28px;
        text-align: center;
        margin-top: 35px;
    }

    .footer-title {
        color: white !important;
        font-size: 20px;
        font-weight: 800;
    }

    .footer-text {
        color: #cbd5e1 !important;
        font-size: 13px;
        margin-top: 7px;
    }

    /* ======================================================
       STREAMLIT METRIC FIX
       ====================================================== */

    div[data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 15px;
    }

    div[data-testid="stMetric"] label {
        color: #64748b !important;
    }

    div[data-testid="stMetricValue"] {
        color: #0f172a !important;
    }

    /* ======================================================
       TABLE
       ====================================================== */

    [data-testid="stDataFrame"] {
        border-radius: 14px;
        overflow: hidden;
    }

    /* ======================================================
       DOWNLOAD BUTTON
       ====================================================== */

    .stDownloadButton button {
        width: 100%;
        border-radius: 10px;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD HISTORICAL DATA
# ============================================================

@st.cache_data
def load_historical_data():

    file_path = "foresight_inventory_predictions.csv"

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    numeric_columns = [
        "Inventory Level",
        "Units Sold",
        "Predicted Demand",
        "Safety Stock",
        "Reorder Point",
        "Inventory Coverage Days",
        "Recommended Order Qty"
    ]

    for col in numeric_columns:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df


# ============================================================
# LOAD FUTURE DATA
# ============================================================

@st.cache_data
def load_future_data():

    file_path = "foresight_final_forecast_inventory.csv"

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    numeric_columns = [
        "Predicted Demand",
        "Opening Inventory",
        "Received Today",
        "Ending Inventory",
        "Rolling_Std_28",
        "Safety Stock",
        "Reorder Point",
        "Inventory Coverage Days",
        "Recommended Order Qty",
        "Stockout Quantity",
        "Available Inventory",
        "Days of Cover"
    ]

    for col in numeric_columns:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df


# ============================================================
# LOAD DATASETS
# ============================================================

try:

    df = load_historical_data()

except FileNotFoundError:

    st.error(
        "❌ foresight_inventory_predictions.csv was not found."
    )

    st.info(
        "Place the historical CSV inside D:\\FORESIGHT\\dashboard"
    )

    st.stop()


try:

    future_df = load_future_data()

except FileNotFoundError:

    future_df = pd.DataFrame()

    st.warning(
        "⚠️ Future forecast CSV was not found. "
        "Historical dashboard will still work."
    )


# ============================================================
# HEADER
# ============================================================

st.html(
    """
    <div class="hero">

        <div class="hero-title">
            📦 FORESIGHT
        </div>

        <div class="hero-subtitle">
            AI-Powered Demand & Inventory Intelligence Platform
        </div>

        <div class="hero-badges">

            <span class="hero-badge">
                🤖 XGBoost AI
            </span>

            <span class="hero-badge">
                📈 Demand Forecasting
            </span>

            <span class="hero-badge">
                📦 Inventory Intelligence
            </span>

            <span class="hero-badge">
                ⚠️ Risk Detection
            </span>

            <span class="hero-badge">
                🔮 7-Day Forecast
            </span>

        </div>

    </div>
    """
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔎 Filters")

st.sidebar.write(
    "Explore demand forecasts, inventory levels and risk intelligence."
)


# ============================================================
# HISTORICAL FILTERS
# ============================================================

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.sidebar.date_input(
    "📅 Historical Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)


stores = sorted(
    df["Store ID"].dropna().unique().tolist()
)

selected_stores = st.sidebar.multiselect(
    "🏬 Store",
    options=stores,
    default=stores
)


products = sorted(
    df["Product ID"].dropna().unique().tolist()
)

selected_products = st.sidebar.multiselect(
    "📦 Product",
    options=products,
    default=products
)


categories = sorted(
    df["Category"].dropna().unique().tolist()
)

selected_categories = st.sidebar.multiselect(
    "📁 Category",
    options=categories,
    default=categories
)


regions = sorted(
    df["Region"].dropna().unique().tolist()
)

selected_regions = st.sidebar.multiselect(
    "🌐 Region",
    options=regions,
    default=regions
)


# ============================================================
# RESET
# ============================================================

if st.sidebar.button(
    "🔄 Reset Filters",
    use_container_width=True
):

    st.rerun()


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if len(date_range) == 2:

    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    filtered_df = filtered_df[
        (filtered_df["Date"] >= start_date)
        &
        (filtered_df["Date"] <= end_date)
    ]


if selected_stores:

    filtered_df = filtered_df[
        filtered_df["Store ID"].isin(selected_stores)
    ]

else:

    filtered_df = filtered_df.iloc[0:0]


if selected_products:

    filtered_df = filtered_df[
        filtered_df["Product ID"].isin(selected_products)
    ]

else:

    filtered_df = filtered_df.iloc[0:0]


if selected_categories:

    filtered_df = filtered_df[
        filtered_df["Category"].isin(selected_categories)
    ]

else:

    filtered_df = filtered_df.iloc[0:0]


if selected_regions:

    filtered_df = filtered_df[
        filtered_df["Region"].isin(selected_regions)
    ]

else:

    filtered_df = filtered_df.iloc[0:0]


if filtered_df.empty:

    st.warning(
        "⚠️ No historical records match the selected filters."
    )

    st.stop()


# ============================================================
# INVENTORY OVERVIEW
# ============================================================

st.html(
    """
    <div class="section-heading">
        📊 Inventory Overview
    </div>

    <div class="section-description">
        Historical demand and inventory intelligence generated by the FORESIGHT platform.
    </div>
    """
)


total_records = len(filtered_df)

avg_predicted_demand = filtered_df[
    "Predicted Demand"
].mean()

high_stockout = filtered_df[
    "Stockout Risk"
].eq("HIGH").sum()

recommended_units = filtered_df[
    "Recommended Order Qty"
].sum()

avg_inventory = filtered_df[
    "Inventory Level"
].mean()


kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)


with kpi1:

    st.html(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">📊</div>

            <div class="kpi-title">
                Total Records
            </div>

            <div class="kpi-value">
                {total_records:,}
            </div>

            <div class="kpi-subtitle">
                Historical records
            </div>

        </div>
        """
    )


with kpi2:

    st.html(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">📈</div>

            <div class="kpi-title">
                Avg Predicted Demand
            </div>

            <div class="kpi-value">
                {avg_predicted_demand:,.1f}
            </div>

            <div class="kpi-subtitle">
                Units per record
            </div>

        </div>
        """
    )


with kpi3:

    stockout_percentage = (
        high_stockout / total_records * 100
        if total_records > 0
        else 0
    )

    st.html(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">⚠️</div>

            <div class="kpi-title">
                High Stockout Risk
            </div>

            <div class="kpi-value">
                {high_stockout:,}
            </div>

            <div class="kpi-subtitle">
                {stockout_percentage:.1f}% of records
            </div>

        </div>
        """
    )


with kpi4:

    st.html(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">🚚</div>

            <div class="kpi-title">
                Recommended Orders
            </div>

            <div class="kpi-value">
                {recommended_units:,.0f}
            </div>

            <div class="kpi-subtitle">
                Historical replenishment
            </div>

        </div>
        """
    )


with kpi5:

    st.html(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">📦</div>

            <div class="kpi-title">
                Avg Inventory
            </div>

            <div class="kpi-value">
                {avg_inventory:,.1f}
            </div>

            <div class="kpi-subtitle">
                Available units
            </div>

        </div>
        """
    )


# ============================================================
# TRAINING & TESTING CONFIGURATION
# ============================================================

st.html(
    """
    <div class="section-heading">
        🧪 Training & Testing Configuration
    </div>

    <div class="section-description">
        Chronological machine-learning setup used to train and evaluate the demand forecasting model.
    </div>

    <div class="training-banner">

        <div class="training-banner-title">
            🤖 XGBoost Demand Forecasting Pipeline
        </div>

        <div class="training-banner-text">
            The dataset was split chronologically to prevent future information
            from entering the training process. Lag features, rolling statistics,
            calendar features and product/store information were used for demand prediction.
        </div>

    </div>
    """
)


t1, t2, t3, t4 = st.columns(4)


with t1:

    st.html(
        """
        <div class="training-card">

            <div class="training-icon">📚</div>

            <div class="training-label">
                Training Records
            </div>

            <div class="training-value">
                56,200
            </div>

            <div class="training-subtitle">
                Historical training samples
            </div>

        </div>
        """
    )


with t2:

    st.html(
        """
        <div class="training-card">

            <div class="training-icon">🧪</div>

            <div class="training-label">
                Testing Records
            </div>

            <div class="training-value">
                14,100
            </div>

            <div class="training-subtitle">
                Chronological test samples
            </div>

        </div>
        """
    )


with t3:

    st.html(
        """
        <div class="training-card">

            <div class="training-icon">🤖</div>

            <div class="training-label">
                Model
            </div>

            <div class="training-value">
                XGBoost
            </div>

            <div class="training-subtitle">
                Regression forecasting
            </div>

        </div>
        """
    )


with t4:

    st.html(
        """
        <div class="training-card">

            <div class="training-icon">📅</div>

            <div class="training-label">
                Split Date
            </div>

            <div class="training-value">
                14 Aug 2023
            </div>

            <div class="training-subtitle">
                Chronological boundary
            </div>

        </div>
        """
    )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.html(
    """
    <div class="section-heading">
        🎯 Model Performance
    </div>

    <div class="section-description">
        Evaluation metrics calculated on the chronological test dataset.
    </div>
    """
)


m1, m2, m3, m4 = st.columns(4)


with m1:

    st.html(
        """
        <div class="model-metric">

            <div class="model-metric-label">
                MAE
            </div>

            <div class="model-metric-value">
                89.21
            </div>

        </div>
        """
    )


with m2:

    st.html(
        """
        <div class="model-metric">

            <div class="model-metric-label">
                RMSE
            </div>

            <div class="model-metric-value">
                108.88
            </div>

        </div>
        """
    )


with m3:

    st.html(
        """
        <div class="model-metric">

            <div class="model-metric-label">
                WAPE
            </div>

            <div class="model-metric-value">
                65.56%
            </div>

        </div>
        """
    )


with m4:

    st.html(
        """
        <div class="model-metric">

            <div class="model-metric-label">
                SMAPE
            </div>

            <div class="model-metric-value">
                72.19%
            </div>

        </div>
        """
    )


# ============================================================
# DEMAND ANALYSIS
# ============================================================

st.html(
    """
    <div class="section-heading">
        📈 Demand Analysis
    </div>

    <div class="section-description">
        Comparison between actual historical demand and model predictions.
    </div>
    """
)


daily_demand = (
    filtered_df
    .groupby("Date")
    .agg(
        Actual_Demand=("Units Sold", "sum"),
        Predicted_Demand=("Predicted Demand", "sum")
    )
    .reset_index()
    .sort_values("Date")
)


fig_demand = px.line(
    daily_demand,
    x="Date",
    y=[
        "Actual_Demand",
        "Predicted_Demand"
    ],
    markers=True,
    title="Actual vs Predicted Demand",
    template="plotly_white"
)


fig_demand.update_layout(
    hovermode="x unified",
    xaxis_title="Date",
    yaxis_title="Units",
    height=480
)


st.plotly_chart(
    fig_demand,
    use_container_width=True
)


actual_total = filtered_df["Units Sold"].sum()

predicted_total = filtered_df[
    "Predicted Demand"
].sum()

difference = predicted_total - actual_total

forecast_difference_pct = (
    difference / actual_total * 100
    if actual_total != 0
    else 0
)


demand_col1, demand_col2, demand_col3 = st.columns(3)


with demand_col1:

    st.metric(
        "Actual Demand",
        f"{actual_total:,.0f} units"
    )


with demand_col2:

    st.metric(
        "Predicted Demand",
        f"{predicted_total:,.0f} units"
    )


with demand_col3:

    st.metric(
        "Forecast Difference",
        f"{difference:,.0f} units",
        f"{forecast_difference_pct:.2f}%"
    )


# ============================================================
# RISK ANALYSIS
# ============================================================

st.html(
    """
    <div class="section-heading">
        ⚠️ Risk Analysis
    </div>
    """
)


risk_col1, risk_col2 = st.columns(2)


with risk_col1:

    stockout_summary = (
        filtered_df["Stockout Risk"]
        .value_counts()
        .reset_index()
    )

    stockout_summary.columns = [
        "Risk",
        "Count"
    ]

    fig_stockout = px.pie(
        stockout_summary,
        names="Risk",
        values="Count",
        hole=0.50,
        title="Stockout Risk Distribution",
        template="plotly_white"
    )

    fig_stockout.update_layout(
        height=400
    )

    st.plotly_chart(
        fig_stockout,
        use_container_width=True
    )


with risk_col2:

    overall_summary = (
        filtered_df["Overall Risk"]
        .value_counts()
        .reset_index()
    )

    overall_summary.columns = [
        "Risk",
        "Count"
    ]

    fig_overall = px.bar(
        overall_summary,
        x="Risk",
        y="Count",
        text="Count",
        title="Overall Inventory Risk",
        template="plotly_white"
    )

    fig_overall.update_traces(
        textposition="outside"
    )

    fig_overall.update_layout(
        height=400
    )

    st.plotly_chart(
        fig_overall,
        use_container_width=True
    )


# ============================================================
# DEMAND TREND
# ============================================================

st.html(
    """
    <div class="section-heading">
        📊 Demand Trend Intelligence
    </div>
    """
)


trend_summary = (
    filtered_df["Demand Trend"]
    .value_counts()
    .reset_index()
)

trend_summary.columns = [
    "Trend",
    "Count"
]


fig_trend = px.bar(
    trend_summary,
    x="Trend",
    y="Count",
    text="Count",
    title="Demand Trend Distribution",
    template="plotly_white"
)

fig_trend.update_traces(
    textposition="outside"
)

fig_trend.update_layout(
    height=400
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)


# ============================================================
# INVENTORY COVERAGE
# ============================================================

st.html(
    """
    <div class="section-heading">
        📦 Inventory Coverage
    </div>
    """
)


coverage_col1, coverage_col2 = st.columns(2)


with coverage_col1:

    coverage_data = (
        filtered_df[
            "Inventory Coverage Days"
        ]
        .replace(
            [np.inf, -np.inf],
            np.nan
        )
        .dropna()
    )

    fig_coverage = px.histogram(
        coverage_data,
        x="Inventory Coverage Days",
        nbins=30,
        title="Inventory Coverage Distribution",
        template="plotly_white"
    )

    fig_coverage.update_layout(
        height=420,
        xaxis_title="Coverage Days",
        yaxis_title="Number of Records"
    )

    st.plotly_chart(
        fig_coverage,
        use_container_width=True
    )


with coverage_col2:

    store_inventory = (
        filtered_df
        .groupby("Store ID")
        .agg(
            Average_Inventory=(
                "Inventory Level",
                "mean"
            ),
            Average_Demand=(
                "Predicted Demand",
                "mean"
            )
        )
        .reset_index()
    )

    fig_store = px.bar(
        store_inventory,
        x="Store ID",
        y=[
            "Average_Inventory",
            "Average_Demand"
        ],
        barmode="group",
        title="Inventory vs Predicted Demand by Store",
        template="plotly_white"
    )

    fig_store.update_layout(
        height=420,
        yaxis_title="Units"
    )

    st.plotly_chart(
        fig_store,
        use_container_width=True
    )


# ============================================================
# HISTORICAL AI RECOMMENDATIONS
# ============================================================

st.html(
    """
    <div class="section-heading">
        🤖 Historical AI Inventory Recommendations
    </div>
    """
)


recommendations = (
    filtered_df[
        filtered_df["Recommended Order Qty"] > 0
    ]
    .sort_values(
        "Recommended Order Qty",
        ascending=False
    )
    .head(10)
)


for _, row in recommendations.iterrows():

    risk = str(
        row["Stockout Risk"]
    ).upper()

    if risk == "HIGH":

        icon = "🔴"
        badge_class = "risk-high"
        badge_text = "HIGH STOCKOUT RISK"

    elif risk == "MEDIUM":

        icon = "🟠"
        badge_class = "risk-medium"
        badge_text = "MEDIUM STOCKOUT RISK"

    else:

        icon = "🟢"
        badge_class = "risk-low"
        badge_text = "LOW STOCKOUT RISK"


    st.html(
        f"""
        <div class="recommendation-card">

            <div class="recommendation-title">

                {icon}
                {row["Store ID"]}
                |
                {row["Product ID"]}

                &nbsp;&nbsp;

                <span class="{badge_class}">
                    {badge_text}
                </span>

            </div>

            <div class="recommendation-metrics">

                Inventory:
                <b>{row["Inventory Level"]:.0f}</b> units

                &nbsp; | &nbsp;

                Predicted Demand:
                <b>{row["Predicted Demand"]:.1f}</b> units

                &nbsp; | &nbsp;

                Reorder Point:
                <b>{row["Reorder Point"]:.0f}</b> units

                &nbsp; | &nbsp;

                Recommended Order:
                <b>{row["Recommended Order Qty"]:.0f}</b> units

            </div>

            <div class="recommendation-text">

                <b>Recommendation:</b>
                {row["Recommendation"]}

            </div>

        </div>
        """
    )


# ============================================================
# HISTORICAL PRIORITY REORDER TABLE
# ============================================================

st.html(
    """
    <div class="section-heading">
        🚨 Historical Priority Reorder Requirements
    </div>
    """
)


top_reorders = (
    filtered_df[
        filtered_df["Recommended Order Qty"] > 0
    ]
    .sort_values(
        "Recommended Order Qty",
        ascending=False
    )
    .head(20)
)


display_columns = [
    "Date",
    "Store ID",
    "Product ID",
    "Category",
    "Inventory Level",
    "Predicted Demand",
    "Reorder Point",
    "Inventory Coverage Days",
    "Stockout Risk",
    "Recommended Order Qty",
    "Recommendation"
]


display_table = top_reorders[
    display_columns
].copy()


display_table["Date"] = (
    display_table["Date"]
    .dt.strftime("%Y-%m-%d")
)


for col in [
    "Inventory Coverage Days",
    "Predicted Demand"
]:

    display_table[col] = (
        display_table[col]
        .round(1)
    )


st.dataframe(
    display_table,
    use_container_width=True,
    hide_index=True,
    height=500
)


# ============================================================
# PRODUCT INTELLIGENCE
# ============================================================

st.html(
    """
    <div class="section-heading">
        🔍 Product Intelligence
    </div>
    """
)


product_summary = (
    filtered_df
    .groupby("Product ID")
    .agg(
        Average_Inventory=(
            "Inventory Level",
            "mean"
        ),
        Average_Demand=(
            "Predicted Demand",
            "mean"
        ),
        Average_Coverage=(
            "Inventory Coverage Days",
            "mean"
        ),
        Recommended_Order=(
            "Recommended Order Qty",
            "sum"
        )
    )
    .reset_index()
)


product_summary = product_summary.rename(
    columns={
        "Product ID": "Product",
        "Average_Inventory": "Avg Inventory",
        "Average_Demand": "Avg Predicted Demand",
        "Average_Coverage": "Avg Coverage Days",
        "Recommended_Order": "Recommended Order Units"
    }
)


for col in [
    "Avg Inventory",
    "Avg Predicted Demand",
    "Avg Coverage Days",
    "Recommended Order Units"
]:

    product_summary[col] = (
        product_summary[col]
        .round(1)
    )


st.dataframe(
    product_summary.sort_values(
        "Recommended Order Units",
        ascending=False
    ),
    use_container_width=True,
    hide_index=True,
    height=450
)


# ============================================================
# FUTURE FORECAST
# ============================================================

st.markdown("---")


st.html(
    """
    <div class="section-heading">
        🔮 AI Forecast & Dynamic Inventory Intelligence
    </div>
    """
)


if future_df.empty:

    st.warning(
        "Future forecast dataset is not available."
    )

else:

    # --------------------------------------------------------
    # FORECAST BANNER
    # --------------------------------------------------------

    forecast_start = future_df["Date"].min()
    forecast_end = future_df["Date"].max()

    unique_skus = (
        future_df[
            ["Store ID", "Product ID"]
        ]
        .drop_duplicates()
        .shape[0]
    )

    st.html(
        f"""
        <div class="forecast-banner">

            <div class="forecast-title">
                🔮 7-Day AI Inventory Forecast
            </div>

            <div class="forecast-text">
                XGBoost recursive demand forecasting combined
                with dynamic inventory simulation and
                a 3-day replenishment lead time.
            </div>

            <div class="forecast-meta">

                📅 Forecast Period:
                {forecast_start.strftime("%Y-%m-%d")}
                →
                {forecast_end.strftime("%Y-%m-%d")}

                &nbsp;&nbsp; | &nbsp;&nbsp;

                📦 SKUs:
                {unique_skus}

                &nbsp;&nbsp; | &nbsp;&nbsp;

                📊 Forecast Records:
                {len(future_df):,}

            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # FUTURE FILTERS
    # --------------------------------------------------------

    forecast_stores = sorted(
        future_df["Store ID"]
        .dropna()
        .unique()
        .tolist()
    )

    forecast_products = sorted(
        future_df["Product ID"]
        .dropna()
        .unique()
        .tolist()
    )


    fc1, fc2 = st.columns(2)


    with fc1:

        forecast_store = st.selectbox(
            "🏬 Forecast Store",
            ["All Stores"] + forecast_stores
        )


    with fc2:

        forecast_product = st.selectbox(
            "📦 Forecast Product",
            ["All Products"] + forecast_products
        )


    forecast_view = future_df.copy()


    if forecast_store != "All Stores":

        forecast_view = forecast_view[
            forecast_view["Store ID"]
            == forecast_store
        ]


    if forecast_product != "All Products":

        forecast_view = forecast_view[
            forecast_view["Product ID"]
            == forecast_product
        ]


    if forecast_view.empty:

        st.warning(
            "No future forecast records match the selection."
        )

    else:

        # ----------------------------------------------------
        # FUTURE KPIs
        # ----------------------------------------------------

        future_total_demand = (
            forecast_view[
                "Predicted Demand"
            ].sum()
        )

        future_high_risk = (
            forecast_view[
                "Stockout Risk"
            ].eq("HIGH").sum()
        )

        future_orders = (
            forecast_view[
                "Recommended Order Qty"
            ].sum()
        )

        future_stockout = (
            forecast_view[
                "Stockout Quantity"
            ].sum()
        )


        fk1, fk2, fk3, fk4 = st.columns(4)


        with fk1:

            st.html(
                f"""
                <div class="kpi-card">

                    <div class="kpi-icon">📈</div>

                    <div class="kpi-title">
                        7-Day Predicted Demand
                    </div>

                    <div class="kpi-value">
                        {future_total_demand:,.0f}
                    </div>

                    <div class="kpi-subtitle">
                        Forecast units
                    </div>

                </div>
                """
            )


        with fk2:

            st.html(
                f"""
                <div class="kpi-card">

                    <div class="kpi-icon">🔴</div>

                    <div class="kpi-title">
                        High Stockout Risk
                    </div>

                    <div class="kpi-value">
                        {future_high_risk:,}
                    </div>

                    <div class="kpi-subtitle">
                        Forecast records
                    </div>

                </div>
                """
            )


        with fk3:

            st.html(
                f"""
                <div class="kpi-card">

                    <div class="kpi-icon">🚚</div>

                    <div class="kpi-title">
                        Recommended Replenishment
                    </div>

                    <div class="kpi-value">
                        {future_orders:,.0f}
                    </div>

                    <div class="kpi-subtitle">
                        Simulation quantity
                    </div>

                </div>
                """
            )


        with fk4:

            st.html(
                f"""
                <div class="kpi-card">

                    <div class="kpi-icon">⚠️</div>

                    <div class="kpi-title">
                        Stockout Exposure
                    </div>

                    <div class="kpi-value">
                        {future_stockout:,.0f}
                    </div>

                    <div class="kpi-subtitle">
                        Projected shortage units
                    </div>

                </div>
                """
            )


        # ----------------------------------------------------
        # FORECAST DEMAND
        # ----------------------------------------------------

        st.html(
            """
            <div class="section-heading">
                📈 7-Day AI Demand Forecast
            </div>
            """
        )


        forecast_daily = (
            forecast_view
            .groupby("Date")
            .agg(
                Predicted_Demand=(
                    "Predicted Demand",
                    "sum"
                )
            )
            .reset_index()
        )


        fig_future_demand = px.line(
            forecast_daily,
            x="Date",
            y="Predicted_Demand",
            markers=True,
            title="Forecasted Demand by Day",
            template="plotly_white"
        )


        fig_future_demand.update_layout(
            height=430,
            xaxis_title="Forecast Date",
            yaxis_title="Predicted Units"
        )


        st.plotly_chart(
            fig_future_demand,
            use_container_width=True
        )


        # ----------------------------------------------------
        # INVENTORY TRAJECTORY
        # ----------------------------------------------------

        st.html(
            """
            <div class="section-heading">
                📦 Dynamic Inventory Projection
            </div>
            """
        )


        if (
            forecast_store != "All Stores"
            and forecast_product != "All Products"
        ):

            trajectory = forecast_view.sort_values(
                "Date"
            )

            fig_inventory = px.line(
                trajectory,
                x="Date",
                y=[
                    "Opening Inventory",
                    "Ending Inventory",
                    "Reorder Point"
                ],
                markers=True,
                title=(
                    f"Inventory Trajectory — "
                    f"{forecast_store} / "
                    f"{forecast_product}"
                ),
                template="plotly_white"
            )

            fig_inventory.update_layout(
                height=450,
                xaxis_title="Date",
                yaxis_title="Units"
            )

            st.plotly_chart(
                fig_inventory,
                use_container_width=True
            )

        else:

            inventory_daily = (
                forecast_view
                .groupby("Date")
                .agg(
                    Opening_Inventory=(
                        "Opening Inventory",
                        "sum"
                    ),
                    Ending_Inventory=(
                        "Ending Inventory",
                        "sum"
                    ),
                    Predicted_Demand=(
                        "Predicted Demand",
                        "sum"
                    )
                )
                .reset_index()
            )

            fig_inventory = px.line(
                inventory_daily,
                x="Date",
                y=[
                    "Opening_Inventory",
                    "Ending_Inventory",
                    "Predicted_Demand"
                ],
                markers=True,
                title="Forecast Inventory Position",
                template="plotly_white"
            )

            fig_inventory.update_layout(
                height=450,
                xaxis_title="Date",
                yaxis_title="Units"
            )

            st.plotly_chart(
                fig_inventory,
                use_container_width=True
            )


        # ----------------------------------------------------
        # FUTURE RISK
        # ----------------------------------------------------

        risk_fc1, risk_fc2 = st.columns(2)


        with risk_fc1:

            future_risk = (
                forecast_view[
                    "Stockout Risk"
                ]
                .value_counts()
                .reset_index()
            )

            future_risk.columns = [
                "Risk",
                "Count"
            ]


            fig_future_risk = px.pie(
                future_risk,
                names="Risk",
                values="Count",
                hole=0.50,
                title="7-Day Stockout Risk",
                template="plotly_white"
            )


            fig_future_risk.update_layout(
                height=400
            )


            st.plotly_chart(
                fig_future_risk,
                use_container_width=True
            )


        with risk_fc2:

            priority_summary = (
                forecast_view[
                    "Reorder Priority"
                ]
                .value_counts()
                .reset_index()
            )

            priority_summary.columns = [
                "Priority",
                "Count"
            ]


            fig_priority = px.bar(
                priority_summary,
                x="Priority",
                y="Count",
                text="Count",
                title="Reorder Priority",
                template="plotly_white"
            )


            fig_priority.update_traces(
                textposition="outside"
            )


            fig_priority.update_layout(
                height=400
            )


            st.plotly_chart(
                fig_priority,
                use_container_width=True
            )


        # ----------------------------------------------------
        # FUTURE ALERTS
        # ----------------------------------------------------

        st.html(
            """
            <div class="section-heading">
                🚨 Future Replenishment Alerts
            </div>
            """
        )


        urgent = (
            forecast_view[
                forecast_view[
                    "Reorder Priority"
                ] == "URGENT"
            ]
            .sort_values(
                "Recommended Order Qty",
                ascending=False
            )
            .head(15)
        )


        if urgent.empty:

            st.success(
                "No urgent replenishment alerts "
                "for the selected forecast."
            )

        else:

            for _, row in urgent.iterrows():

                arrival = row.get(
                    "Order Arrival Date",
                    np.nan
                )

                if pd.notna(arrival):

                    try:

                        arrival_text = pd.to_datetime(
                            arrival
                        ).strftime(
                            "%Y-%m-%d"
                        )

                    except Exception:

                        arrival_text = str(arrival)

                else:

                    arrival_text = "N/A"


                st.html(
                    f"""
                    <div class="recommendation-card">

                        <div class="recommendation-title">

                            🔴
                            {row["Store ID"]}
                            |
                            {row["Product ID"]}

                            &nbsp;&nbsp;

                            <span class="risk-high">
                                URGENT
                            </span>

                        </div>

                        <div class="recommendation-metrics">

                            Date:
                            <b>
                                {row["Date"].strftime("%Y-%m-%d")}
                            </b>

                            &nbsp; | &nbsp;

                            Predicted Demand:
                            <b>
                                {row["Predicted Demand"]:.1f}
                            </b>

                            units

                            &nbsp; | &nbsp;

                            Ending Inventory:
                            <b>
                                {row["Ending Inventory"]:.1f}
                            </b>

                            &nbsp; | &nbsp;

                            Recommended Order:
                            <b>
                                {row["Recommended Order Qty"]:.0f}
                            </b>

                            units

                        </div>

                        <div class="recommendation-text">

                            <b>Action:</b>
                            {row["Recommendation"]}

                            &nbsp; | &nbsp;

                            Order Arrival:
                            <b>
                                {arrival_text}
                            </b>

                        </div>

                    </div>
                    """
                )


        # ----------------------------------------------------
        # FINAL FORECAST TABLE
        # ----------------------------------------------------

        st.html(
            """
            <div class="section-heading">
                📋 Forecast Inventory Intelligence
            </div>
            """
        )


        base_columns = [
            "Date",
            "Store ID",
            "Product ID",
            "Predicted Demand",
            "Opening Inventory",
            "Ending Inventory",
            "Stockout Risk",
            "Recommended Order Qty",
            "Order Arrival Date",
            "Reorder Priority"
        ]


        available_columns = [
            col for col in base_columns
            if col in forecast_view.columns
        ]


        forecast_table = forecast_view[
            available_columns
        ].copy()


        forecast_table["Date"] = (
            forecast_table["Date"]
            .dt.strftime("%Y-%m-%d")
        )


        if "Order Arrival Date" in forecast_table.columns:

            forecast_table[
                "Order Arrival Date"
            ] = (
                pd.to_datetime(
                    forecast_table[
                        "Order Arrival Date"
                    ],
                    errors="coerce"
                )
                .dt.strftime("%Y-%m-%d")
            )


        numeric_display = [
            "Predicted Demand",
            "Opening Inventory",
            "Ending Inventory",
            "Recommended Order Qty"
        ]


        for col in numeric_display:

            if col in forecast_table.columns:

                forecast_table[col] = (
                    forecast_table[col]
                    .round(1)
                )


        st.dataframe(
            forecast_table,
            use_container_width=True,
            hide_index=True,
            height=550
        )


        # ----------------------------------------------------
        # EXPORT
        # ----------------------------------------------------

        st.html(
            """
            <div class="section-heading">
                📥 Export Future Intelligence
            </div>
            """
        )


        future_export = forecast_view.copy()

        future_export["Date"] = (
            future_export["Date"]
            .dt.strftime("%Y-%m-%d")
        )


        future_csv = future_export.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(
            label="📥 Download 7-Day Forecast & Inventory Report",
            data=future_csv,
            file_name=(
                "foresight_7_day_forecast_inventory.csv"
            ),
            mime="text/csv",
            use_container_width=True
        )


# ============================================================
# MODEL INFORMATION
# ============================================================

st.html(
    """
    <div class="section-heading">
        ℹ️ FORESIGHT Model Information
    </div>
    """
)


info1, info2, info3 = st.columns(3)


with info1:

    st.html(
        """
        <div class="info-card">

            <div class="info-card-title">
                🎯 Demand Prediction
            </div>

            <div class="info-card-text">

                <b>XGBoost Regression Model</b>

                <br><br>

                Uses historical demand, lag features,
                rolling statistics, calendar variables
                and store/product information to predict
                future demand.

            </div>

        </div>
        """
    )


with info2:

    st.html(
        """
        <div class="info-card">

            <div class="info-card-title">
                📦 Inventory Intelligence
            </div>

            <div class="info-card-text">

                Safety Stock + Reorder Point +
                Inventory Coverage analysis.

                <br><br>

                Dynamic simulation uses a
                3-day replenishment lead time.

            </div>

        </div>
        """
    )


with info3:

    st.html(
        """
        <div class="info-card">

            <div class="info-card-title">
                ⚠️ Risk Detection
            </div>

            <div class="info-card-text">

                Stockout risk classification with
                actionable replenishment recommendations.

                <br><br>

                Future inventory exposure and
                recommended order quantities are calculated.

            </div>

        </div>
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer-box">

        <div class="footer-title">
            📦 FORESIGHT
        </div>

        <div class="footer-text">
            AI-Powered Demand & Inventory Intelligence Platform
        </div>

        <div class="footer-text">
            XGBoost • Python • Pandas • NumPy • Plotly • Streamlit
        </div>

        <div class="footer-text">
            Demand Forecasting • Inventory Optimization • Risk Intelligence
        </div>

    </div>
    """
)