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
        if char is ' ' and mine[len(mine) - 1] is '\n':
            continue
        mine += char
        if char in [':', '.', '?']:
            mine += '\n' * 2

    print(mine)
