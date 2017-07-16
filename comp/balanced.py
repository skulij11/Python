
def balanced(st):
    c = 0
    for i in st:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        if c < 0:
            return False
    return c == 0
