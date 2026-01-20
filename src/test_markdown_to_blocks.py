import unittest

from src.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_removes_extra_blank_lines(self):
        md = "Block 1\n\n\n\nBlock 2\n\n\nBlock 3"
        self.assertEqual(markdown_to_blocks(md), ["Block 1", "Block 2", "Block 3"])


if __name__ == "__main__":
    unittest.main()
