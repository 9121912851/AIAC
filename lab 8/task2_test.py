import unittest
from task2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    def test_grade_a(self):
        self.assertEqual(assign_grade(90), 'A')
        self.assertEqual(assign_grade(95), 'A')
        self.assertEqual(assign_grade(100), 'A')

    def test_grade_b(self):
        self.assertEqual(assign_grade(80), 'B')
        self.assertEqual(assign_grade(85), 'B')
        self.assertEqual(assign_grade(89), 'B')

    def test_grade_c(self):
        self.assertEqual(assign_grade(70), 'C')
        self.assertEqual(assign_grade(75), 'C')
        self.assertEqual(assign_grade(79), 'C')

    def test_grade_d(self):
        self.assertEqual(assign_grade(60), 'D')
        self.assertEqual(assign_grade(65), 'D')
        self.assertEqual(assign_grade(69), 'D')

    def test_grade_f(self):
        self.assertEqual(assign_grade(0), 'F')
        self.assertEqual(assign_grade(59), 'F')
        self.assertEqual(assign_grade(30), 'F')

    def test_invalid_input_type(self):
        self.assertEqual(assign_grade("90"), 'Invalid input')
        self.assertEqual(assign_grade(None), 'Invalid input')
        self.assertEqual(assign_grade([90]), 'Invalid input')
        self.assertEqual(assign_grade({'score': 90}), 'Invalid input')

    def test_invalid_input_range(self):
        self.assertEqual(assign_grade(-1), 'Invalid input')
        self.assertEqual(assign_grade(101), 'Invalid input')
        self.assertEqual(assign_grade(150), 'Invalid input')
        self.assertEqual(assign_grade(-20), 'Invalid input')

    def test_float_scores(self):
        self.assertEqual(assign_grade(89), 'B')
        self.assertEqual(assign_grade(79), 'C')
        self.assertEqual(assign_grade(69), 'D')
        self.assertEqual(assign_grade(59), 'F')
        self.assertEqual(assign_grade(100), 'A')

if __name__ == '__main__':
    unittest.main()
