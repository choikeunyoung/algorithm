T = int(input())

binary_dict = {
    "0001101" : "0",
    "0011001" : "1",
    "0010011" : "2",
    "0111101" : "3",
    "0100011" : "4",
    "0110001" : "5",
    "0101111" : "6",
    "0111011" : "7",
    "0110111" : "8",
    "0001011" : "9",
}

for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [ list(map(str,input())) for _ in range(N) ]
    for i in range(N):
        if "1" in matrix[i]:
            break
    start = -1
    end = -1
    for j in range(M):
        if matrix[i][j] == "1":
            if start == -1:
                start = j
            else:
                end = j

    ans = "".join(matrix[i][start:end+1])
    
    if end - start < 56:
        ans = "0"*(56 - (end-start) - 1) + ans
    answer = ""
    for k in range(0,56,7):
        answer += binary_dict[ans[k:k+7]]
    
    even_total = 0
    odd_total = 0
    for i in range(8):
        if i % 2 == 0:
            odd_total += int(answer[i])
        else:
            even_total += int(answer[i])

    total = odd_total*3 + even_total

    if total % 10 == 0:
        print(f"#{tc} {even_total+odd_total}")
    else:
        print(f"#{tc} 0")