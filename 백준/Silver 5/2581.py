def prime(n,m):
    # 문제에서 주어진 Input 값의 범위가 10000이기 때문에 list 크기를 10001 로 설정해준다.
    # list의 Index 값은 0 부터 시작하기 때문에 10001개로 설정
    prime_list = [False, False] + [True]*10**4
    # 소수를 판단 후 범위 내의 소수값들만 리턴해줄 리스트 생성
    num_list = []
    for i in range(1,10001): # 반복문을 10000번 시행 => 실제로는 10000**0.5 번정도만 실행하는것으로 해결가능함. 시간절약을 위해서
        if prime_list[i]: # if prime_list[i]: 는 if prime_list == True 랑 같은 말이지만 ==연산자를 사용하지 않기 때문에 시간 복잡도가 좀 더 줄어든다. (읽은 기억이 있음)
            for j in range(i*2,10001,i): # 반복문을 i 값이 아닌 i*2 부터 시행하는데 10000번째 까지 돌리고 증가하는 연산자 값을 i 로 설정함. => ex) i 값이 3인 경우 3을 제외한 6,9,12,15 등등으로 소수가 아닌 값들을 쳐내는 과정
                prime_list[j] = False
    
    # 소수를 판단했으면 이제 n,m 값을 통해서 넘겨줄 값들을 리스트로 append 해줌
    for x in range(n,m+1):
        if prime_list[x]:
            num_list.append(x)

    return num_list

n = int(input())
m = int(input())
prime_num = prime(n,m)
# 리스트로 넘겨준 이유는 값의 합을 구하기 때문에 sum 함수를 사용해주기 위해서 리스트로 받아왔다.
# 또한 리스트의 0번 인덱스 값이 최솟값을 나타내기 때문에 출력은 sum 과 0 번인덱스틀 이용하여 출력해줌.
if not len(prime_num):
    print(-1)
else:
    print(sum(prime_num))
    print(prime_num[0])