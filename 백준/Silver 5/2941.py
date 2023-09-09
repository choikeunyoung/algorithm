alpabet = ["lj", "z=", "s=", "nj", "c=", "c-", "d-", "dz="]

sentence = list(input())
checklist = []
j_index = 0
z_index = 0
for i in range(len(sentence)):
    a = sentence[i]
    # if a == "c" or a == "s" or a == "z":
    if a == "c" or a == "s":
        if sentence[i + 1] == "=":
            checklist.append(a + "=")
    elif a == "z":
        if z_index != i:
            if sentence[i + 1] == "=":
                checklist.append(a + "=")
    # elif a == "c" or a == "d":
    elif a == "c":
        if sentence[i + 1] == "-":
            checklist.append(a + "-")

    elif a == "d":
        if sentence[i + 1] == "z" and sentence[i + 2] == "=":
            checklist.append("dz=")
            z_index = i + 1
        elif sentence[i + 1] == "-":
            checklist.append("d-")
        else:
            checklist.append(a)

    elif a == "l" or a == "n":
        if sentence[i + 1] == "j":
            checklist.append(a + "j")
            j_index = i + 1
        else:
            checklist.append(a)

    elif a != "=":
        if a == "j":
            if i != j_index:
                checklist.append(a)
        else:
            checklist.append(a)

# print(checklist)
print(len(checklist))
