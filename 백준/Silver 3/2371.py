N = int(input())

file_lengths = []
for _ in range(N):
    num_list = list(map(int, input().split()))
    num_length = len(num_list)
    file_lengths.append(num_list)

max_length = max(map(len, file_lengths))
min_k = float('inf')

for K in range(1, max_length + 1):
    unique_sequences = set()

    for file in file_lengths:
        if K > len(file):
            unique_sequences.add(tuple(file + [0] * (K - len(file))))
        else:
            unique_sequences.add(tuple(file[:K]))

    if len(unique_sequences) == N:
        min_k = K
        break

print(min_k)