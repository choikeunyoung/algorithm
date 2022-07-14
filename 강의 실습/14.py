# 문제 14
# > 문자열 word가 주어질 때, 해당 문자열에서 `a` 개수를 구하세요.
# **`count()` 메서드 사용 금지**
# > 

# ### Input

# ```
# apple
# ```

# ### Output

# ```
# 1
# ```

# 아래의 테스트 케이스로도 확인 해보세요.

# ```python
# banana # 3
# kiwi # 0
# ```

word = input()
cnt = 0

for i in word:
    if i == "a":
        cnt+=1

print(cnt)