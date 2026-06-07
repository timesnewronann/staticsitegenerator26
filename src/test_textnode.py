import unittest
from textnode import TextType, TextNode, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("Click Me", TextType.LINK,
                        "https://nba-player-insight-dashboard.vercel.app/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click Me")
        self.assertEqual(html_node.props, {
                         "href": "https://nba-player-insight-dashboard.vercel.app/"})

    def test_image(self):
        node = TextNode("some alt text", TextType.IMAGE, "https://example.com/pic.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
                         "src": "https://example.com/pic.png", "alt": "some alt text"})


if __name__ == "__main__":
    unittest.main()
