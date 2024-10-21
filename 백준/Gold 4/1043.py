import sys

input = sys.stdin.readline

N,M = map(int,input().split())

true_person = list(map(int,input().split()))

if true_person[0] != 0:
    cnt = 0
    next_person = true_person[1:]
    next_party = []
    for _ in range(M):
        party_info = list(map(int,input().split()))
        for i in next_person:
            if i in party_info[1:]:
                for k in party_info[1:]:
                    if k != i:
                        next_person.append(k)
                break
        else:
            next_party.append(party_info)
    while next_person:
        next = next_person.pop()
        for i in next_party:
            if next in i[1:]:
                
else:
    for _ in range(M):
        party_info = list(map(int,input().split()))
    print(M)    
