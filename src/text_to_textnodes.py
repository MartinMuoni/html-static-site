from src.textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter
from src.split_nodes_image_link import split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    # First handle images and links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # Then handle inline delimiters
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes
