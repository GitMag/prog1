"""
COMP.CS.100 Programming 1
ROT13 program code template
"""


def row_encryption(text):
    """
    Encrypts a row of text with rot13 algorithm. Returns the encrypted row of
    text
    :param text: str, row of text to encrypt
    :return: str, encrypted row of text
    """
    encrypted_text = ""
    for letter in text:
        letter = encrypt(letter)
        encrypted_text += letter
    return encrypted_text


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]
    if text.isalpha():
        letter_index = regular_chars.index(text.lower())
        if text.isupper():
            text = encrypted_chars[letter_index]
            text = text.upper()
        else:
            text = encrypted_chars[letter_index]
    return text
