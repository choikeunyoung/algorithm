import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())

for k in range(1,T+1):
    x = sys.stdin.readline()
    x = x.strip()
    a = []
    b = []
    cnt = 0
    for i in range(0,len(x)):
        a.append(x[i])
        cnt+=1
    for j in range(cnt-1,-1,-1):
        b.append(x[j])
    a = ''.join(a)
    b = ''.join(b)
    if a == b:
        print(f'#{k}', '1')
    else:
        print(f'#{k}', '0')



# T = int(input())

# for k in range(1,T+1):
#     x = input()
#     x = x.strip()
#     a = []
#     b = []
#     cnt = 0
#     for i in range(0,len(x)):
#         a.append(x[i])
#         cnt+=1
#     for j in range(cnt-1,-1,-1):
#         b.append(x[j])
#     a = ''.join(a)
#     b = ''.join(b)
#     if a == b:
#         print(f'#{k}', '1')
#     else:
#         print(f'#{k}', '0')