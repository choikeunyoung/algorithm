# N = int(input())
# word = input()
# num_list = []
# for _ in range(N):
#     num_list.append(int(input()))

# stack = []
# num_dict = {}
# check = 0

# for i in word:
#     if i == "+":
#         A = stack.pop()
#         B = stack.pop()
#         if isinstance(A,str) and isinstance(B,str):
#             stack.append(num_dict[A]+num_dict[B])
#         elif isinstance(A,str) and isinstance(B,int):
#             stack.append(num_dict[A]+B)
#         elif isinstance(A,int) and isinstance(B,str):
#             stack.append(A+num_dict[B])
#         else:
#             stack.append(A+B)
#     elif i == "*":
#         A = stack.pop()
#         B = stack.pop()
#         if isinstance(A,str) and isinstance(B,str):
#             stack.append(num_dict[A]*num_dict[B])
#         elif isinstance(A,str) and isinstance(B,int):
#             stack.append(num_dict[A]*B)
#         elif isinstance(A,int) and isinstance(B,str):
#             stack.append(A*num_dict[B])
#         else:
#             stack.append(A*B)
#     elif i == "/":
#         A = stack.pop()
#         B = stack.pop()
#         if isinstance(A,str) and isinstance(B,str):
#             stack.append(num_dict[B]/num_dict[A])
#         elif isinstance(A,str) and isinstance(B,int):
#             stack.append(B/num_dict[A])
#         elif isinstance(A,int) and isinstance(B,str):
#             stack.append(num_dict[B]/A)
#         else:
#             stack.append(B/A)
#     elif i == "-":
#         A = stack.pop()
#         B = stack.pop()
#         if isinstance(A,str) and isinstance(B,str):
#             stack.append(num_dict[B]-num_dict[A])
#         elif isinstance(A,str) and isinstance(B,int):
#             stack.append(B-num_dict[A])
#         elif isinstance(A,int) and isinstance(B,str):
#             stack.append(num_dict[B]-A)
#         else:
#             stack.append(B-A)
#     else:
#         if i not in num_dict:
#             num_dict[i] = num_list[check]
#             check += 1
#         stack.append(i)
# print("%.2f" %stack[0])


N = int(input())
word = input()
num_list = []
for _ in range(N):
    num_list.append(int(input()))
# 스택을 이용하여 값을 저장할 리스트
stack = []
# 딕셔너리를 통한 문자와 변수 매칭
num_dict = {}
# num_list 순회할 변수
check = 0
# 만약 i 값이 연산자인 경우 아닌 경우 나눠서 행동
for i in word:
    # 연산자가 나온경우
    if i in ['+', '-', '*', '/']:
        # 뒤에서 2개의 피연산자를 뽑아서 사용
        A = stack.pop()
        B = stack.pop()
        # A,B가 각각 문자인 경우 A,B에 각각 딕셔너리의 value 값 반환
        if isinstance(A, str):
            A = num_dict[A]
        if isinstance(B, str):
            B = num_dict[B]
        # A,B가 문자가 아닌 경우 정수이므로 아래 계산식 수행
        if i == '+':
            stack.append(B + A)
        elif i == '-':
            stack.append(B - A)
        elif i == '*':
            stack.append(B * A)
        elif i == '/':
            stack.append(B / A)
    # 피연산자인 경우
    else:
        # 피연산자가 딕셔너리안에 없으면 딕셔너리에 연산자와 값을 추가
        if i not in num_dict:
            num_dict[i] = num_list[check]
            # 값을 추가했으니 num_list 를 순회할 변수 증가
            check += 1
        # stack 에 피연산자 추가
        stack.append(i)

print("%.2f" % stack[0])