import textwrap

def wrap(string, max_width):
    wstring = textwrap.wrap(string,max_width)
    return for word in wstring:
        print(word)
        
print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',4)) # Why print None?