import unittest

from src.skill_extractor import (
    find_matching_skills,
    find_missing_skills,
    skill_exists
)


class TestSkillExtractor(unittest.TestCase):

    def setUp(self):
        self.skills = [
            "python",
            "sql",
            "machine learning",
            "aws"
        ]

    def test_skill_exists(self):
        self.assertTrue(
            skill_exists("I know python", "python")
        )

    def test_skill_not_exists(self):
        self.assertFalse(
            skill_exists("I know java", "python")
        )

    def test_matching_skills(self):
        resume = "I know python and sql"
        job = "Need python, sql and aws"

        result = find_matching_skills(
            resume, job, self.skills
        )

        self.assertEqual(result, ["python", "sql"])

    def test_missing_skills(self):
        resume = "I know python and sql"
        job = "Need python, sql and aws"

        result = find_missing_skills(
            resume, job, self.skills
        )

        self.assertEqual(result, ["aws"])

    def test_no_matching_skills(self):
        resume = "I know java"
        job = "Need python and sql"

        result = find_matching_skills(
            resume, job, self.skills
        )

        self.assertEqual(result, [])

    def test_uppercase_skill(self):
        self.assertTrue(
            skill_exists("I USE PYTHON", "python")
        )

    def test_partial_word_not_matched(self):
        self.assertFalse(
            skill_exists("I know pythons", "python")
        )


if __name__ == "__main__":
    unittest.main()
