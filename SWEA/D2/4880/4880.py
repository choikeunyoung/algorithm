# def winner(group, tc):
#     group_length = len(group)
#     if group_length == 1:
#         print(f"#{tc} {group[0][-1]+1}")
#     else:
#         new_list = []
#         if group_length % 2 == 0:
#             for i in range(0, group_length, 2):
#                 if group[i][0] == 1:
#                     if group[i+1][0] == 1:
#                         new_list.append(group[i])
#                     elif group[i+1][0] == 2:
#                         new_list.append(group[i+1])
#                     elif group[i+1][0] == 3:
#                         new_list.append(group[i])
#                 elif group[i][0] == 2:
#                     if group[i+1][0] == 1:
#                         new_list.append(group[i])
#                     elif group[i+1][0] == 2:
#                         new_list.append(group[i])
#                     elif group[i+1][0] == 3:
#                         new_list.append(group[i+1])
#                 elif group[i][0] == 3:
#                     if group[i+1][0] == 1:
#                         new_list.append(group[i+1])
#                     elif group[i+1][0] == 2:
#                         new_list.append(group[i])
#                     elif group[i+1][0] == 3:
#                         new_list.append(group[i])
#         else:
#             group_length -= 1
#             for i in range(0, group_length, 2):
#                 if group[i][0] == 1:
#                     if group[i+1][0] == 1:
#                         new_list.append(group[i])
#                     elif group[i+1][0] == 2:
#                         new_list.append(group[i+1])
#                     elif group[i+1][0] == 3:
#                         new_list.append(group[i])
#                 elif group[i][0] == 2:
#                     if group[i+1][0] == 1:
#                         new_list.append(group[i])
#                     elif group[i+1][0] == 2:
#                         new_list.append(group[i])
#                     elif group[i+1][0] == 3:
#                         new_list.append(group[i+1])
#                 elif group[i][0] == 3:
#                     if group[i+1][0] == 1:
#                         new_list.append(group[i+1])
#                     elif group[i+1][0] == 2:
#                         new_list.append(group[i])
#                     elif group[i+1][0] == 3:
#                         new_list.append(group[i])
#             new_list.append(group[-1])
#         winner(new_list, tc)


def win(x,y):
    if group_list[x] - group_list[y] == 0:
        return x
    elif group_list[x] - group_list[y] == 1 or group_list[x] - group_list[y] == -2:
        return x
    return y

def group(start, end):
    if start == end:
        return start
    left = group(start, (start + end) // 2)
    right = group((start + end) // 2 + 1, end)
    return win(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    group_list = list(map(int,input().split()))
    result = group(0, N-1) + 1
    print(f"#{tc} {result}")