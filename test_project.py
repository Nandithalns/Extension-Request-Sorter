
import unittest
import main


class TestExtensionSorter(unittest.TestCase):

    def test_within_policy(self):
        data = {"course": "CS101", "days": 2, "reason": "medical"}
        self.assertEqual(main.classify_request(data), "within_policy")

    def test_faculty_review(self):
        data = {"course": "MA102", "days": 5, "reason": "family"}
        self.assertEqual(main.classify_request(data), "needs_faculty_review")

    def test_missing_course(self):
        data = {"course": None, "days": 2, "reason": "medical"}
        self.assertEqual(main.classify_request(data), "needs_more_info")

    def test_missing_days(self):
        data = {"course": "PH103", "days": None, "reason": "other"}
        self.assertEqual(main.classify_request(data), "needs_more_info")

    def test_three_day_technical_request(self):
        data = {"course": "CS101", "days": 3, "reason": "technical"}
        self.assertEqual(main.classify_request(data), "within_policy")


if __name__ == "__main__":
    unittest.main()
