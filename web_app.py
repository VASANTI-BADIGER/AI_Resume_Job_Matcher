import streamlit as st

from src.resume_parser import extract_text_from_pdf
from src.text_preprocessing import clean_text
from src.skill_extractor import find_matching_skills, find_missing_skills
from src.matcher import calculate_match_score, calculate_text_similarity


SKILLS = [
    "python", "sql", "java", "c", "c++", "javascript",
    "html", "css", "machine learning", "deep learning",
    "artificial intelligence", "data science", "pandas",
    "numpy", "matplotlib", "scikit-learn", "tensorflow",
    "pytorch", "aws", "azure", "google cloud", "docker",
    "git", "linux", "mongodb", "mysql", "postgresql",
    "flask", "django", "streamlit"
]


st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume & Job Description Matcher")
st.write("Upload your resume and compare it with a job description.")

resume_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the job description",
    height=250,
    placeholder="Paste the complete job description here..."
)

if st.button("Analyze Resume", type="primary"):
    if resume_file is None:
        st.error("Please upload your resume PDF.")
    elif not job_description.strip():
        st.error("Please enter a job description.")
    else:
        try:
            with st.spinner("Analyzing your resume..."):
                # Save uploaded PDF temporarily in memory
                import tempfile
                import os

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as temp_file:
                    temp_file.write(resume_file.getvalue())
                    temp_path = temp_file.name

                try:
                    resume_text = extract_text_from_pdf(temp_path)
                finally:
                    os.remove(temp_path)

                if not resume_text.strip():
                    st.error(
                        "No readable text found. "
                        "Please upload a text-based PDF."
                    )
                    st.stop()

                cleaned_resume = clean_text(resume_text)
                cleaned_jd = clean_text(job_description)

                matching_skills = find_matching_skills(
                    cleaned_resume, SKILLS
                )
                missing_skills = find_missing_skills(
                    cleaned_resume, cleaned_jd, SKILLS
                )

                skill_score = calculate_match_score(
                    matching_skills, missing_skills
                )
                text_score = calculate_text_similarity(
                    cleaned_resume, cleaned_jd
                )
                combined_score = (
                    skill_score * 0.7 + text_score * 0.3
                )

            st.success("Analysis complete!")

            st.subheader("Match Scores")

            col1, col2, col3 = st.columns(3)

            col1.metric("Skill Match", f"{skill_score:.2f}%")
            col2.metric("Text Similarity", f"{text_score:.2f}%")
            col3.metric("Combined Match", f"{combined_score:.2f}%")

            st.subheader("Matching Skills")
            if matching_skills:
                st.write(", ".join(matching_skills))
            else:
                st.info("No matching skills found.")

            st.subheader("Missing Skills")
            if missing_skills:
                st.write(", ".join(missing_skills))
            else:
                st.write("No missing skills found from the skill list.")

            st.subheader("Recommended Skills to Learn")
            if missing_skills:
                for skill in missing_skills:
                    st.write(f"- {skill}")
            else:
                st.write("No recommendations at this time.")

        except Exception as error:
            st.error(f"Something went wrong: {error}")
