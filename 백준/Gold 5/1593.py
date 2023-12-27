g, s = map(int,input().split())
# 찾을 단어
find_word = input()
# 비교할 단어
search_list = input()
# 아스키 코드로 찾을 단어를 체크
current_list = [0] * 58
# 비교할 단어들의 아스키 코드값을 체크할 리스트
check_list = [0] * 58
# 순열이 몇개 존재하는지 체크할 변수
cnt = 0
# 시작 값
start = 0
# 길이를 체크할 변수
check_length = 0
# 찾을 단어의 아스키 값을 리스트에 저장
for i in find_word:
    current_list[ord(i)-65] += 1
# 비교할 단어를 반복문을 돌며 아스키 코드 값 체크
for i in search_list:
    check_list[ord(i)-65] += 1
    # 아스키 코드값을 넣어준 후 길이를 +1 해줌
    check_length += 1
    # 만약 길이가 비교할 단어와 같은경우
    if check_length == g:
        # 두 리스트가 동일하면 cnt 증가
        if check_list == current_list:
            cnt += 1
        # 비교를 진행하였으니 앞의 값의 아스키 코드를 -1 해줌
        check_list[ord(search_list[start])-65] -= 1
        # start 부분을 1씩 증가 후 길이는 -1
        start += 1
        check_length -= 1

print(cnt)