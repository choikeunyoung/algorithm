# > 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
# > 

# ### Input

# ```python
# apple
# ```

# ### Output

# ```
# elppa
# ```

word_list=[]
cnt=0
for i in "apple":
    word_list.append(i)
    cnt+=1

while True:
    if cnt == 0:
        break
    else:
        cnt-=1
        print(word_list[cnt],end='')