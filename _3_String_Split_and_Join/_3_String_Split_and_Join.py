"""
Question 3: String Split and Join
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Return the modified string.
"""

def split_and_join(line):
    
    result = "-".join(word for word in line.split(" "))
    
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)