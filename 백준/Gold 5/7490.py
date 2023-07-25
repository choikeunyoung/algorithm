def back_tracking(num,m):
    if len(num) == m:
        

T = int(input())

for _ in range(T):
    N = int(input())
    num_list = []
    # operator_list = ["+", "-", " "]
    for i in range(1,N+1):
        num_list.append(str(i))

    # stack = []

    # for j in range(3):
    #     stack.append(num_list[0]+operator_list[j]+num_list[1])

    # for i in range(2,N):
    #     stack_length = len(stack)
    #     for j in range(stack_length):
    #         for k in range(3):
    #             stack.append(stack[j]+operator_list[k]+num_list[i])
    
    # answer_list = []

    # for i in stack:
    #     answer = 0
    #     for j in range(N):
    #         if j == '+':
    #             answer += (int(i[j-1])+int(i[j+1]))
    #         elif j == "-":
    #             answer += (int(i[j-1]))