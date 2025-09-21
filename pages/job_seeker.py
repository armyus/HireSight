import streamlit as st
import json, os
from utils.extract_text import extract_text
from utils.scoring import hard_match_score, final_score
from utils.embeddings import semantic_score

st.title("Job Seeker - Resume Relevance Check")

jobs_file = "data/jobs.json"
if not os.path.exists(jobs_file):
    st.warning("No jobs posted yet.")
    st.stop()

with open(jobs_file, "r") as f:
    jobs = json.load(f)

job_id = st.selectbox("Select Job", list(jobs.keys()), format_func=lambda x: jobs[x]['title'])
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf","docx"])

if st.button("Check Relevance"):
    if uploaded_file and job_id:
        resume_text = extract_text(uploaded_file)
        job = jobs[job_id]

        # Hard + Soft match
        hard_score, missing = hard_match_score(resume_text, job['keywords'])
        soft_score = semantic_score(resume_text, job['description'])
        score, verdict = final_score(hard_score, soft_score)

        st.success(f"Relevance Score: {score:.2f}%")
        st.info(f"Verdict: {verdict}")
        if missing:
            st.warning(f"Missing Keywords/Skills: {', '.join(missing)}")

        # Store evaluation
        evaluations_file = "data/evaluations.json"
        if os.path.exists(evaluations_file):
            with open(evaluations_file, "r") as f:
                evaluations = json.load(f)
        else:
            evaluations = {}

        evaluations_key = f"{job_id}_{uploaded_file.name}"
        evaluations[evaluations_key] = {
            "job_title": job["title"],
            "resume_file": uploaded_file.name,
            "score": score,
            "verdict": verdict,
            "missing_keywords": missing
        }

        with open(evaluations_file, "w") as f:
            json.dump(evaluations, f)

    else:
        st.warning("Upload resume and select a job.")
