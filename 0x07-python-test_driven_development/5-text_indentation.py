#!/usr/bin/python3
""" indent """


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    mine = ""
    for char in text:
        mine += char
        if char in [':', '.', '?']:
            mine += '\n\n'
    print(mine)
