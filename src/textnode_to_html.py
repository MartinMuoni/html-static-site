from src.textnode import TextNode, TextType
from src.leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("LINK TextNode must have a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("IMAGE TextNode must have a URL")
        return LeafNode(
            "img",
            "",
            {"src": text_node.url, "alt": text_node.text},
        )

    raise Exception(f"Unknown TextType: {text_node.text_type}")
