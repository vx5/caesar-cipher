"""
Module includes functions that work together to encrypt/decrypt strings using a caesar cipher.
"""

# Constants used in both encryption and decryption
MIN_VAL = ord('a')
NUM_LETTERS = 26


def caesar_encrypt(text, key):
    """
    INPUTS:
    Text to be encrypted (str) [text]
    Encryption key (int) [key]
    OUTPUT:
    Encrypted text (str)
    """
    # Warns when key is 0, because no change will be made to text
    if not key:
        return 'Error: key cannot be 0'
    lower_text = text.lower()
    output = []
    # Iterates through given text
    for char in lower_text:
        # Ignores non-alpha characters
        if not char.isalpha():
            continue
        # Shifts letters up alphabet by <key> chars
        adj_num = ord(char) - MIN_VAL
        encr_num = (adj_num + key) % NUM_LETTERS
        encr_char = chr(encr_num + MIN_VAL)
        output.append(encr_char)
    return ''.join(output)


def caesar_decrypt(text, key):
    """
        INPUTS:
        Text to be decrypted (str) [text]
        Encryption key (int) [key]
        OUTPUT:
        Encrypted text (str)
        """
    lower_text = text.lower()
    output = []
    for char in lower_text:
        # Non-alpha characters, if found, are not decrypted
        if not char.isalpha():
            decr_char = char
        else:
            # Shifts characters down alphabet by <key> chars
            # to reverse encryption
            adj_num = ord(char) - MIN_VAL
            decr_num = (adj_num - key) % NUM_LETTERS
            decr_char = chr(decr_num + MIN_VAL)
        output.append(decr_char)
    return ''.join(output)
