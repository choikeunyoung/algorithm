N = int(input())
# 첫 경기 값들
first = list(map(int,input().split()))
# 둘째 경기 값들
second = list(map(int,input().split()))
# 첫 경기 합
first_max = 0
# 둘째 경기 합
second_max = 0
# 첫 경기합 절대값
for i in first:
    first_max += abs(i)
# 둘째 경기합 절대값
for i in second:
    second_max += abs(i)
# 두 경기합 더하기
print(first_max + second_max)