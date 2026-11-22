
import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"

st.set_page_config(page_title="Extension Request Sorter", page_icon="🎓", layout="wide")

st.title("🎓 AI-Based Extension Request Sorter")
st.write("An AI-assisted system for analysing student extension requests.")

results_file = OUTPUT_DIR / "results.csv"
summary_file = OUTPUT_DIR / "summary.txt"
review_file = OUTPUT_DIR / "review_queue.csv"

if results_file.exists():
    df = pd.read_csv(results_file)

    st.subheader("Request Processing Dashboard")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Requests", len(df))

    if "recommendation" in df.columns:
        counts = df["recommendation"].value_counts()
        c2.metric("Within Policy", counts.get("within_policy", 0))
        c3.metric("Faculty Review", counts.get("needs_faculty_review", 0))

    st.subheader("Processed Requests")
    st.dataframe(df, use_container_width=True)

    if summary_file.exists():
        st.subheader("Processing Summary")
        st.text(summary_file.read_text(encoding="utf-8"))

    if review_file.exists():
        st.subheader("Requests Requiring Attention")
        st.dataframe(pd.read_csv(review_file), use_container_width=True)

    st.success("AI processing reports loaded successfully.")
else:
    st.warning("No reports found. Run the project first using python main.py.")

st.caption("AI recommendations are decision-support only. Final decisions remain with faculty.")
