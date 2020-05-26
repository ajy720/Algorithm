import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s1 = set()
s2 = set()
for i in " "*n:
    s1.add(input())
for i in " "*m:
    s2.add(input())

s1 = s1.intersection(s2)
print(len(s1))
for i in sorted(list(s1)):
    print(i.rstrip())