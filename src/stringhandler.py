import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue

            if node.text.count(delimiter) % 2 != 0:
                raise Exception(f"Delimiter '{delimiter}' not balanced in text: '{node.text}'")
            
            parts = node.text.split(delimiter)

            for i, part in enumerate(parts):
                if part == "":
                    continue   
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes
    

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
    
def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == TextType.TEXT:
            pattern = r"(!\[[^\[\]]*\]\([^\(\)]*\))"
            parts = re.split(pattern, node.text)
            matches = extract_markdown_images(node.text)
            if matches:
                for part in parts:
                    if part == "":
                        continue
                    if part[0] == "!" and part[1] == "[" and part[-1] == ")":
                        new_part = extract_markdown_images(part)
                        new_nodes.append(TextNode(new_part[0][0], TextType.IMAGE, new_part[0][1]))
                    else:
                        new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes
      
def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == TextType.TEXT:
            pattern = r"(\[[^\[\]]*\]\([^\(\)]*\))"
            parts = re.split(pattern, node.text)
            matches = extract_markdown_links(node.text)
            if matches:
                for part in parts:
                    if part == "":
                        continue
                    if part[0] == "[" and part[-1] == ")":
                        new_part = extract_markdown_links(part)
                        new_nodes.append(TextNode(new_part[0][0], TextType.LINK, new_part[0][1]))
                    else:
                        new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)

    return nodes
      