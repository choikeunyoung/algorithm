char = input()

for i in char:
    if i in 'CAMBRIDGE':
        char = char.replace(i,"")
print(char)