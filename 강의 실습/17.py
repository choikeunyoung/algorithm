# > 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# `**.upper()`, `.swapcase()` 사용 금지**
# > 

# ### Input

# ```
# banana
# ```

# ### Output

# ```python
# BANANA
# ```

word = input()
temp = 0
for i in word:
    temp = ord(i) - 32
    print(chr(temp), end='')