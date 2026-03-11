from blockhandler import BlockType, markdown_to_blocks, block_to_block_type
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from stringhandler import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def heading_to_html_node(block):
    heading_rank = len(block.split()[0])  # Number of '#' characters
    child_html_nodes = text_to_children(block[heading_rank:].strip())
    return ParentNode(f"h{heading_rank}", child_html_nodes)

def code_to_html_node(block):
    child_text_node = TextNode(block[4:-3], TextType.TEXT)
    code_html_node = text_node_to_html_node(child_text_node)
    code_parent_node = ParentNode("code", [code_html_node])
    pre_parent_node = ParentNode("pre", [code_parent_node])
    return pre_parent_node

def quote_to_html_node(block):
    child_html_nodes = text_to_children(" ".join(line.lstrip("> ").strip() for line in block.splitlines()))
    return ParentNode("blockquote", child_html_nodes)

def unordered_list_to_html_node(block):
    list_items = block.splitlines()
    child_html_nodes = []
    for item in list_items:
        item_text = item[2:].strip()  # Remove "- " from the beginning
        item_child_html_nodes = text_to_children(item_text)
        child_html_nodes.append(ParentNode("li", item_child_html_nodes))
    return ParentNode("ul", child_html_nodes)

def ordered_list_to_html_node(block):
    list_items = block.splitlines()
    child_html_nodes = []
    for item in list_items:
        item_text = item[item.find(". ")+2:].strip()  # Remove "1. ", "2. ", etc. from the beginning
        item_child_html_nodes = text_to_children(item_text)
        child_html_nodes.append(ParentNode("li", item_child_html_nodes))
    return ParentNode("ol", child_html_nodes)

def paragraph_to_html_node(block):
    child_html_nodes = text_to_children(" ".join(line.strip() for line in block.splitlines()))
    return ParentNode("p", child_html_nodes)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                nodes.append(heading_to_html_node(block))
            case BlockType.CODE:
                nodes.append(code_to_html_node(block))
            case BlockType.QUOTE:
                nodes.append(quote_to_html_node(block))
            case BlockType.UNORDERED_LIST:
                nodes.append(unordered_list_to_html_node(block))
            case BlockType.ORDERED_LIST:
                nodes.append(ordered_list_to_html_node(block))
            case BlockType.PARAGRAPH:
                nodes.append(paragraph_to_html_node(block))
    return ParentNode("div", nodes)  # Wrap all blocks in a div for the final HTML node


        # Convert block to HTML node based on block_type
        # This is where the actual conversion logic would go



