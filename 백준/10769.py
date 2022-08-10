char = input()

smile = char.count(":-)")
sad = char.count(":-(")

if smile > sad:
    print('happy')
elif smile < sad:
    print('sad')
elif smile == 0 and sad == 0:
    print('none')
else:
    print('unsure')