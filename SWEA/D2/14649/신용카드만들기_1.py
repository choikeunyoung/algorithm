import sys

sys.stdin = open("./input.txt","r")

T = int(sys.stdin.readline())
# input 파일 읽어오기
for i in range(1,T+1): # Test case 개수만큼 반복
    sum_ = 0
    num_list = list(map(int,sys.stdin.readline().split())) #input 파일에서 읽어온 문장 리스트로 생성
    for j in range(1,len(num_list)+1): # 1~15까지 반복
        if j % 2 == 0: # 짝수일때 조건 (그냥 더하기)
            sum_ += num_list[j-1]
        else: # 홀수일때 조건 (2곱해서 더하기)
            sum_ += (num_list[j-1]*2)
    if sum_ % 10 == 0: # 다 더한값이 10으로 나누어 떨어질 경우 마지막 자리수 값은 0
        print(f"#{i}", 0)
    else: # 다 더한값이 10으로 떨어지지 않을 경우 그 차를 마지막 자리수로 배치
        print(f"#{i}", 10*(sum_//10+1) - sum_)
