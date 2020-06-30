def solve(s):
    ls = s.split(' ')
    cs = ''
    for word in ls:
        if word is ls[0]:
            cs = word.capitalize()
        else:
            cs += ' ' + word.capitalize()
    return cs

print(solve('hello world'))