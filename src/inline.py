from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def split_nodes_delimiter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    # return a new list of nodes
    # where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax
    # If an "old node" is not a TextType.TEXT add it to the new list as-is
    # Only attempt to split "text" type objects (not bold, italic, etc)

    # I think we'd have to go through the list of old_nodes

    # list of new nodes we'll return
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # add it to the new list as is
            new_nodes.append(node)
            continue

        # temporary list
        split_nodes = []
        # go through the text of the node
        split_list = node.text.split(delimeter)

        # if the split list has an even number of sections -> delimeter was opened but not closed
        if len(split_list) % 2 == 0:
            # raise an exception, matching closing delimeter is not found raise an exception
            raise Exception(f"The matching closing delimeter: {delimeter} is not found")

        for i in range(len(split_list)):
            if len(split_list[i]) == 0:
                # skip the string
                continue

            if i % 2 == 0:
                # decide which text type
                # Create a plain text
                new_node = TextNode(split_list[i], TextType.TEXT)
                split_nodes.append(new_node)
            else:
                # it's odd so special
                new_node = (TextNode(split_list[i], text_type))
                split_nodes.append(new_node)

        new_nodes.extend(split_nodes)

    return new_nodes
