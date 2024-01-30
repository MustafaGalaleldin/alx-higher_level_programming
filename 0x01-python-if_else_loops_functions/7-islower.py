#!/usr/bin/python3
def islower(c):
    """
    Check if a character is lowercase.

    Parameters:
    c (str): The character to check.

    Returns:
    bool: True if the character is lowercase, False otherwise.
    """
    return ord(c) in range(ord('a'), ord('z') + 1)
