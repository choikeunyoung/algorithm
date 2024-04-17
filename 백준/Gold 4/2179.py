import sys

input = sys.stdin.readline

N = int(input())

word_list = []

for _ in range(N):
    word_list.append(input())

word_list.sort()