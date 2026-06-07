import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_no_value_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_tag(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click Me!</a>')


class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
