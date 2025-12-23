import streamlit as st
import os
import pandas as pd
from resume_ranker import rank_resumes

UPLOAD_FOLDER = "uploaded_resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="AI Resume Ranker", layout="wide")

st.title("🤖 AI-Powered Resume Ranker")
st.write("Upload resumes and paste job description to rank candidates")

st.divider()

job_description = st.text_area(
    "📌 Job Description",
    height=200,
    placeholder="Enter required skills, experience..."
)

uploaded_files = st.file_uploader(
    "📂 Upload Resume PDFs",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        with open(os.path.join(UPLOAD_FOLDER, file.name), "wb") as f:
            f.write(file.getbuffer())

if st.button("🚀 Rank Resumes"):
    if not job_description:
        st.warning("Please enter job description")
    elif not uploaded_files:
        st.warning("Please upload resumes")
    else:
        with st.spinner("Analyzing resumes..."):
            ranked = rank_resumes(UPLOAD_FOLDER, job_description)

        df = pd.DataFrame(ranked, columns=["Resume", "Score"])

        total_resumes = len(df)

# Rank starts from 1 (already sorted best → worst)
        df["Rank"] = range(1, total_resumes + 1)

# Individual percentage per resume based on rank
        df["Match %"] = (df["Rank"] / total_resumes * 100).round(2)

# Keep only required columns
        df = df[["Resume", "Match %"]]



        st.success("Ranking Completed")
        st.dataframe(df, use_container_width=True)
        st.bar_chart(df.set_index("Resume")["Match %"])

