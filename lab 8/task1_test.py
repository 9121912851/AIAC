import unittest
from task1 import generate_email

class TestGenerateEmail(unittest.TestCase):
    def test_basic_email(self):
        self.assertEqual(
            generate_email('john', 'doe', 'example.com'),
            'john.doe@example.com'
        )

    def test_uppercase_names(self):
        self.assertEqual(
            generate_email('JOHN', 'DOE', 'EXAMPLE.COM'),
            'john.doe@example.com'
        )

    def test_mixed_case_names(self):
        self.assertEqual(
            generate_email('JoHn', 'DoE', 'ExAmPlE.CoM'),
            'john.doe@example.com'
        )

    def test_names_with_spaces(self):
        self.assertEqual(
            generate_email(' John ', ' Doe ', ' Example.com '),
            ' john . doe @ example.com '
        )

    def test_names_with_hyphens(self):
        self.assertEqual(
            generate_email('Mary-Jane', 'O\'Connor', 'mail.com'),
            "mary-jane.o'connor@mail.com"
        )

    def test_numeric_names(self):
        self.assertEqual(
            generate_email('user1', 'test2', 'domain123.com'),
            'user1.test2@domain123.com'
        )

    def test_empty_first_name(self):
        self.assertEqual(
            generate_email('', 'doe', 'example.com'),
            '.doe@example.com'
        )

    def test_empty_last_name(self):
        self.assertEqual(
            generate_email('john', '', 'example.com'),
            'john.@example.com'
        )

    def test_empty_domain(self):
        self.assertEqual(
            generate_email('john', 'doe', ''),
            'john.doe@'
        )

    def test_all_empty(self):
        self.assertEqual(
            generate_email('', '', ''),
            '.@'
        )

if __name__ == '__main__':
    unittest.main()
