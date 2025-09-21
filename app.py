import streamlit as st
from PyPDF2 import PdfReader
import docx
from sentence_transformers import SentenceTransformer, util

st.title("HireSight - Resume Relevance Checker")

# Step 1: Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

# Step 2: Enter job description
job_desc = st.text_area("Paste the Job Description here")

# Load embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def extract_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

if st.button("Check Relevance"):
    if uploaded_file and job_desc:
        resume_text = extract_text(uploaded_file)
        # Compute embeddings
        resume_emb = model.encode(resume_text, convert_to_tensor=True)
        job_emb = model.encode(job_desc, convert_to_tensor=True)
        # Cosine similarity
        score = util.cos_sim(resume_emb, job_emb).item()
        st.success(f"Relevance Score: {score*100:.2f}%")
    else:
        st.warning("Please upload a resume and enter a job description.")
