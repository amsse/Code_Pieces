# You are given a string "s" and width "w".
# Your task is to wrap the string into a paragraph of width "w".
#
# Input Format:
# The first line contains a string, "s".
# The second line contains the width, "w".

# Output Format:
# Print the text wrapped paragraph.

import textwrap


def wrap(string, max_width):
    txw = textwrap.wrap(string, max_width)
    result = ""
    for i in txw:
        print(i)
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


############################################
#
# WITHOUT TEXTWRAP:
# def wrap(string, max_width):
#     return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
#
############################################
