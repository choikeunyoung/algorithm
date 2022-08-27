import sys

while True:
    sent = sys.stdin.readline()
    s_cnt = 0
    b_cnt = 0
    flag = 0
    if sent == '.':
        break
    else:
        for j in sent:
            if j =='(':
                s_cnt += 1
            elif j == '[':
                b_cnt += 1
            elif j == ']' and b_cnt != 0:
                b_cnt -= 1
            elif j == ']' and b_cnt == 0:
                print('no')
                break
            elif j == ')' and s_cnt != 0:
                s_cnt -= 1
            elif j == ')' and s_cnt == 0:
                print('no')
                break
    if s_cnt == 0 and b_cnt == 0:
        print('yes')
