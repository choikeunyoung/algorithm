def find_list(num):
    global vowel_cnt
    global consonant
    global list_length
    # 리스트 길이가 채워야 하는 조건에 맞는 경우
    if list_length == N:
        # num값이 끝값일 경우
        if num == N-1:
            # 자음, 모음 체크를 못했기 때문에 각각 체크한 후 값 증가
            if ans[-1] == "a" or ans[-1] == "e" or ans[-1] == "i" or ans[-1] == "o" or ans[-1] == "u":
                vowel_cnt += 1
            elif ans[-1] != "a" and ans[-1] != "e" and ans[-1] != "i" and ans[-1] != "o" and ans[-1] != "u":
                consonant += 1
        # 만약 모음 1개 자음 2개 이상의 경우
        if vowel_cnt >= 1 and consonant >= 2:
            # 값 출력
            print("".join(ans))
        # num값이 끝값일 경우 위에서 체크한 값 다시 뺴기 해줌
        if num == N-1:
            if ans[-1] == "a" or ans[-1] == "e" or ans[-1] == "i" or ans[-1] == "o" or ans[-1] == "u":
                vowel_cnt -= 1
            elif ans[-1] != "a" and ans[-1] != "e" and ans[-1] != "i" and ans[-1] != "o" and ans[-1] != "u":
                consonant -= 1
        return
    else:
        for i in range(num,M):
            # 자음과 모음의 갯수 체크
            if word_list[i] == "a" or word_list[i] == "e" or word_list[i] == "i" or word_list[i] == "o" or word_list[i] == "u":
                vowel_cnt += 1
            elif word_list[i] != "a" and word_list[i] != "e" and word_list[i] != "i" and word_list[i] != "o" and word_list[i] != "u":
                consonant += 1
            # 리스트에 추가
            ans.append(word_list[i])
            # 리스트 길이 증가
            list_length += 1
            # 재귀
            find_list(i+1)
            # 백트래킹
            ans.pop()
            list_length -= 1
            if word_list[i] == "a" or word_list[i] == "e" or word_list[i] == "i" or word_list[i] == "o" or word_list[i] == "u":
                vowel_cnt -= 1
            elif word_list[i] != "a" and word_list[i] != "e" and word_list[i] != "i" and word_list[i] != "o" and word_list[i] != "u":
                consonant -= 1
N, M = map(int,input().split())

word_list = list(map(str,input().split()))
# 들어온 단어 오름차순 정렬
word_list.sort()
# 단어를 출력할 리스트
ans = []
# 리스트 길이 체크
list_length = 0
# 모음 갯수
vowel_cnt = 0
# 자음 갯수
consonant = 0

find_list(0)