"""
Question 3: Mutations
You are given a string and an integer. You have to replace the character at the given index with the given character.
"""
def mutate_string(string, position, character):
    
    string_list = list(string)
    string_list[position] = character

    return ''.join(string_list)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)