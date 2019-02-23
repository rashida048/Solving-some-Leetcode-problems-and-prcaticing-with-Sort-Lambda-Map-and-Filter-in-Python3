def romanToInteger(s):
    symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    join = {'IV': (4-6), 'IX': (9-11), 'XL': (40-60),
            'XC': (90-110), 'CD': (400-600), 'CM': (900-1100)}
    res = 0
    i = 0
    while i < len(s):
        res += symbol[s[i]]
        js = s[i-1] + s[i]
        if i != 0 and (js) in join:
            res += join[js]
        i += 1
    return res
print(romanToInteger("MCMXCIV"))
