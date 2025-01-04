import sys

input = sys.stdin.readline

N = int(input())

type_list = []
undo_list = []

for _ in range(N):
    types, title, time = list(map(str,input().split()))

    if types == "undo":
        undo_list.append