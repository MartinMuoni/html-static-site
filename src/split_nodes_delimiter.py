from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split plain text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # If there's no delimiter, nothing to do
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # Valid markdown requires pairs of delimiters => odd number of parts
        # Example: "a **b** c" split on "**" => ["a ", "b", " c"] (3 parts)
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid markdown: missing closing delimiter '{delimiter}'")

        for i, part in enumerate(parts):
            if part == "":
                # Allow empty segments silently (common at edges), but don't create empty nodes
                continue

            if i % 2 == 0:
                # Outside delimiters => plain text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Inside delimiters => given text_type
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
