# 끝자리가 0이 되는경우는 5나 2로 나눈 경우가 된다.
# 조합모든 숫자를 구하는 것이 아닌 0이 나오는 경우를 생각하면 된다. => 구하려는 수에서 5와 2의 갯수를 세야하는 코드를 구현해야한다.
# ex n = 10 , m = 5 nCm => 10!//(10-5)!*5! => 1*2*3*4*5*6*7*8*9*10 // 5*4*3*2*1*5*4*3*2*1
# 1 * 2 * 3 * 2^2 * 5 * 2 * 3 * 7 * 2^3 * 3^2 * 2 * 5 // 5 * 2^2 * 3 * 2 * 1 * 5 *2^2 * 3 * 2 * 1
# 1 * 2^8 * 3^4 * 5^2 * 7 // 1^2 * 2^6 * 3^2 * 5^2

# min을 사용하는 이유

# 5  2 * 2 1
# 5의 2승 2의 1승
# 으로 만들어진
# 친구인데
# 0의 갯수는
# 하나잖아여?
# 그럼
# 지수로 비교한다면
# 찾은쪽 수의 갯수가
# 0의 갯수랑
# 동일하다는게
# 보여질거에요
# 그럼 다시 5의 3승 2의 2승인 125 * 4
# 500으로도



def two_cnt(num):
    cnt_two = 0
    while num:
        num //= 2
        cnt_two += num
    return cnt_two

def five_cnt(num):
    cnt_five = 0
    while num:
        num //= 5
        cnt_five += num
    return cnt_five

n,m = map(int,input().split())

print(min((two_cnt(n) - two_cnt(m) - two_cnt(n-m)),(five_cnt(n) - five_cnt(m) - five_cnt(n-m))))