import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes


class TestInline(unittest.TestCase):

    # test a single delimited section in the middle of text
    def test_basic_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        # single delimited section in the middle
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ])

    def test_non_text_node_passes_through(self):
        # a node that isn't plain text should come out unchanged
        node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "|", TextType.BOLD)
        self.assertEqual(result, [node])

    def test_unclosed_delimiter_raises(self):
        # missing closing delimiter should raise error
        with self.assertRaises(Exception):
            node = TextNode("hello `world", TextType.TEXT)
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_multiple_nodes(self):
        # two nodes in the input list
        node1 = TextNode("Hello `code`world", TextType.TEXT)
        node2 = TextNode("Foo`bar`baz", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        # expect all sections from both nodes in order
        self.assertEqual(result, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("world", TextType.TEXT),
            TextNode("Foo", TextType.TEXT),
            TextNode("bar", TextType.CODE),
            TextNode("baz", TextType.TEXT)
        ])

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes
        )

    def test_text_to_textnodes(self):
        text = "This is **bold** text and an _italic_ word."
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text and an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)


if __name__ == "__main__":
    unittest.main()
