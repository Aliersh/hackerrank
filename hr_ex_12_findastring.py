def count_substring(string, sub_string):
    pos = 0
    count = 0
    for char in string:
        tchar = string[pos:pos + len(sub_string)] # tchar is a substring with the first character of the iteration + the next characters (total len = len substring)
        if sub_string == tchar:
            count += 1
            pos += 1
        pos += 1
       
    return count

print(count_substring('ABCDCDC','CDC'))