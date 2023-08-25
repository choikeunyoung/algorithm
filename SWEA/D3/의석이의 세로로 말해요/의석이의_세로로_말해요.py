T = int(input())

for tc in range(1,T+1):
    matrix = [ list(map(str,input())) for _ in range(5) ]
    ans = ""
    max_length = 0
    for i in matrix:
        list_length = len(i)
        if max_length < list_length:
            max_length = list_length
    
    for i in matrix:
        list_length = len(i)
        for j in range(max_length-list_length):
            i.append("")
    
    for i in range(max_length):
        for j in range(5):
            if matrix[j][i] != "":
                ans += matrix[j][i]
    print(f"#{tc} {ans}")