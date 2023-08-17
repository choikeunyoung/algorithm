from collections import deque

clock = deque([12, 3, 6, 9])

N = int(input())

N = (N//90)%4

for i in range(N):
    clock.rotate(1)

while clock:
    print(clock.popleft(), end=" ")
    print(clock.pop(), end=" ")