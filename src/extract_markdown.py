import re


def extract_markdown_images(text):
    # Returns list of (alt, url)
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    # Returns list of (anchor, url) but NOT images
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
