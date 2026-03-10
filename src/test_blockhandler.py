import unittest
from blockhandler import BlockType, markdown_to_blocks, block_to_block_type

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

    def test_markdown_to_blocks_with_empty_blocks(self):
        md = """
        This is a block of text.

        This is another block of text.

        This is a third block of text.
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "This is a block of text.",
            "This is another block of text.",
            "This is a third block of text."
        ])

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\nCode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Quote\n> continued quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Unordered list item\n- Another item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Ordered list item\n2. Another item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_block_to_block_type_edge_cases(self):
        self.assertEqual(block_to_block_type(""), None)
        self.assertEqual(block_to_block_type("####### Not a heading"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("```\nUnbalanced code block"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("> Bad quote\n More bad quote"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("- Bad list item\n No list marker"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1. Weird number ordered list item\n3. Your Mom"), BlockType.PARAGRAPH)