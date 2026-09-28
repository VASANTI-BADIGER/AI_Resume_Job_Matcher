
from src.resume_parser import extract_text_from_pdf
from src.text_preprocessing import clean_text
from src.skill_extractor import find_matching_skills, find_missing_skills
from src.matcher import calculate_match_score, calculate_text_similarity


# Skills database
SKILLS = [
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


def main():
    print("=" * 45)
    print("       AI RESUME & JOB MATCHER")
    print("=" * 45)

    # Get resume PDF
    pdf_path = input("\nEnter resume PDF path: ").strip()

    if not pdf_path:
        print("Error: Please enter a PDF file path.")
        return

    # Read resume
    try:
        resume_text = extract_text_from_pdf(pdf_path)
    except (ValueError, FileNotFoundError) as error:
        print(f"\nError: {error}")
        return

    # Get job description
    job_description = input(
        "\nEnter the job description: "
    ).strip()

    if not job_description:
        print("Error: Job description cannot be empty.")
        return

    # Clean both texts
    resume = clean_text(resume_text)
    job_description = clean_text(job_description)

    # Find matching and missing skills
    matching_skills = find_matching_skills(
        resume,
        job_description,
        SKILLS
    )

    missing_skills = find_missing_skills(
        resume,
        job_description,
        SKILLS
    )

    # Calculate scores
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

    # Display report
    print("\n")
    print("=" * 45)
    print("             MATCH REPORT")
    print("=" * 45)

    print("\nMatching skills:")
    if matching_skills:
        for skill in matching_skills:
            print("  +", skill)
    else:
        print("  No matching skills found.")

    print("\nMissing skills:")
    if missing_skills:
        for skill in missing_skills:
            print("  -", skill)
    else:
        print("  No missing skills found.")

    print("\n" + "-" * 45)
    print(f"Skill Match Score:       {skill_match_score:.2f}%")
    print(f"Text Similarity Score:   {text_similarity_score:.2f}%")
    print(f"Combined Match Score:    {combined_match_score:.2f}%")
    print("-" * 45)

    # Recommendations
    print("\nRecommended skills to learn:")

    if missing_skills:
        for skill in missing_skills:
            print("  ->", skill)
    else:
        print("  No missing skills from this database.")

    print("\n" + "=" * 45)
    print("             END OF REPORT")
    print("=" * 45)


if __name__ == "__main__":
    main()
