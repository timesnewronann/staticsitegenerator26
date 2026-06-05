from enum import Enum

"""
COVER TYPES
text (plain)
**Bold text**
_Italic text_
`Code text`
Links, in this format: [anchor text](url)
Images, in this format: ![alt text](url)
"""


class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD_TEXT = "**"
    ITALIC_TEXT = "__"
    CODE_TEXT = "``"
    LINK = "[]()"
    IMAGE = "![]()"


class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        pass

    def __repr__(self):
        pass
