

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