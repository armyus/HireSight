# HireSight – Automated Resume Relevance Checker

**HireSight** is an AI-powered web application designed to automate the evaluation of resumes for placement teams and job seekers. It provides fast, consistent, and actionable feedback by combining rule-based keyword checks with semantic analysis using embeddings.

---

## **Table of Contents**
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Workflow](#workflow)
- [Scoring Mechanism](#scoring-mechanism)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [License](#license)

---

## **Overview**
HireSight helps placement teams streamline resume evaluation while giving students insights to improve their resumes. The system:

- Automates assessment of resumes against job descriptions.
- Generates a Relevance Score (0–100) for each resume.
- Highlights missing skills, certifications, or projects.
- Provides a fit verdict: High, Medium, or Low suitability.
- Stores evaluations in a searchable dashboard for placement teams.

HireSight uses **Hard Match** (keywords, skills, education) and **Semantic Match** (embeddings + AI reasoning) to deliver fast and reliable results.

---

## **Problem Statement**
Manual resume evaluation is time-consuming and inconsistent. Placement teams receive multiple job postings weekly, each attracting hundreds of resumes. This leads to:

- Delays in shortlisting candidates.
- Inconsistent judgments due to subjective interpretation.
- High workload for placement staff.

HireSight automates this process, ensuring speed, consistency, and actionable feedback.

---

## **Features**
- **Admin Page:** Post job descriptions (PDF/DOCX) and define required skills.
- **Job Seeker Page:** Upload resume, select a job, and get Relevance Score, Verdict, and missing skills.
- **Hard Match:** Keyword and skill-based scoring.
- **Semantic Match:** Embedding-based similarity scoring.
- **Dashboard:** Stores job postings and evaluations for placement teams.

---

## **Tech Stack**
- **Backend:** Python  
- **Frontend:** Streamlit  
- **Resume Parsing:** PyPDF2, python-docx  
- **Text Processing:** spaCy, NLTK  
- **Semantic Analysis:** SentenceTransformers (embeddings), cosine similarity  
- **Storage:** JSON (jobs.json, evaluations.json)  
- **Optional:** SQLite/PostgreSQL for scalable deployments

---

## **Workflow**
1. **Job Upload:** Placement team uploads job description with required skills.  
2. **Resume Upload:** Job seekers upload their resumes.  
3. **Parsing & Extraction:** Extract text from PDFs/DOCX files.  
4. **Hard Match:** Compare keywords, skills, and education.  
5. **Semantic Match:** Compare embeddings of resume and job description.  
6. **Scoring & Verdict:** Generate final relevance score and suitability verdict.  
7. **Results Storage:** Store evaluations in JSON (or database) for dashboard access.

---

## **Scoring Mechanism**
HireSight calculates a **Relevance Score (0–100)** for each resume using a **hybrid approach**:

1. **Hard Match (Keyword / Skills Check):**  
   - Checks for mandatory skills, certifications, and education keywords.  
   - Each matched keyword increases the hard score proportionally.  

2. **Semantic Match (Embedding Similarity):**  
   - Uses embeddings from `SentenceTransformer` to measure semantic similarity between resume and job description.  
   - Cosine similarity is calculated for overall context and phrasing.

3. **Final Relevance Score:**  
   - Final Score = (Weight_Hard * Hard_Score) + (Weight_Semantic * Semantic_Score)
   - - Typically, `Weight_Hard = 0.4` and `Weight_Semantic = 0.6` (can be tuned).  
- The result is converted to a **percentage score (0–100)**.

4. **Verdict:**  
- **High:** Score ≥ 75%  
- **Medium:** 50% ≤ Score < 75%  
- **Low:** Score < 50%  

> This hybrid scoring ensures both **exact requirement matching** and **contextual understanding**, giving fair and actionable evaluations.  

---

## **Installation & Setup**
1. Clone the repository:
```bash
git clone https://github.com/yourusername/HireSight.git
cd HireSight
```
2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the app:
```bash
streamlit run app.py
```

---

## **Usage**
   - Admin: Navigate to the Admin page, upload job description, add required skills, and post the job.
   - Job Seeker: Navigate to Job Seeker page, select job, upload resume, and click “Check Relevance” to view score, verdict, and missing skills.
   - Overview: Provides a summary of the app, its features, and workflow.

## **License**
This project is for educational and competition purposes.
   
