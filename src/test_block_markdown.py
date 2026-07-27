import unittest
from block import markdown_to_blocks


class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    # a document with just one block (no blank lines at all)
    def test_markdown_one_block(self):
        md = """
One block markdown **markdown** one block!!!
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "One block markdown **markdown** one block!!!"
            ],
        )

    # test a document with multiple blank lines in a row between blocks (not just one blank line - two or three)

    def test_markdown_multiple_blank_lines_between_blocks(self):
        md = """
Block One


- Block two 
- two
- two






# Block three

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Block One",
                "- Block two \n- two\n- two",
                "# Block three"
            ]
        )

    # A document with leading or trailing whitespace/newlines around the whole string
    def test_markdown_leading_trailing_space_lines(self):
        md = """

Trailing whitespaces



"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "Trailing whitespaces"
            ],
        )

    # A document that's just one empty or only whitespace
    def test_markdown_one_empty(self):
        md = """


"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
            ],
        )
