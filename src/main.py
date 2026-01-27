from textnode import TextNode, TextType

# Entry point for HTML static site generator


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


main()
