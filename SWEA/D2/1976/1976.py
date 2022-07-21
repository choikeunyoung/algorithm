import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())

for i in range(1,T+1):
    a = sys.stdin.readline()
    a = a.strip()
    b = a[:len(a)//2].split()
    c = a[len(a)//2+1:].split()
    x=[]
    for i in range(0,len(b)):
        x.append(int(b[i]) + int(c[i]))
    m = x.pop()
    h = x.pop()
    if m >= 60:
        h +=1
        m -= 60
    if h > 12:
        h -= 12
    print(h, m)


# T = int(input())

# for i in range(1,T+1):
#     a = input()
#     a = a.strip()
#     b = a[:len(a)//2].split()
#     c = a[len(a)//2+1:].split()
#     x=[]
#     for k in range(0,len(b)):
#         x.append(int(b[k]) + int(c[k]))
#     m = x.pop()
#     h = x.pop()
#     if m >= 60:
#         h +=1
#         m -= 60
#     if h > 12:
#         h -= 12
#     print(f'#{i}', h, m)