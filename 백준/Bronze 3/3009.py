x_dict = {}
y_dict = {}
ans = ""
for _ in range(3):
# x,y에 input 값을 대입
    x, y = map(str,input().split())
# x 값이 x_dict에 존재할 경우 value 값 1 증가
    if x in x_dict:
        x_dict[x] += 1
# x 값이 x_dict에 존재하지 않을 경우 value 에 1을 넣음
    else:
        x_dict[x] = 1
# y 값이 y_dict에 존재할 경우 value 값 1 증가
    if y in y_dict:
        y_dict[y] += 1
# y 값이 y_dict에 존재하지 않을 경우 value 에 1을 넣음
    else:
        y_dict[y] = 1
# value 값이 1인 경우 key 출력
for k,v in x_dict.items():
    if v == 1:
        ans += k
        break

for k,v in y_dict.items():
    if v == 1:
        ans += " "+k
        break
print(ans)