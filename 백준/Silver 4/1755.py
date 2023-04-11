N,M = map(int,input().split())

ans_list = []

num_list = []

for i in range(N,M+1):
    num_list.append(str(i))
# 들어온 숫자를 문자로 변경할 딕셔너리
num_dict = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}
# 문자를 다시 숫자로 변환
return_dict = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine"  : "9",
    "zero" : "0"
}
# 들어온 값의 숫자를 리스트 형태로 문자로 변형하여 저장
for i in num_list:
    check_list = []
    for j in i:
        check_list.append(num_dict[j])
    ans_list.append(check_list)
# 문자열로 정렬
ans_list.sort(key=lambda x:x[:])
# 10개 단위로 줄이바뀌므로 체크하는 변수
cnt = 1
# 정렬된 문자열을 다시 숫자로 변환하는 과정
for i in ans_list:
    answer = ""
    for j in i:
        answer += return_dict[j]
    if cnt == 10:
        print(answer)
        cnt = 1
    else:
        print(answer, end=" ")
        cnt += 1