import sys

sys.stdin = open('./input.txt','r')

T = int(sys.stdin.readline())
# input 파일 불러오기

for i in range(1,T+1): # Test case 개수만큼 반복
    square = list(map(int,sys.stdin.readline().split())) # 직사각형 변의 길이 리스트 생성
    max_len = max(square) # 리스트에서 젤 큰값 찾기
    min_len = min(square) # 리스트에서 젤 작은 값 찾기
    max_count = square.count(max_len) # 큰 값의 갯수
    min_count = square.count(min_len) # 작은 값의 갯수
    if max_count < min_count: # 직사각형이 되기 위해서는 가로 끼리의 길이가 같고 세로끼리의 길이가 같기 때문에 큰 값과 작은 값의 갯수 중 더 적은 값을 가진 변이 모자라기 때문에 count 한 갯수로 비교해서 모자란 값을 출력해줌. (정사각형이 될 경우 아무 값이나 출력)
        print(f"#{i}", max_len)
    else:
        print(f"#{i}", min_len)