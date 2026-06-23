import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

pio.templates.default = "plotly_dark"
# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="STT NMDC-02 Dashboard",
    page_icon="🏗️",
    layout="wide"
)
st.markdown("""
<style>
[data-testid="metric-container"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD EXCEL
# =====================================================

@st.cache_data
def load_excel(file):
    return pd.read_excel(file, sheet_name=None)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🏗️ NMDC-02 Dashboard")

uploaded_file = st.sidebar.file_uploader(
    "Upload Weekly Report",
    type=["xlsx"]
)

if uploaded_file is None:
    st.warning("Please upload project_data.xlsx")
    st.stop()

data = load_excel(uploaded_file)
page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Summary",
        "Design Tracker",
        "Work Progress",
        "Procurement",
        "Manpower",
        "Milestones",
        "Risk Register",
        
    ]
)

# =====================================================
# TITLE
# =====================================================

st.title("🏗️ STT NMDC-02 Data Center Project Dashboard")
st.markdown("---")

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

if page == "Executive Summary":

    st.header("📊 Executive Summary")
    col1, col2, col3 = st.columns(3)

    with col1:
     st.success("🟢 Design Progress On Track")

    with col2:
     st.warning("🟡 Procurement Needs Attention")

    with col3:
     st.error("🔴 Critical Risks Open")
 
    kpi = data["Executive_KPI"]

    planned = int(
        kpi.loc[
            kpi["KPI"] == "Planned Progress",
            "Value"
        ].iloc[0]
    )

    actual = int(
        kpi.loc[
            kpi["KPI"] == "Actual Progress",
            "Value"
        ].iloc[0]
    )

    design = int(
        kpi.loc[
            kpi["KPI"] == "Design Progress",
            "Value"
        ].iloc[0]
    )

    procurement = int(
        kpi.loc[
            kpi["KPI"] == "Procurement Progress",
            "Value"
        ].iloc[0]
    )

    execution = int(
        kpi.loc[
            kpi["KPI"] == "Execution Progress",
            "Value"
        ].iloc[0]
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Planned", f"{planned}%")
    c2.metric("Actual", f"{actual}%")
    c3.metric("Design", f"{design}%")
    c4.metric("Procurement", f"{procurement}%")
    c5.metric("Execution", f"{execution}%")

    st.markdown("---")

    scurve = data["SCurve"]

    fig = px.line(
        scurve,
        x="Week",
        y=["Baseline", "Revised", "Actual"],
        markers=True,
        title="Project S-Curve Progress"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
# =====================================================
# DESIGN TRACKER
# =====================================================

elif page == "Design Tracker":

    st.header("📐 Design Tracker")

    design = data["Design_Tracker"]

    chart_df = design.iloc[1:8].copy()

    total_drawings = int(
        design["Total Nos"].fillna(0).max()
    )

    approved = int(
        design["CODE F"].fillna(0).sum()
    )

    pending = int(
        design["Balance for submission"].fillna(0).sum()
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Drawings", total_drawings)
    c2.metric("Approved", approved)
    c3.metric("Pending", pending)

    st.markdown("---")

    fig = px.bar(
    chart_df,
    x="Description",
    y="Total Nos",
    text="Total Nos",
    color="Description",
    title="Design Deliverables by Discipline",
    color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig.update_layout(
    template="plotly_dark",
    height=500,
    showlegend=False,
    title_x=0.35
)

    fig.update_traces(
    textposition="outside"
)

    st.plotly_chart(
    fig,
    use_container_width=True
)
    
# =====================================================
# WORK PROGRESS
# =====================================================

elif page == "Work Progress":

    st.header("🏗️ Work Progress Dashboard")

    work_df = data["Construction"]

    st.markdown("### Construction Progress Overview")

    st.dataframe(
        work_df,
        use_container_width=True
    )

    numeric_cols = work_df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_cols) > 0:

        x_col = work_df.columns[0]

        y_col = numeric_cols[0]

        fig = px.bar(
            work_df,
            x=x_col,
            y=y_col,
            color=y_col,
            text=y_col,
            title="Construction Progress"
        )

        fig.update_layout(
            template="plotly_dark",
            height=550
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =====================================================
# PROCUREMENT
# =====================================================
elif page == "Procurement":

    st.header("📦 Procurement Dashboard")

    procurement = data["Procurement"]

    delivered = len(
        procurement[
            procurement["Status"] == "Delivered"
        ]
    )

    delayed = len(
        procurement[
            procurement["Status"] == "Delayed"
        ]
    )

    avg_completion = round(
        procurement["Completion %"].mean(),
        1
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Delivered", delivered)
    c2.metric("Delayed", delayed)
    c3.metric("Average Completion", f"{avg_completion}%")

    st.markdown("---")

    fig = px.bar(
    procurement,
    x="Package",
    y="Completion %",
    color="Status",
    text="Completion %",
    title="Procurement Package Status",
    color_discrete_sequence=px.colors.qualitative.Set1
)

    fig.update_layout(
    template="plotly_dark",
    height=550,
    title_x=0.35
)

    st.plotly_chart(
    fig,
    use_container_width=True
)
# =====================================================
# MANPOWER
# =====================================================

elif page == "Manpower":

    st.header("👷 Manpower Dashboard")

    manpower = data["Manpower"]

    latest = manpower.iloc[-1]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Electrical",
        int(latest["Electrical"])
    )

    c2.metric(
        "Mechanical",
        int(latest["Mechanical"])
    )

    c3.metric(
        "Subcontractors",
        int(latest["Subcontractors"])
    )

    c4.metric(
        "Total Workforce",
        int(latest["Total"])
    )

    st.markdown("---")

    trend = manpower.melt(
        id_vars=["Date"],
        value_vars=[
            "Mechanical",
            "Electrical",
            "Housekeeping",
            "Common",
            "Subcontractors",
            "Yard Activities"
        ],
        var_name="Discipline",
        value_name="Count"
    )

    fig = px.area(
    trend,
    x="Date",
    y="Count",
    color="Discipline",
    title="Manpower Deployment Trend",
    color_discrete_sequence=px.colors.qualitative.Vivid
)

    fig.update_layout(
    template="plotly_dark",
    height=550,
    title_x=0.35
)

    st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# MILESTONES
# =====================================================

elif page == "Milestones":

    st.header("🎯 Project Milestones Dashboard")

    milestone_df = data["Milestones"].copy()

    # Convert dates
    milestone_df["Baseline Date"] = pd.to_datetime(
        milestone_df["Baseline Date"]
    )

    milestone_df["Forecast Date"] = pd.to_datetime(
        milestone_df["Forecast Date"]
    )

    # Delay Calculation
    milestone_df["Delay Days"] = (
        milestone_df["Forecast Date"]
        - milestone_df["Baseline Date"]
    ).dt.days

    # KPI CARDS

    completed = len(
        milestone_df[
            milestone_df["Status"] == "Completed"
        ]
    )

    delayed = len(
        milestone_df[
            milestone_df["Status"] == "Delayed"
        ]
    )

    pending = len(
        milestone_df[
            milestone_df["Status"] == "Pending"
        ]
    )

    avg_delay = round(
        milestone_df["Delay Days"].mean(),
        1
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("✅ Completed", completed)
    c2.metric("🔴 Delayed", delayed)
    c3.metric("🟡 Pending", pending)
    c4.metric("📅 Avg Delay", f"{avg_delay} Days")

    st.markdown("---")

    # DELAY CHART

    fig = px.bar(
        milestone_df,
        x="Milestone",
        y="Delay Days",
        color="Status",
        text="Delay Days",
        title="Milestone Delay Analysis",
        color_discrete_map={
            "Completed": "#22c55e",
            "Pending": "#f59e0b",
            "Delayed": "#ef4444"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        height=550,
        title_x=0.25,
        xaxis_title="Milestone",
        yaxis_title="Delay Days"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # DELAYED MILESTONES

    delayed_df = milestone_df[
        milestone_df["Status"] == "Delayed"
    ]

    if len(delayed_df) > 0:

        st.subheader("🔴 Delayed Milestones")

        st.dataframe(
            delayed_df[
                [
                    "Milestone",
                    "Baseline Date",
                    "Forecast Date",
                    "Delay Days"
                ]
            ],
            use_container_width=True
        )

    st.markdown("---")

    # FULL TABLE

    with st.expander("📋 View Complete Milestone Register"):

        st.dataframe(
            milestone_df,
            use_container_width=True
        )



# =====================================================
# RISK REGISTER
# =====================================================


elif page == "Risk Register":

    st.header("⚠️ Project Risk Dashboard")

    risk = data["Risk_Register"].copy()

    # Risk Score
    risk["Risk Score"] = (
        risk["Probability"] *
        risk["Impact"]
    )

    # KPI Cards

    total_risks = len(risk)

    high_risks = len(
        risk[
            risk["Risk Score"] >= 15
        ]
    )

    medium_risks = len(
        risk[
            (risk["Risk Score"] >= 8)
            &
            (risk["Risk Score"] < 15)
        ]
    )

    low_risks = len(
        risk[
            risk["Risk Score"] < 8
        ]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Risks", total_risks)
    c2.metric("🔴 High Risks", high_risks)
    c3.metric("🟡 Medium Risks", medium_risks)
    c4.metric("🟢 Low Risks", low_risks)

    st.markdown("---")

    # Risk Heat Map

    fig = px.scatter(
        risk,
        x="Probability",
        y="Impact",
        size="Risk Score",
        color="Risk Score",
        hover_name="Risk",
        title="Risk Heat Map",
        color_continuous_scale="RdYlGn_r"
    )

    fig.update_layout(
        template="plotly_dark",
        height=600,
        title_x=0.35
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # Top Risks

    top_risks = risk.sort_values(
        "Risk Score",
        ascending=False
    ).head(5)

    st.subheader("🔴 Top 5 Critical Risks")

    st.dataframe(
        top_risks,
        use_container_width=True
    )

    st.markdown("---")

    with st.expander("📋 Complete Risk Register"):

        st.dataframe(
            risk,
            use_container_width=True
        )

        # =====================================================
