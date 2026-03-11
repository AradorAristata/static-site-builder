import unittest
from generator import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_title(self):
        markdown = "# My Title\nThis is some content."
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_without_title(self):
        markdown = "This is some content without a title."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No title found in the provided markdown content.")