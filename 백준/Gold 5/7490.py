def calculator(num):
    global ans
    answer = ""
    if num == N:
        ans.append(str(num))
        for i in ans:
            if i == " ":
                if eval(answer) != 0:
                    answer = str(eval(answer))
                else:
                    answer = answer + i
            else:
                answer += i
        if eval(answer) == 0:
            print(answer)
        ans.pop()
        return
    else:
        for i in ["+", "-", " "]:
            ans.append(str(num))
            ans.append(i)
            calculator(num+1)
            ans.pop()
            ans.pop()
T = int(input())

for _ in range(T):
    N = int(input())
    ans = []
    
    calculator(1)