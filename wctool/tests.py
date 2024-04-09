from django.test import TestCase

from wctool.wctoolutils import extract_file_id_name


class ExtractFileIdNameTests(TestCase):
    def test_extract_id_name(self):
        file = "1-TestName"
        separator = '-'
        result = extract_file_id_name(file, separator)
        expected = ['1', 'TestName']
        self.assertEqual(result, expected)

    def test_extract_with_same_separator(self):
        file = "1-Test-Name-With-Separator"
        separator = '-'
        result = extract_file_id_name(file, separator)
        expected = ['1', 'Test-Name-With-Separator']
        self.assertEqual(result, expected)

    def test_extract_with_different_separator(self):
        file = "1*Test-Name-With-Separator"
        separator = '*'
        result = extract_file_id_name(file, separator)
        expected = ['1', 'Test-Name-With-Separator']
        self.assertEqual(result, expected)
