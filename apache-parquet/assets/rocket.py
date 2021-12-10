"""Prints a rocket to the std output."""
from time import sleep

# pylint: disable-all


def print_rocket():
    """Prints a rocket to the std output.
    The implementation is taken from https://steemit.com/wherein/@justyy/the-simple-console-rocket-animation-in-python"""
    print(
        """
           _
          /^\\
          |-|
          | |
          |N|
          |A|
          |S|
          |A|
         /| |\\
        / | | \\
       |  | |  |
       `-\\"\\"\\"-`
"""
    )


print_rocket()

delay = 500
for i in range(60):
    print()
    sleep(delay / 1000)
    delay = delay * 0.9
