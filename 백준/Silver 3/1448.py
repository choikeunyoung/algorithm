import sys
# input 값이 많으므로 sys 사용
input = sys.stdin.readline

N = int(input())
# input 값을 담을  리스트
num_list = []

for _ in range(N):
    num_list.append(int(input()))
# 내림차순 정렬
num_list.sort(reverse=True)
# N-2 값까지 반복문 시행
for i in range(N-2):
    # 삼각형의 제일 긴 변의 길이가 다른 두변의 합보다 작아야 삼각형이 된다.
    if num_list[i] < num_list[i+1] + num_list[i+2]:
        print(num_list[i]+num_list[i+1]+num_list[i+2])
        break
# 그 외의 경우 -1 출력
else:
    print(-1)