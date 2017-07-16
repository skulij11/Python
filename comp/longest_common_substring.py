
def longest_common_substring(words):
    st = words[0]
    l = len(st)
    
    while l > 0:
        for i in range(len(st)):
            
            for k in words[1:]:
                if k.find(st[i:i+l]) == -1:
                    break
            else:
                return l
            
            if i + l > len(st) - 1:
                l -= 1
                break
    return 0

