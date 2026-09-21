import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.resume_parser import extract_text_from_pdf
from src.text_preprocessing import clean_text


def skill_exists(text, skill):
    pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
    return re.search(pattern, text) is not None


def find_matching_skills(resume, job_description, skills):
    matching_skills = []

    for skill in skills:
        if skill_exists(resume, skill) and skill_exists(job_description, skill):
            matching_skills.append(skill)

    return matching_skills


def find_missing_skills(resume, job_description, skills):
    missing_skills = []

    for skill in skills:
        if skill_exists(job_description, skill) and not skill_exists(resume, skill):
            missing_skills.append(skill)

    return missing_skills


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


# Get resume PDF
pdf_path = input("Enter resume PDF path: ")

resume = extract_text_from_pdf(pdf_path)


# Get job description
job_description = input("\nEnter the job description: ")


# Clean resume and job description
resume = clean_text(resume)
job_description = clean_text(job_description)


# Skills database
skills = [
    "python",
    "sql",
    "java",
    "c",
    "c++",
    "javascript",
    "html",
    "css",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "aws",
    "azure",
    "google cloud",
    "docker",
    "git",
    "linux",
    "mongodb",
    "mysql",
    "postgresql",
    "flask",
    "django",
    "streamlit"
]


# Find matching skills
matching_skills = find_matching_skills(
    resume,
    job_description,
    skills
)


# Find missing skills
missing_skills = find_missing_skills(
    resume,
    job_description,
    skills
)


# Calculate skill match score
skill_match_score = calculate_match_score(
    matching_skills,
    missing_skills
)


# Calculate AI text similarity
text_similarity_score = calculate_text_similarity(
    resume,
    job_description
)


# Calculate combined score
combined_match_score = (
    skill_match_score * 0.60
    + text_similarity_score * 0.40
)


# Display results
print("\nMatching skills:")
print(matching_skills)

print("\nMissing skills:")
print(missing_skills)

print("\nSkill Match Score:")
print(f"{skill_match_score:.2f}%")

print("\nAI Text Similarity Score:")
print(f"{text_similarity_score:.2f}%")

print("\nCombined Resume Match Score:")
print(f"{combined_match_score:.2f}%")


# Skill recommendations
print("\nRecommended skills to learn:")

for skill in missing_skills:
    print("->", skill)
