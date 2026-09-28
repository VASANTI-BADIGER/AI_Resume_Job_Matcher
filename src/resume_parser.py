from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract readable text from a PDF resume.
    """

    if not pdf_path or not str(pdf_path).strip():
        raise ValueError(
            "Please provide a PDF file path."
        )

    try:
        reader = PdfReader(pdf_path)

        if reader.is_encrypted:
            raise ValueError(
                "PDF is password-protected."
            )

        if len(reader.pages) == 0:
            raise ValueError(
                "The PDF contains no pages."
            )

        page_texts = []

        for page in reader.pages:
            page_text = page.extract_text() or ""
            page_texts.append(page_text)

        text = "\n".join(page_texts).strip()

        if not text:
            raise ValueError(
                "No readable text found. "
                "The PDF may be scanned or empty."
            )

        return text

    except FileNotFoundError:
        raise FileNotFoundError(
            f"PDF file not found: {pdf_path}"
        )

    except ValueError:
        raise

    except Exception as error:
        raise ValueError(
            f"Could not read PDF: {error}"
        )
