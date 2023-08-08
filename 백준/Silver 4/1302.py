N = int(input())
dict = {}
for i in range(N):
    book = input()
    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1
book_list=[]
cnt = 0
for k,v in dict.items():
    if v == max(dict.values()):
        book_list.append(k)
        cnt+=1

if cnt >= 2:
    book_list.sort()
    print(book_list[0])
else:
    print(book_list[0])