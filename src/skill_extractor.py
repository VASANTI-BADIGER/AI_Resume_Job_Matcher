
import re


# Different names that can refer to the same skill.
SKILL_ALIASES = {
    "machine learning": ["machine learning", "ml"],
    "ml": ["machine learning", "ml"],

    "artificial intelligence": [
        "artificial intelligence",
        "ai",
    ],
    "ai": [
        "artificial intelligence",
        "ai",
    ],

    "scikit-learn": ["scikit-learn", "sklearn"],
    "sklearn": ["scikit-learn", "sklearn"],

    "c++": ["c++", "cpp"],
    "cpp": ["c++", "cpp"],
}


def skill_exists(text, skill):
    text = text.lower()
    skill = skill.lower()

    aliases = SKILL_ALIASES.get(skill, [skill])

    for alias in aliases:
        pattern = (
            r"(?<!\w)"
            + re.escape(alias)
            + r"(?!\w)"
        )

        if re.search(pattern, text):
            return True

    return False


def find_matching_skills(resume, job_description, skills):
    matching_skills = []

    for skill in skills:
        if skill_exists(resume, skill) and skill_exists(
            job_description, skill
        ):
            matching_skills.append(skill)

    return matching_skills


def find_missing_skills(resume, job_description, skills):
    missing_skills = []

    for skill in skills:
        if skill_exists(job_description, skill) and not skill_exists(
            resume, skill
        ):
            missing_skills.append(skill)

    return missing_skills
