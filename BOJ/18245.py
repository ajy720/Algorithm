import sys

input = sys.stdin.readline

arr = []

while 1:
    temp = input().strip("\n")
    if temp == "Was it a cat I saw?": break
    arr.append(temp)

for i in range(0, len(arr)):
    for j in range(0, len(arr[i]), i+2):
        print(arr[i][j], end="")
    print()