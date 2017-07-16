from datetime import datetime

def valid(st):
    if len(st) != 10 or st[9] not in ['0','9'] or st[0:6]=='290200' and st[9] == '9':
        return False
    
    try:
        date = datetime.strptime(st[:6], '%d%m%y')
    except ValueError:
        return False
    
    c = 2
    s = 0
    for i in st[:8][::-1]:
        s += int(i)*c
        c += 1
        if c == 8:
            c = 2
    
    mod = s % 11
    var = 11 - mod
    if var == 11:
        var = 0
    elif var == 10:
        return False
    return var == int(st[8])
