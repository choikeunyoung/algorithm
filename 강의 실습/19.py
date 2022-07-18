#양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
#양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지
x = int(input("양의 정수를 입력하세요 : "))
i = 0
while True:
    if x <= 0:
        x = int(input('양의 정수를 입력하세요 : '))
    else:
        break

while True:
    a=x//10**i
    if a ==0:
        break
    else:
        i+=1

print(i)

