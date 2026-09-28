from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)

        if reader.is_encrypted:
            raise ValueError("PDF is password-protected.")

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        if not text.strip():
            raise ValueError(
                "No readable text found in PDF."
            )

        return text

    except FileNotFoundError:
        raise FileNotFoundError(
            f"PDF file not found: {pdf_path}"
        )

    except Exception as e:
        raise ValueError(
            f"Could not read PDF: {e}"
        )
