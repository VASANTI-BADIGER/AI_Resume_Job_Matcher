
# AI Resume & Job Description Matcher

A Python-based application that analyzes a resume against a job description. It extracts text from PDF resumes, identifies matching and missing skills, and calculates similarity scores to help users understand how their resume aligns with a job.

## Project Overview

The AI Resume & Job Description Matcher is a beginner portfolio project built using Python and Streamlit.

Users can upload a PDF resume and enter a job description. The application processes the text, checks for required skills, and displays matching skills, missing skills, recommendations, and similarity scores.

## Features

- Upload resumes in PDF format.
- Extract text from PDF files.
- Clean and preprocess resume and job-description text.
- Identify matching skills.
- Identify missing skills.
- Recommend skills to focus on developing.
- Calculate a skill match score.
- Calculate text similarity using TF-IDF and cosine similarity.
- Display results through a Streamlit web interface.
- Validate empty job descriptions.

## Technologies Used

- Python
- Streamlit
- Pandas and NumPy (if used in the current implementation)
- scikit-learn
- TF-IDF
- Cosine Similarity
- PDF text extraction
- Git and GitHub

## Project Structure

```text
AI-Resume-Job-Matcher/
│
├── app.py
├── web_app.py
├── pdf_reader.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── matcher.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── text_preprocessing.py
│
├── tests/
├── resume.pdf
└── test_resume.pdf
```

## How It Works

1. **Resume Upload:** The user uploads a resume as a PDF file.
2. **Text Extraction:** The application extracts readable text from the PDF.
3. **Text Preprocessing:** The extracted resume text and job description are cleaned.
4. **Skill Matching:** The application checks which required skills appear in the resume.
5. **Missing Skills:** Required skills not found in the resume are identified.
6. **Similarity Calculation:** TF-IDF and cosine similarity are used to compare the resume text and job description.
7. **Results:** The application displays skill matches, missing skills, recommendations, and scores.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/VASANTI-BADIGER/AI_Resume_Job_Matcher.git
```

### 2. Open the project folder

```bash
cd AI_Resume_Job_Matcher
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

On Linux or Ubuntu:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the web application

```bash
streamlit run web_app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## How to Use

1. Open the application in your browser.
2. Upload a PDF resume.
3. Paste a job description into the text box.
4. Click **Analyze Resume**.
5. Review the matching skills, missing skills, recommendations, and scores.

## Matching Method

The application uses two types of comparison:

- **Skill Match Score:** Measures how many of the listed required skills were found in the resume.
- **Text Similarity Score:** Uses TF-IDF vectorization and cosine similarity to estimate how similar the resume and job-description text are.

The combined score uses a weighted calculation in the current implementation. These scores are simple text-based indicators, not a guarantee of job suitability or selection.

## Testing

The application was manually tested with:

- A sample PDF resume.
- A job description with several matching skills.
- A changed job description with a smaller set of required skills.
- An empty job description to check input validation.

## Limitations

- Skill matching depends on the skills included in the application's predefined list.
- The application may not recognize equivalent skills written using different terms.
- Text similarity measures textual overlap, not actual candidate ability.
- PDF extraction quality depends on the PDF's text and formatting.
- The application is a learning and portfolio project, not a validated recruitment system.

## Future Improvements

- Add more skills and support skill synonyms.
- Improve resume parsing and section detection.
- Add downloadable analysis reports.
- Improve the user interface.
- Add more automated tests.
- Explore semantic similarity methods.

## Author

**Vasanti Badiger**

GitHub: [VASANTI-BADIGER](https://github.com/VASANTI-BADIGER)
