N = int(input())
people_dict={}
for i in range(1,N+1):
    people = list(map(str,input().split()))
    if people[1] == "enter":
        people_dict[people[0]] = people[1]
    else:
        if people_dict[people[0]]:
            del people_dict[people[0]]

for k in sorted(people_dict.keys(),reverse=True):
    print(k)