# AI Resume & Job Description Matcher

A Python application that analyzes a resume against a job description. It identifies matching skills, missing skills, and calculates resume match scores using skill matching and text similarity.

## Features

* Extracts text from PDF resumes
* Accepts multiline job descriptions
* Identifies matching skills
* Detects missing skills
* Calculates skill match score
* Calculates TF-IDF text similarity using cosine similarity
* Calculates a combined resume match score
* Recommends skills to learn

## Technologies Used

* Python
* pypdf
* Scikit-learn
* TF-IDF
* Cosine Similarity
* Git
* GitHub

## How It Works

1. Enter the path to a resume PDF.
2. Paste the job description, including multiple lines.
3. Press Enter on an empty line to finish the description.
4. The application extracts and cleans the resume and job description text.
5. It identifies matching and missing skills.
6. It calculates skill match, text similarity, and combined scores.
7. It recommends skills that are missing from the resume.

## Project Structure

```text
AI-Resume-Job-Matcher/
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── resume_parser.py
│   ├── text_preprocessing.py
│   ├── skill_extractor.py
│   └── matcher.py
└── tests/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/VASANTI-BADIGER/AI_Resume_Job_Matcher.git
cd AI_Resume_Job_Matcher
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

When prompted for the resume PDF path, enter:

```text
test_resume.pdf
```

For testing, use this sample job description:

```text
Python Developer Fresher
Required Skills:
Python
SQL
Git
Linux
Pandas
NumPy
Machine Learning
AWS
```

Press Enter on an empty line after the final line of the job description.

## Scoring

The application calculates:

* Skill Match Score: based on skills found in both the resume and job description.
* Text Similarity Score: based on TF-IDF and cosine similarity.
* Combined Match Score: 60% skill match score and 40% text similarity score.

These scores are indicators for comparing text, not guarantees of job suitability or hiring outcomes.

## Testing

Run the unit tests with:

```bash
python -m unittest discover -s tests -v
```

## Future Improvements

* Support DOCX resumes
* Expand the skill database
* Improve skill extraction
* Add a simple web interface
* Allow users to download the match report

## Author

Vasanti Badiger
