
import unittest
from src.resume_parser import extract_text_from_pdf


class TestResumeParser(unittest.TestCase):

    def test_missing_pdf(self):
        with self.assertRaises(FileNotFoundError):
            extract_text_from_pdf("missing_resume.pdf")

    def test_empty_path(self):
        with self.assertRaises(ValueError):
            extract_text_from_pdf("")

    def test_invalid_pdf(self):
        with self.assertRaises(ValueError):
            extract_text_from_pdf("README.md")


if __name__ == "__main__":
    unittest.main()
