
def palindrome(n, b):
    lis = []
    while n > 0:
        lis.insert(0,n%b)
        n //= b
    print(lis)
    return lis == lis[::-1]
