N = int(input())
like_list = []
for i in range(N+1):
    i = str(i)
    for char in i:
        if not (char == '4' or char == '7'):
            break
    else:
        max_ = int(i)
print(max_)