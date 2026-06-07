import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def htmlNode_eq(self):
        htmlNode = HTMLNode()
        htmlNode2 = HTMLNode()
        self.assertEqual(htmlNode, htmlNode2)


if __name__ == "__main__":
    unittest.main()
