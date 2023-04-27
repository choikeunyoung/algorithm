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
    # 9가 들어왔을때 9를 6으로 변경이 가능하므로 둘중 큰 값을 체크해주면된다.
    if i == "9":
        if num_dict["6"] < num_dict["9"]:
            num_dict["6"] += 1
        elif num_dict["6"] >= num_dict["9"]:
            num_dict["9"] += 1
    # 마찬가지로 6이 들어왔을때 6도 9로 변경이 가능하므로 둘중 큰 값을 체크해주면 된다.
    elif i == "6":
        if num_dict["6"] > num_dict["9"]:
            num_dict["9"] += 1
        elif num_dict["6"] <= num_dict["9"]:
            num_dict["6"] += 1
    else:
        num_dict[i] += 1
# 제일 큰값에 따라서 몇세트를 사용해야할지 결정된다.
print(max(num_dict.values()))