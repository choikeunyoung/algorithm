def hanoi(N, from_pos, to_pos, other_pos):
    global cnt
    cnt += 1
    if N == 1:
        print(from_pos, to_pos)
    else:
        hanoi(N-1, from_pos, other_pos, to_pos)
        print(from_pos, to_pos)
        hanoi(N-1, other_pos, to_pos, from_pos)

N = int(input())
cnt = (2**N)-1
print(cnt)
if N <= 20:
    hanoi(N,1,3,2)
