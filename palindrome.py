def palindrome(n):
    n = str(n)
    i = 0
    res = True
    while i<((len(n))/2):
        if n[i] != n[-(i+1)]:
            return False        
        i += 1
    return
print(palindrome(1000021))
