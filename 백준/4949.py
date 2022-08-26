import sys

while True:
    sent = sys.stdin.readline()
    cnt = 0
    r_cnt = 0
    print(sent)
    if sent == '.':
        break
    else:
        for j in sent:
            if j =='(' or j == '[':
                cnt += 1
            elif j == ']' or j == ')':
                if cnt == 0:
                    r_cnt += 1
                else:
                    cnt += 1
    
    if cnt == 0 and r_cnt == 0:
        print('yes')
    else:
        print('no')