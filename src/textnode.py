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