import sys

while True:
    sent = sys.stdin.readline().rstrip()
    s_list = []
    s_cnt = 0
    if sent == '.':
        break
    else:
        for j in sent:
            if j =='(':
                s_list.append(j)
            elif j == '[':
                s_list.append(j)
            elif j == ']' and len(s_list) == 0:
                s_list.append(j)
            elif j == ']' and s_list[-1] != '[':
                s_list.append(j)
            elif j == ']' and s_list[-1] == '[':
                s_list.pop()
            elif j == ')' and len(s_list) == 0:
                s_list.append(j)
            elif j == ')' and s_list[-1] != '(':
                s_list.append(j)
            elif j == ')' and s_list[-1] == '(':
                s_list.pop()
    if len(s_list) == 0:
        print('yes')
    else:
        print('no')
