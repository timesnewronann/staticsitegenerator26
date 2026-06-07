class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented Error")

    def props_to_html(self):
        if self.props is None:
            return ""

        props_html = ""

        for key in self.props:
            props_html += f' {key}="{self.props[key]}"'

        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        # if the leaf node has no value raise a Value Error all nodes need a value
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        # If there's tag (None) value should be returned as a raw text
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
