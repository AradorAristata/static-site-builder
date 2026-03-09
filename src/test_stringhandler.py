import unittest

from stringhandler import split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node

class TestStringHandler(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("This is a *bold* text node", TextType.TEXT),
            TextNode("This is an *italic* text node", TextType.TEXT),
            TextNode("This is a text node with *unbalanced delimiter", TextType.TEXT),
            TextNode("This is a text node with **double delimiter**", TextType.TEXT),
            TextNode("This is a text node with no delimiters", TextType.TEXT),
            TextNode("*Bold at start*", TextType.TEXT),
            TextNode("Bold at end*", TextType.TEXT),
        ]

        try:
            new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        except Exception as e:
            print(f"Error: {e}")


    def test_split_nodes_code_(self):
        nodes = [
            TextNode("This is a `code` text node", TextType.TEXT)]

        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text node", TextType.TEXT)
        ])

    def test_split_nodes_unbalanced_delimiter(self):
        nodes = [
            TextNode("This is a *bold text node with unbalanced delimiter", TextType.TEXT)
        ]

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(nodes, "*", TextType.BOLD)
        
        self.assertTrue("Delimiter '*' not balanced in text: 'This is a *bold text node with unbalanced delimiter'" in str(context.exception))
