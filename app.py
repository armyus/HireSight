import streamlit as st

# Page configuration
st.set_page_config(page_title="HireSight Overview", layout="centered")

# Title
st.markdown("<h1 style='text-align:center; color:#1976D2;'>HireSight</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#000000;'>Automated Resume Relevance Checker</h4>", unsafe_allow_html=True)
st.markdown("---")

# Overview content in a card
st.markdown("""
<div style='background-color:#ffffff; padding:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);'>
    <h3 style='color:#1976D2;'>Overview</h3>
    <p>
        HireSight is an AI-powered web application designed to help placement teams and job seekers by automating resume evaluation.
        It allows:
    </p>
    <ul>
        <li>Automatic assessment of resumes against uploaded job descriptions.</li>
        <li>Generation of a Relevance Score (0–100) for each resume.</li>
        <li>Highlighting missing skills, certifications, or projects.</li>
        <li>Providing a fit verdict: High, Medium, or Low suitability.</li>
        <li>Storing evaluations in a searchable dashboard for placement teams.</li>
    </ul>
    <p>
        HireSight uses a combination of <b>Hard Match</b> (keyword/skill checks) and <b>Semantic Match</b> (embeddings + AI reasoning) to ensure speed, consistency, and actionable feedback.
    </p>
</div>
""", unsafe_allow_html=True)

# Navigation hint
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#1976D2;'>
    Go to the Admin page to post job descriptions or to the Job Seeker page to evaluate your resume.
</div>
""", unsafe_allow_html=True)
