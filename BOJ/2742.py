import sys

input = sys.stdin.readline

n = int(input())

for i in reversed(range(n)):
    print(i+1)