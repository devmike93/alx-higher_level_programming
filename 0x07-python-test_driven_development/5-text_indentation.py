#!/usr/bin/python3
"""
Text Indentation Module
"""


def text_indentation(text):
    """
    Format Text with Paragraphs

    This function takes an input text and formats it into paragraphs.
    It adds two newline characters ("\n\n") after each occurrence of:
    '.', '?', or ':' in the text.
    Additionally, it ensures that there are no leading or trailing whitespace
    characters in each paragraph.

    Args:
    text (str): The input text to be formatted.

    Raises:
    TypeError: If the input text is not a string or is None.
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    txt = "".join([char + "\n\n" if char in ".?:" else char for char in text])
    print("\n".join([line.strip() for line in txt.split("\n")]), end="")
