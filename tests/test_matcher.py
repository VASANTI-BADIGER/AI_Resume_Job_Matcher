
import unittest

from src.matcher import (
    calculate_match_score,
    calculate_text_similarity,
    calculate_combined_score,
)


class TestMatcher(unittest.TestCase):

    def test_match_score(self):
        result = calculate_match_score(
            ["python", "sql"],
            ["aws"],
        )
        self.assertEqual(result, 66.67)

    def test_zero_required_skills(self):
        result = calculate_match_score([], [])
        self.assertEqual(result, 0.0)

    def test_all_skills_matched(self):
        result = calculate_match_score(
            ["python", "sql"],
            [],
        )
        self.assertEqual(result, 100.0)

    def test_no_skills_matched(self):
        result = calculate_match_score(
            [],
            ["python", "sql"],
        )
        self.assertEqual(result, 0.0)

    def test_empty_resume_similarity(self):
        result = calculate_text_similarity(
            "",
            "python developer",
        )
        self.assertEqual(result, 0.0)

    def test_empty_job_description_similarity(self):
        result = calculate_text_similarity(
            "python developer",
            "",
        )
        self.assertEqual(result, 0.0)

    def test_text_similarity(self):
        result = calculate_text_similarity(
            "python developer",
            "python developer",
        )
        self.assertGreater(result, 0.0)
        self.assertLessEqual(result, 100.0)

    def test_unusable_text_similarity(self):
        result = calculate_text_similarity(
            "!!!",
            "???",
        )
        self.assertEqual(result, 0.0)

    def test_combined_score(self):
        result = calculate_combined_score(66.67, 25.0)
        self.assertEqual(result, 50.0)


if __name__ == "__main__":
    unittest.main()
