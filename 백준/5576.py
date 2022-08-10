w = [int(input()) for _ in range(10)]
k = [int(input()) for __ in range(10)]

w_sum = 0
k_sum = 0
k.sort()
w.sort()
for ___ in range(3):
    w_sum += w.pop()
    k_sum += k.pop()

print(w_sum, k_sum)