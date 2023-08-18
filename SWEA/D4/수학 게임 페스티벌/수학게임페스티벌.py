from collections import deque

def Double(num):
    num *= 2
    if num >= 10000:
        return num % 10000
    else:
        return num

def Subtrack(num):
    if num == 0:
        return 9999
    else:
        return num - 1

def Left_Rotate(num):
    num = str(num)
    num = deque(map(str,num))
    if len(num) < 4:
        for _ in range(4-len(num)):
            num.appendleft("0")
    num.rotate(-1)
    num = int("".join(num))
    return num
    
def Right_Rotate(num):
    num = str(num)
    num = deque(map(str,num))
    if len(num) < 4:
        for _ in range(4-len(num)):
            num.appendleft("0")
    num.rotate(1)
    num = int("".join(num))
    return num


def BFS(start,target):
    queue = []
    queue.append(start)
    while queue:
        check = queue.pop(0)
        dobule_num = Double(check)
        subtrack_num = Subtrack(check)
        left_num = Left_Rotate(check)
        right_num = Right_Rotate(check)
        if not ans_list[dobule_num]:
            ans_list[dobule_num] = ans_list[check] + "D"
            queue.append(dobule_num)
        if not ans_list[subtrack_num]:
            ans_list[subtrack_num] = ans_list[check] + "S"
            queue.append(subtrack_num)
        if not ans_list[left_num]:
            ans_list[left_num] = ans_list[check] + "L"
            queue.append(left_num)
        if not ans_list[right_num]:
            ans_list[right_num] = ans_list[check] + "R"
            queue.append(right_num)
            
        if dobule_num == target:
            print(ans_list[dobule_num])
            break
        elif subtrack_num == target:
            print(ans_list[subtrack_num])
            break
        elif left_num == target:
            print(ans_list[left_num])
            break
        elif right_num == target:
            print(ans_list[right_num])
            break
            
N = int(input())

for _ in range(N):
    problem, answer = map(int,input().split())
    ans_list = ["" for _ in range(10000)]
    BFS(problem,answer)