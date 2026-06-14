from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from extractLinks import extract_markdown_images, extract_markdown_links


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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # extract the image in the node.text
        images = extract_markdown_images(node.text)

        # if no images found
        if len(images) == 0:
            # add the node as is
            new_nodes.append(node)
            continue

        # keep track of the remaining text
        remaining_text = node.text

        for alt, url in images:
            # Split remaining_text on ![alt](url) with maxsplit=1
            text_before, text_after = remaining_text.split(f'![{alt}]({url})', 1)

            if len(text_before) != 0:
                # construct the text node the nadd it in
                before_node = TextNode(text_before, TextType.TEXT)
                # add a text node for text_before
                new_nodes.append(before_node)

            # add an image node for (alt, url)
            image_node = TextNode(alt, TextType.IMAGE, url)
            new_nodes.append(image_node)

            remaining_text = text_after

        if len(remaining_text) != 0:
            # add a text node for remaining_text
            remaining_node = TextNode(remaining_text, TextType.TEXT)
            new_nodes.append(remaining_node)

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # extract the links in the node.text
        links = extract_markdown_links(node.text)

        # if no links are found
        if len(links) == 0:
            new_nodes.append(node)
            continue

        # keep track of our remaining text
        remaining_text = node.text

        for anchor, url in links:
            # Split remaining text on [anchor](url)
            text_before, text_after = remaining_text.split(f"[{anchor}]({url})", 1)

            if len(text_before) != 0:
                before_node = TextNode(text_before, TextType.TEXT)
                new_nodes.append(before_node)

            # add a link node
            link_node = TextNode(anchor, TextType.LINK, url)
            new_nodes.append(link_node)

            remaining_text = text_after

        if len(remaining_text) != 0:
            remaining_text = TextNode(remaining_text, TextType.TEXT)
            new_nodes.append(remaining_text)

    return new_nodes
