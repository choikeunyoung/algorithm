import sys

sys.stdin = open('input.txt', 'r')

t = int(sys.stdin.readline())

s = [1]
for i in range (1, t+1):
    s.append(2**(i))
    
print(s)


# t = int(input())

# s = [1]
# for i in range (1, t+1):
#     s.append(2**(i))
    
# for j in s:    
# 	print(j, end=' ')