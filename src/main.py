from textnode import TextNode, TextType

def main():
    node = TextNode("Text", TextType.TEXT, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()
