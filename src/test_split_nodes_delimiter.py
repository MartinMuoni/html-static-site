import unittest

from src.textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_split_italic(self):
        node = TextNode("A _cool_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("A ", TextType.TEXT),
                TextNode("cool", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_non_text_nodes_untouched(self):
        node = TextNode("bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_raises_on_missing_closing(self):
        node = TextNode("This is **broken", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiple_splits_in_one_node(self):
        node = TextNode("a **b** c **d** e", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("a ", TextType.TEXT),
                TextNode("b", TextType.BOLD),
                TextNode(" c ", TextType.TEXT),
                TextNode("d", TextType.BOLD),
                TextNode(" e", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
