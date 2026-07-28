from enum import Enum


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(markdown):
    # takes a single block of makrdown text as input and returns the BlockType representing the type of block it is.
    # You can assume all leading and trailing whitespace were already stripped

    # takes a raw markdown string (representing a full document) -> returns a list of "block" strings

    # headings might be the easiest

    # Is this a heading -> answer: how many # characters (if any) are at the very start of the string and is there a space right after them?

    # use a loop that tires prefix lengths 1 - 6, slicing markdown[0:n]
    for length in range(1, 7):
        # at each length is the slice all # characters, and the very next character a space?
        markdown[0:length]


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
