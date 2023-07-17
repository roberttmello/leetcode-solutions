def romanToInt(str):
    table = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100,'D':500,  'M': 1000}
    total = 0
    for i in range(len(str)):
        if i < len(str) - 1 and table[str[i]] < table[str[i + 1]]:
            total -= table[str[i]]
        else:
            total += table[str[i]]
    return total

print(romanToInt('IV'))
