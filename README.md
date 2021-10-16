# Simple Caesar cipher module

## Introduction

This project is a simple, short module which implements Caesar cipher encryption and decryption functions. This approach uses an integer key to shift each character by the number of characters indicated by the key (e.g., if the character is 'A' and the key is 3, the encrypted character is 'D'). See the image below for an example:

![Example](https://github.com/vx5/caesar-cipher/blob/main/images/screenshot.png)

## How to use

To use this simple module, add an import line to the top of the file, such as any of the following:

```python3
import caesar_cipher
from caesar_cipher import caesarEncrypt
from caesar_cipher import caesarEncrypt, caesarDecrypt
```