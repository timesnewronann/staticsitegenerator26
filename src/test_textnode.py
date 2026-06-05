import unittest
from textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    # --- EQUALITY: things that should be equal ---
    def test_eq_basic(self):
        # --- Same text and text_type without URL ---
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        # --- Same text, text_type, and url ---
        node = TextNode("Click Me", TextType.LINK,
                        "https://nba-player-insight-dashboard.vercel.app/")
        node2 = TextNode("Click Me", TextType.LINK,
                         "https://nba-player-insight-dashboard.vercel.app/")
        self.assertEqual(node, node2)

    def test_eq_url_node_default(self):
        # --- URL default to None, two nodes with no url should be equal ---
        node = TextNode("Hi", TextType.TEXT)
        node2 = TextNode("Hi", TextType.TEXT, None)
        self.assertEqual(node, node2)

    # --- Inequality: things that shouldn't be equal ---

    def test_text_neq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node 2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_text_and_text_type_neq(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        node2 = TextNode("This is a regular text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_type_neq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    


if __name__ == "__main__":
    unittest.main()
