# > 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# **min() 함수 사용 금지**
# > 

# ### Input

# ```python
# numbers = [0, 20, 100]
# ```

# 아래의 테스트 케이스로도 확인 해보세요.

# ```python
# numbers = [0, 20, 100, 50, -60, 50, 100] # -60
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -100
# ```

# ### Output

# ```
# 0
# ```

numbers = [-10, -100, -30]
a=numbers[0]
for i in numbers:
    if i<a:
        a=i
    else:
        a=a
print(a)