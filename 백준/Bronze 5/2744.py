word = input()
result = ""

for i in word:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()
print(result)