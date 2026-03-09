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
    