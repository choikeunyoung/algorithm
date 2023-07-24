# from itertools import permutations
# # N의 갯수
# N = int(input())
# # 1~N 까지 수를 담을 리스트
# num_list = []

# for i in range(1,N+1):
#     num_list.append(i)
# # N개의 갯수만큼 순열 생성
# answer = list(permutations(num_list,N))

# for j in answer:
#     print(*j)


authors = ['작자 미상', '이항복', '임제', '임제', 
           '조성기', '조성기', '조성기', '임제', 
           '허균', '허균', '허균', '임제', '임제', 
           '임제', '임제', '임제', '임제', '임제', 
           '임제', '임제', '임제', '박지원', '이항복', 
           '남영로', '남영로', '남영로', '이항복', '임제', '임제']

print(set(authors))