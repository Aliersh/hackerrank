def split_and_join(line):
    lline = line.split(' ')
    jline = '-'.join(lline)
    return jline

line = 'this is a string'
print(split_and_join(line))