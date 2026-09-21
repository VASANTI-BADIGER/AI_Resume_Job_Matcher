from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def find_matching_skills(resume, job_description, skills):
    matching_skills = []

    for skill in skills:
        if skill in resume and skill in job_description:
            matching_skills.append(skill)

    return matching_skills


def find_missing_skills(resume, job_description, skills):
    missing_skills = []

    for skill in skills:
        if skill in job_description and skill not in resume:
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

# Convert text to lowercase
resume = resume.lower()
job_description = job_description.lower()

skills = [
    "python",
    "sql",
    "machine learning",
    "pandas",
    "numpy",
    "tensorflow",
    "aws"
]

matching_skills = find_matching_skills(
    resume,
    job_description,
    skills
)

missing_skills = find_missing_skills(
    resume,
    job_description,
    skills
)

skill_match_score = calculate_match_score(
    matching_skills,
    missing_skills
)

text_similarity_score = calculate_text_similarity(
    resume,
    job_description
)

combined_match_score = (
    skill_match_score * 0.60
    + text_similarity_score * 0.40
)

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

print("\nRecommended skills to learn:")

for skill in missing_skills:
    print("->", skill)
