
def split_n(lis, nr):
    pre = []
    post = []
    for i in range(min(nr, len(lis))):
        pre.append(lis[i])
    for i in range(nr, len(lis)):
        post.append(lis[i])
    return (pre, post)

print(split_n([1, 9, 30, 12], 2))
print(split_n([1], 0))
print(split_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 96, 97, 98, 99, 100], 4))
print(split_n([1, 9, 30, 12], 3))
print(split_n([1, 9, 30, 12], 9))
print(split_n([1, 9, 30, 12], 0))
