import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_props(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_url_none_vs_value(self):
        node1 = TextNode("link", TextType.LINK, None)
        node2 = TextNode("link", TextType.LINK, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_same_url(self):
        node1 = TextNode("link", TextType.LINK, "https://example.com")
        node2 = TextNode("link", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
