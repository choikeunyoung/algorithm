import sys
import heapq

input = sys.stdin.readline

def eratos():
    limit = 5000000
    prime_check = [True] * limit
    prime_check[0], prime_check[1] = False, False

    for i in range(2,int(limit**0.5)+1):
        if prime_check[i]:
            for j in range(i*2,limit,i):
                prime_check[j] = False

    return [num for num in range(limit) if prime_check[num]]

check = set(eratos())
use = set()
user_prime = [[],[]]

N = int(input())

point = [0,0] # 0번 대웅이 1번 규성이


for _ in range(N):
    dae, gyu = map(int,input().split())
    current_num = [dae, gyu]

    for i in range(2):
        number = current_num[i]
        idx = 1 - i

        if number in check:
            if number in use:
                point[i] -= 1000
            else:
                use.add(number)
                heapq.heappush(user_prime[i],number)
                if len(user_prime[i]) > 3:
                    heapq.heappop(user_prime[i])
        else:
            if len(user_prime[idx]) < 3:
                point[idx] += 1000
            else:
                point[idx] += sorted(user_prime[idx])[-3]

if point[0] > point[1]:
    print("소수의 신 갓대웅")
elif point[0] < point[1]:
    print("소수 마스터 갓규성")
else:
    print("우열을 가릴 수 없음")
