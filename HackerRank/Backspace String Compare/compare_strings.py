def compare_strings(s1, s2):
    s1 = s1.lstrip('#')
    s2 = s2.lstrip('#')

    string1 = ''
    string2 = ''

    for char in s1:
        if char == '#':
            string1 = string1[:-1]
        else:
            string1 += char

    for char in s2:
        if char == '#':
            string2 = string2[:-1]
        else:
            string2 += char

    if string1 == string2:
        return 1
    return 0
