import sys

for i in range(int(sys.stdin.readline())):
    r,e,c = map(int,sys.stdin.readline().split())
    if e - c > r:
        print('advertise')
    elif e - c < r:
        print('do not advertise')
    else:
        print('does not matter')