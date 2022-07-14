# > 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# **max() 함수 사용 금지**
# > 

# ### Input

# ```python
# numbers = [0, 20, 100]
# ```

# 아래의 테스트 케이스로도 확인 해보세요.

# ```python
# numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -30
# ```

# ### Output

# ```
# 20
# ```

numbers = [0, 20, 100]
numbers = list(set(numbers))
a=numbers[0]
for i in numbers:
    if i>a:
        a=i
    else:
        a=a
print(a)
numbers.remove(a)
b=numbers[0]
for j in numbers:
    if j>b:
        b=j
    else:
        b=b

print(b)