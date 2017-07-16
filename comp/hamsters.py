def hamsters(a):
    l = set()
    for i in a:
        if i < 5000:
            l.add(i)
        else:
            l.add(10000-i)
    return(max(l), 10000-min(l))
