import sys
input = sys.stdin.readline
# 인풋 단어 두개
S = input().strip()
T = input().strip()
# 타겟이 되는 단어 길이가 원하는 단어보다 길이가 작아질때까지
while len(T) > len(S):
    # 타겟 단어의 끝이 A 인 경우 끝 단어 자르기
    if T[-1] == 'A':
        T = T[:-1]
    # 타겟 단어의 끝이 B인 경우 뒤집고 B를 제거한 후 다시 뒤집는다
    else:
        T = T[:-1][::-1]
# 반복문 탈출 후 T랑 S가 같으면 1 없으면 0
if T == S:
    print(1)
else:
    print(0)