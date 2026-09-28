
import unittest

from src.skill_extractor import (
    skill_exists,
    find_matching_skills,
    find_missing_skills,
)


class TestSkillExtractor(unittest.TestCase):

    def test_skill_exists(self):
        self.assertTrue(skill_exists("I know Python", "python"))

    def test_skill_not_exists(self):
        self.assertFalse(skill_exists("I know Java", "python"))

    def test_matching_skills(self):
        resume = "Python SQL Machine Learning"
        job_description = "Python SQL Machine Learning AWS"
        skills = ["python", "sql", "machine learning", "aws"]

        result = find_matching_skills(
            resume, job_description, skills
        )

        self.assertEqual(
            result, ["python", "sql", "machine learning"]
        )

    def test_missing_skills(self):
        resume = "Python SQL"
        job_description = "Python SQL Machine Learning AWS"
        skills = ["python", "sql", "machine learning", "aws"]

        result = find_missing_skills(
            resume, job_description, skills
        )

        self.assertEqual(result, ["machine learning", "aws"])

    def test_no_matching_skills(self):
        resume = "Java"
        job_description = "Python SQL"
        skills = ["python", "sql"]

        result = find_matching_skills(
            resume, job_description, skills
        )

        self.assertEqual(result, [])

    def test_uppercase_skill(self):
        self.assertTrue(skill_exists("PYTHON DEVELOPER", "python"))

    def test_partial_word_not_matched(self):
        self.assertFalse(skill_exists("I use mailing software", "ml"))

    def test_ml_alias(self):
        self.assertTrue(
            skill_exists("I built ML models", "machine learning")
        )

    def test_ai_alias(self):
        self.assertTrue(
            skill_exists("Artificial Intelligence project", "ai")
        )

    def test_sklearn_alias(self):
        self.assertTrue(
            skill_exists("I use sklearn", "scikit-learn")
        )

    def test_cpp_alias(self):
        self.assertTrue(
            skill_exists("I know cpp", "c++")
        )

    def test_ai_not_inside_mail(self):
        self.assertFalse(
            skill_exists("I know mail", "ai")
        )


if __name__ == "__main__":
    unittest.main()
