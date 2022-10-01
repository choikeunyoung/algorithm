N, M = map(int, input().split())

castle = [input() for _ in range(N)]
# print(castle)

# 추가 경비원이 필요한 행의 수를 저장
add_row = 0
# 추가 경비원이 필요한 열의 개수를 저장하는 리스트
add_col = [0] * M
print(add_row, add_col)

for r in range(len(castle)):
    print(castle[r])
    if 'X' not in castle[r]:
        add_row += 1 # 아마 이부분에서 오류가 날거같다고 생각이드네요
        
    for c in range(len(castle[0])):

        var = castle[r][c]
        print(var)
        if var == 'X':
            add_col[c] += 1 # 잘 구현하신거 같은데 개인적인 생각으론 이제 여기에서 X가 있으면 더이상 탐색을 안해도되서 break 걸어줘도 될거같다고 생각이듭니다
            #
print(add_row,add_col)
if add_row == 0:
    print(add_col.count(0))
else:
    print(add_row)