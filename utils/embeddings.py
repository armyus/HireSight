from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def semantic_score(resume_text, job_text):
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    job_emb = model.encode(job_text, convert_to_tensor=True)
    score = util.cos_sim(resume_emb, job_emb).item() * 100
    return score
