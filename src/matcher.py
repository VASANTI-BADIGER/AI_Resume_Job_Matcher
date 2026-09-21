from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(matching_skills, missing_skills):
    total_required_skills = len(matching_skills) + len(missing_skills)

    if total_required_skills > 0:
        score = (len(matching_skills) / total_required_skills) * 100
    else:
        score = 0

    return score


def calculate_text_similarity(resume, job_description):
    texts = [resume, job_description]

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])

    return similarity[0][0] * 100
