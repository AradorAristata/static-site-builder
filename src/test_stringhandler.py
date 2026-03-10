from platform import node
import unittest

from stringhandler import extract_markdown_images, split_nodes_delimiter, extract_markdown_links, split_nodes_image, split_nodes_links, text_to_textnodes
from textnode import TextNode, TextType

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


    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://example.com)")
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links(self):
        node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example.org)",
        TextType.TEXT,)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://example.org"
            ),
        ],
        new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **bold** text with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )