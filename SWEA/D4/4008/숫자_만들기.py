def find_num(num):
    global min_num
    global max_num
    if num == N-1:
        oper_ans.append(num_list[num])
        stack = []
        for i in range(2*N-1):
            stack.append(oper_ans[i])
            if len(stack) == 3:
                if stack[1] == "+":
                    stack = [stack[0] + stack[2]]
                elif stack[1] == "-":
                    stack = [stack[0] - stack[2]]
                elif stack[1] == "/":
                    stack = [int(stack[0] / stack[2])]
                elif stack[1] == "*":
                    stack = [stack[0] * stack[2]]
        value = int(stack[-1])
        if value < min_num:
            min_num = value
        
        if value > max_num:
            max_num = value
        oper_ans.pop()
        return
    else:
        oper_ans.append(num_list[num])
        for i in ["+", "-", "*", "/"]:
            if oper_dict[i] != 0:
                oper_ans.append(i)
                oper_dict[i] -= 1
                find_num(num+1)
                oper_dict[i] += 1
                oper_ans.pop()
        oper_ans.pop()
                
            
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    min_num = 10**9
    max_num = -(10**9)
    oper_cnt = list(map(int,input().split()))
    oper_dict = {
        "+" : oper_cnt[0],
        "-" : oper_cnt[1],
        "*" : oper_cnt[2],
        "/" : oper_cnt[3],
    }
    num_list = list(map(int,input().split()))
    oper_ans = []
    find_num(0)
    print(f"#{tc} {max_num - min_num}")

