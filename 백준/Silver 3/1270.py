N = int(input())
for _ in range(N):
    # 나라와 병사들을 저장할 리스트 생성
    countries = list(map(int,input().split()))
    # 나라에 병사들이 몇명있는지 체크할 딕셔너리
    count_dict = {}
    # 1부터 ~ 끝까지가 병사들의 번호
    for i in range(1,len(countries)):
        # 만약 병사 번호가 딕셔너리에 있으면 +1 없으면 추가
        if countries[i] in count_dict:
            count_dict[countries[i]] += 1
        else:
            count_dict[countries[i]] = 1
    # 딕셔너리 value 에서 max 값을 찾아줌
    max_value = max(count_dict.values())
    # 찾은 max 값이 나라의 절반보다 크면 딕셔너리 item을 순회하며 value에 맞는 key 출력
    if max_value > countries[0]/2:
        for k,v in count_dict.items():
            if v == max_value:
                print(k)
                break
    else:
        print("SYJKGW")