#!/usr/bin/python3

"""
Module contenaing text_indentation function
"""


def text_indentation(text):
    """
    Prints 2 new line after the characters ., ? , :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tmp_text = ""
    for character in text:
        tmp_text += character
        if character in ['?', '.', ':']:
            print(tmp_text.strip() + "\n")
            tmp_text = ''
    print(tmp_text.strip(), end="")
