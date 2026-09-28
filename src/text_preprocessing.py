
import re


def clean_text(text):
    # Fix spaced-out PDF headings.
    # Example: S K I L L S -> SKILLS
    text = re.sub(
        r"\b(?:[A-Za-z]\s+){2,}[A-Za-z]\b",
        lambda match: re.sub(r"\s+", "", match.group()),
        text
    )

    # Convert text to lowercase.
    text = text.lower()

    # Separate headings that PDFs sometimes join together.
    text = text.replace(
        "languageswork experience",
        "languages work experience"
    )
    text = text.replace(
        "workexperience",
        "work experience"
    )
    text = text.replace(
        "projectsprofile",
        "projects profile"
    )

    # Keep useful characters for technical skills.
    # This preserves terms such as C++, C#, and .NET.
    text = re.sub(r"[^a-z0-9+#.\s-]", " ", text)

    # Replace repeated spaces and line breaks with one space.
    text = re.sub(r"\s+", " ", text)

    return text.strip()
