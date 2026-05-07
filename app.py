import streamlit as st
from data_loader import load_data, get_summary_stats
from charts import channel_performance_chart, spend_trend_chart, cpa_by_segment_chart, region_heatmap
from ai_analyst import ask_about_data

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Healthcare Marketing Analytics",
    page_icon="🏥",
    layout="wide"
)

# ── Load data (cached so it only runs once) ───────────────────────────────────
@st.cache_data
def get_data():
    return load_data("data/health_marketing.csv")

df = get_data()
stats = get_summary_stats(df)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🏥 Healthcare Marketing Analytics")
st.caption(f"Data range: {stats['date_range']} · Built with Python + Gemini AI")
st.divider()

# ── Metric cards ──────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Spend", f"${stats['total_spend']:,}")
with col2:
    st.metric("Total Reach", f"{stats['total_reach']:,}")
with col3:
    st.metric("Conversions", f"{stats['total_conversions']:,}")
with col4:
    st.metric("Avg CPA", f"${stats['avg_cpa']}")

st.divider()

# ── Sidebar filters ───────────────────────────────────────────────────────────
st.sidebar.header("Filters")

channels = st.sidebar.multiselect(
    "Channels",
    options=df['channel'].unique(),
    default=df['channel'].unique()
)

regions = st.sidebar.multiselect(
    "Regions",
    options=df['region'].unique(),
    default=df['region'].unique()
)

# Apply filters
filtered_df = df[
    (df['channel'].isin(channels)) &
    (df['region'].isin(regions))
]

# ── Charts grid ───────────────────────────────────────────────────────────────
left, right = st.columns(2)

with left:
    st.plotly_chart(channel_performance_chart(filtered_df), use_container_width=True)

with right:
    st.plotly_chart(spend_trend_chart(filtered_df), use_container_width=True)

left2, right2 = st.columns(2)

with left2:
    st.plotly_chart(cpa_by_segment_chart(filtered_df), use_container_width=True)

with right2:
    st.plotly_chart(region_heatmap(filtered_df), use_container_width=True)

st.divider()

# ── AI Analyst panel ──────────────────────────────────────────────────────────
st.subheader("🤖 Ask the AI Analyst")
st.caption("Ask any question about the data in plain English.")

question = st.text_input(
    "",
    placeholder="e.g. Which channel had the best ROI last quarter?"
)

if question:
    with st.spinner("Analysing..."):
        answer = ask_about_data(question, get_summary_stats(filtered_df))
    st.info(answer)

# ── Raw data expander ─────────────────────────────────────────────────────────
with st.expander("View raw data"):
    st.dataframe(filtered_df, use_container_width=True)