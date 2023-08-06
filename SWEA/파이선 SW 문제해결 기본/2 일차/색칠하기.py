T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 빨간색과 파란색이 들어오기 때문에 두개의 세트 선언
    red_list = set()
    blue_list = set()
    # N 만큼 반복
    for _ in range(N):
        # num_list 를 리스트로 받아서 끝의 인덱스가 1(red) 인지 2(blue) 인지 판단
        num_list = list(map(int,input().split()))
        # 만약 red면 red_list에 (num_list[0], num_list[1]) ~ (num_list[2], num_list[3]) 까지 반복문 인덱스 추가
        if num_list[-1] == 1:
            for i in range(num_list[0],num_list[2]+1):
                for j in range(num_list[1],num_list[3]+1):
                    red_list.add((i,j))
        # blue 면 blue_list에 추가
        else:
            for i in range(num_list[0],num_list[2]+1):
                for j in range(num_list[1],num_list[3]+1):
                    blue_list.add((i,j))
    # 두 set의 교집합 영역 갯수 출력
    print(f"#{tc} {len(list(red_list.intersection(blue_list)))}")