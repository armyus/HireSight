from fuzzywuzzy import fuzz

# Hard match: keywords
def hard_match_score(resume_text, job_keywords):
    matches = 0
    missing = []
    for kw in job_keywords:
        if fuzz.partial_ratio(kw.lower(), resume_text.lower()) > 70:
            matches += 1
        else:
            missing.append(kw)
    score = (matches / len(job_keywords)) * 100 if job_keywords else 0
    return score, missing

# Weighted final score
def final_score(hard_score, soft_score, hard_weight=0.6, soft_weight=0.4):
    score = hard_score*hard_weight + soft_score*soft_weight
    if score >= 75:
        verdict = "High"
    elif score >= 50:
        verdict = "Medium"
    else:
        verdict = "Low"
    return score, verdict
