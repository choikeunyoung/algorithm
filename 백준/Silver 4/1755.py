N,M = map(int,input().split())

ans_list = []

num_list = []

for i in range(N,M+1):
    num_list.append(str(i))

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

for i in num_list:
    check_list = []
    for j in i:
        check_list.append(num_dict[j])
    ans_list.append(check_list)
ans_list.sort(key=lambda x:x[:])
cnt = 1
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