import unittest
from task5 import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-12-31"), "31-12-2023")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")
        self.assertEqual(convert_date_format("1999-11-09"), "09-11-1999")

    def test_invalid_format_missing_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-12")
        with self.assertRaises(ValueError):
            convert_date_format("2023")
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_invalid_format_extra_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-12-31-01")
        with self.assertRaises(ValueError):
            convert_date_format("2023-12-31-")

    def test_non_numeric_input(self):
        # The function does not check for numeric values, just splits and rearranges
        self.assertEqual(convert_date_format("abcd-ef-gh"), "gh-ef-abcd")
        self.assertEqual(convert_date_format("year-month-day"), "day-month-year")

    def test_leading_zeros(self):
        self.assertEqual(convert_date_format("2023-01-05"), "05-01-2023")
        self.assertEqual(convert_date_format("2023-10-09"), "09-10-2023")

    def test_invalid_separator(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/12/31")
        with self.assertRaises(ValueError):
            convert_date_format("2023.12.31")
        with self.assertRaises(ValueError):
            convert_date_format("2023 12 31")

if __name__ == '__main__':
    unittest.main()
