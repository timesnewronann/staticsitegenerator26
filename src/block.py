

# takes a raw markdown string (representing a full document) -> returns a list of "block" strings
def markdown_to_blocks(markdown):
    # 1. split the markdown string into pieces whenever there's a blank line separating them
    # Use .split("\n\n")
    raw_blocks = markdown.split("\n\n")

    # Empty list
    cleaned_blocks = []

    # for each block in raw_blocks
    for raw_block in raw_blocks:
        # strip whitespace from raw_block
        stripped_block = raw_block.strip()

        # if the stripped block is not empty
        if stripped_block:
            # add it it to cleaned_blocks
            cleaned_blocks.append(stripped_block)

    return cleaned_blocks

