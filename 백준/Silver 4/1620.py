import sys

input = sys.stdin.readline

N, M = map(int,input().split())

word_dict = {}
value_dict = {}
# 인풋 문자열 공백제거
for i in range(N):
    check = input().strip()
    # 대응되는 인덱스값 추가
    word_dict[check] = i
# key, value 값 추출
for k,v in word_dict.items():
    # value 값에 word 값 대입
    value_dict[v] = k
# 인풋값 공백제거 후 대응되는 값 출력
for j in range(M):
    ans = input().strip()
    if ans.isdigit():
        print(value_dict[int(ans)-1])
    else:
        print(word_dict[ans]+1)