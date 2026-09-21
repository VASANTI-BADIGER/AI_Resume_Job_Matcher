import re


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
