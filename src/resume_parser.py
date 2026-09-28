from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    if not pdf_path or not str(pdf_path).strip():
        raise ValueError("Please provide a PDF file path.")

    try:
        reader = PdfReader(pdf_path)

        if reader.is_encrypted:
            raise ValueError("PDF is password-protected.")

        text = ""

        for page in reader.pages:
            text += (page.extract_text() or "") + "\n"

        if not text.strip():
            raise ValueError(
                "No readable text found. "
                "The PDF may be scanned or empty."
            )

        return text.strip()

    except FileNotFoundError:
        raise FileNotFoundError(
            f"PDF file not found: {pdf_path}"
        )

    except ValueError:
        raise

    except Exception as e:
        raise ValueError(f"Could not read PDF: {e}")
