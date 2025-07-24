import streamlit as st
from extract_text import extract_resumes_from_folder
from rank_resumes import ResumeRanker

# Title
st.title("AI-Powered Resume Screening Tool")

# Upload job description
st.subheader("Upload Job Description")
job_description = st.text_area("Paste the job description here:")

# Upload resumes
st.subheader("Upload Resumes")
uploaded_files = st.file_uploader("Upload multiple resumes (PDF)", type="pdf", accept_multiple_files=True)

if st.button("Rank Resumes"):
    if not job_description or not uploaded_files:
        st.warning("Please upload resumes and provide a job description.")
    else:
        # Save resumes temporarily
        temp_folder = "temp_resumes"
        import os
        os.makedirs(temp_folder, exist_ok=True)
        for file in uploaded_files:
            with open(os.path.join(temp_folder, file.name), "wb") as f:
                f.write(file.read())

        st.info("Extracting text and ranking resumes...")

        # Extract text and rank
        resumes = extract_resumes_from_folder(temp_folder)
        ranker = ResumeRanker()
        rankings = ranker.rank_resumes(resumes, job_description)

        # Display ranking
        st.subheader("Resume Ranking:")
        for i, (name, score) in enumerate(rankings, start=1):
            st.write(f"{i}. {name} - **Score:** {score:.4f}")
