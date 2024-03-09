"""
Question: Text Wrap
You are given a string S and width w. Your task is to wrap the string into a paragraph of width w.

"""
import textwrap

def wrap(string, max_width):
    wrapped_text = ""
    for i in range(0, len(string), max_width):
        wrapped_text += string[i:i+max_width] + "\n"
    return wrapped_text


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)