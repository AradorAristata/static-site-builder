import unittest
from blockhandler import markdown_to_blocks

class TestBlockHandler(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "This is a block of text.\n\nThis is another block of text.\n\nThis is a third block of text."
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [
            "This is a block of text.",
            "This is another block of text.",
            "This is a third block of text."
        ])

    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )