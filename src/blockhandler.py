from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    new_blocks = []
    blocks = markdown.split("\n\n")
    for i, block in enumerate(blocks):
        if block == "":
            continue
        if "\n" in block:
            block = "\n".join(line.strip() for line in block.splitlines())
        new_blocks.append(block.strip())
    return new_blocks

def block_to_block_type(block):
    if block == "":
        return None
    if all(c == "#" for c in block.split()[0]) and len(block.split()[0]) < 7 and block[len(block.split()[0])] == " ":
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in block.splitlines()):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{j+1}. ") for j, line in enumerate(block.splitlines())):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH