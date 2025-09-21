import streamlit as st
import json, os
from utils.extract_text import extract_text

st.title("Admin - Upload Job Description")

job_title = st.text_input("Job Title")
job_id = st.text_input("Job ID (unique)")
uploaded_file = st.file_uploader("Upload JD (PDF/DOCX)", type=["pdf","docx"])
job_keywords = st.text_area("Enter mandatory keywords (comma separated)").split(",")

if st.button("Post Job"):
    if job_title and job_id and uploaded_file:
        job_text = extract_text(uploaded_file)
        jobs_file = "data/jobs.json"
        os.makedirs("data", exist_ok=True)

        if os.path.exists(jobs_file):
            with open(jobs_file, "r") as f:
                jobs = json.load(f)
        else:
            jobs = {}

        jobs[job_id] = {
            "title": job_title,
            "description": job_text,
            "keywords": [kw.strip() for kw in job_keywords]
        }

        with open(jobs_file, "w") as f:
            json.dump(jobs, f)
        st.success(f"Job '{job_title}' uploaded successfully!")
    else:
        st.warning("Fill all fields and upload JD file.")
