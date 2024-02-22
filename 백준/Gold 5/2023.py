def backtracking(total, cnt):
    global answer
    if cnt == N:
        print("".join(answer))
        return
    
    for num in num_list:
        if int(num)%2 != 0:
            if (total + int(num))%3 != 0 and num != "5":
                total += int(num)
                answer.append(num)
                backtracking(total, cnt+1)
                answer.pop()
                total -= int(num)



N = int(input())

num_list = ["0","1","2","3","4","5","6","7","8","9"]
ans_list = ["2","3","5","7"]
if N == 1:
    for ans in ans_list:
        print(ans)
else:
    for ans in ans_list:
        answer = [ans]
        backtracking(int(answer[0]), 1)


