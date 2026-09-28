
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(matching_skills, missing_skills):
    """
    Calculate the percentage of required skills found
    in the resume.
    """
    total_required_skills = (
        len(matching_skills) + len(missing_skills)
    )

    if total_required_skills == 0:
        return 0.0

    score = (
        len(matching_skills) / total_required_skills
    ) * 100

    return round(score, 2)


def calculate_text_similarity(resume, job_description):
    """
    Compare resume and job-description text using TF-IDF
    and cosine similarity.
    """
    if not resume or not resume.strip():
        return 0.0

    if not job_description or not job_description.strip():
        return 0.0

    texts = [
        resume.strip(),
        job_description.strip()
    ]

    try:
        vectorizer = TfidfVectorizer()
        matrix = vectorizer.fit_transform(texts)

        similarity = cosine_similarity(
            matrix[0:1],
            matrix[1:2]
        )

        score = similarity[0][0] * 100

        return round(float(score), 2)

    except ValueError:
        # For example, both texts may contain only
        # punctuation or words that cannot be tokenized.
        return 0.0


def calculate_combined_score(
    skill_match_score,
    text_similarity_score
):
    """
    Combine the skill score and text similarity score.
    Skills have 60% weight; text similarity has 40%.
    """
    combined_score = (
        skill_match_score * 0.60
        + text_similarity_score * 0.40
    )

    return round(combined_score, 2)
