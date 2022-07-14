# > 문자열 word가 주어질 때, 해당 문자열에서 `a` 가 처음으로 등장하는 위치(index)를 출력해주세요.
# `a` 가 없는 경우에는 `-1`을 출력해주세요.
# `**find()` `index()` 메서드 사용 금지**
# > 

# ### Input

# ```
# banana
# ```

# ### Output

# ```python
# 1
# ```

# 아래의 테스트 케이스로도 확인 해보세요.

# ```python
# apple # 0
# kiwi # -1
# ```

word = input()

for i in range(0,len(word)):
    if word[i]=="a":
        print(i)
        break

if "a" not in word:
    print(-1)