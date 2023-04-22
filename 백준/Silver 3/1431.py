N = int(input())

word_list = []

for _ in range(N):
    word_list.append(input())

# 0번 인덱스부터 N-1 까지 반복문을 통한 정렬
for i in range(N-1):
    for j in range(i+1,N):
        # 일단 우선 각 길이를 반환해줌
        i_length = len(word_list[i])
        j_length = len(word_list[j])
        # 길이가 다를 경우
        if i_length != j_length:
            # i가 앞의 인덱스이고 j가 뒤의 인덱스이기 때문에 i 가 더 큰경우 j 랑 바꿔준다.
            if i_length > j_length:
                temp = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = temp
        # 길이가 같은 경우
        else:
            # 값을 더해줄 변수 생성
            total_1 = 0
            total_2 = 0
            # 반복문을 순회하면서 0~9 사이 값이 있으면 더해준다.
            for k in range(i_length):
                if (word_list[i][k] >= "0" and word_list[i][k] <= "9"):
                    total_1 += int(word_list[i][k])
                if (word_list[j][k] >= "0" and word_list[j][k] <= "9"):
                    total_2 += int(word_list[j][k])
            # 더해준 값들을 비교하여 앞의 값이 큰 경우 작은 값순으로 정렬해야기 때문에 순서를 바꿔준다.
            if total_1 > total_2:
                temp = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = temp
            # 값이 같은경우 문자 순으로 정렬
            elif total_1 == total_2:
                if word_list[i] > word_list[j]:
                    temp = word_list[i]
                    word_list[i] = word_list[j]
                    word_list[j] = temp
for _ in word_list:
    print(_)