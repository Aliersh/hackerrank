import string

def swap_case(s):
    ns = ''
    for char in s:
        if char in string.ascii_uppercase:
            char = char.lower()
            ns = ns + char
        else:
            char = char.upper()
            ns = ns + char
    return ns

s = input()