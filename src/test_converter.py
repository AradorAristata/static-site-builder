from platform import node
import unittest
from converter import markdown_to_html_node, quote_to_html_node


class TestConverter(unittest.TestCase):
    def test_paragraphs(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

    def test_codeblock(self):
        md = """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
    
    def test_quote(self):
        md = """
            > This is a quote with **bold** text and _italic_ text
            > that should be converted to HTML correctly.
            > It should also handle multiple lines in the quote.
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <b>bold</b> text and <i>italic</i> text that should be converted to HTML correctly. It should also handle multiple lines in the quote.</blockquote></div>",
    )
        
    def test_unordered_list(self):
        md = """
            - Item 1 with **bold** text
            - Item 2 with _italic_ text
            - Item 3 with `code` text
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1 with <b>bold</b> text</li><li>Item 2 with <i>italic</i> text</li><li>Item 3 with <code>code</code> text</li></ul></div>",
    )
        
    def test_ordered_list(self):
        md = """
            1. First item with **bold** text
            2. Second item with _italic_ text
            3. Third item with `code` text
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item with <b>bold</b> text</li><li>Second item with <i>italic</i> text</li><li>Third item with <code>code</code> text</li></ol></div>",
    )