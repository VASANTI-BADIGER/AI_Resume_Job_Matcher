from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


pdf_path = input("Enter PDF file path: ")

resume_text = extract_text_from_pdf(pdf_path)

print("\nExtracted Resume Text:")
print(resume_text)
