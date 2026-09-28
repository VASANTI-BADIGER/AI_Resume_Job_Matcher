import re


def clean_text(text):
    # Join letters in spaced-out PDF words
    text = re.sub(
        r"\b(?:[a-z]\s+){2,}[a-z]\b",
        lambda m: re.sub(r"\s+", "", m.group()),
        text,
        flags=re.IGNORECASE
    )

    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove unwanted characters
    text = re.sub(r"[^a-zA-Z0-9+#.\s-]", "", text)

    return text.strip()
