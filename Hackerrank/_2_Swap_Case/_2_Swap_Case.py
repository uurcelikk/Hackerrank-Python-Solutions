"""
Question: Swap Case 
Given a string, convert it into a string with upper case and lower case swapped.
Return the modified string.
"""
def swap_case(s):
    swapped = ''
    for char in s:
        if char.islower():
            swapped += char.upper()
        elif char.isupper():
            swapped += char.lower()
        else:
            swapped += char
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#Solution2
# def swap_case(s):
#     return s.swapcase()

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)