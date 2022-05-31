#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

for letter in range(26, 52):
    print("{}".format(chr(letter)), end="")
