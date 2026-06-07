import unittest
from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def htmlNode_eq(self):
        htmlNode = HTMLNode()
        htmlNode2 = HTMLNode()
        self.assertEqual(htmlNode, htmlNode2)

    # Constructor stores the values correctly
    def test_props(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://boot.dev"})
        assert node.tag == "a"
        assert node.value == "Boot.dev"
        assert node.children is None
        assert node.props == {"href": "https://boot.dev"}

    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://boot.dev"})
        assert node.props_to_html() == ' href="https://boot.dev"'

    def test_props_to_html_multiple_props(self):
        node = HTMLNode("a", "Boot.dev", None, {
            "href": "https://boot.dev",
            "target": "_blank",
        })
        html = node.props_to_html()
        assert ' href="https://boot.dev"' in html
        assert ' target="_blank"' in html

    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "hello", None, None)
        assert node.props_to_html() == ""

    def test_to_html_raises(self):
        node = HTMLNode("p", "hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()
