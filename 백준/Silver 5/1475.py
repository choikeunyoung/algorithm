N = input()
num_dict = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
}

for i in N:
    if i == "9" or i == "6":
        if num_dict["6"] < num_dict["9"]:
            num_dict["9"] -= 1
            num_dict["6"] += 1
        elif num_dict["6"] > num_dict["9"]:
            num_dict["9"] += 1
            num_dict["6"] -= 1
        else:
            num_dict[i] += 1
    else:
        num_dict[i] += 1
print(num_dict)