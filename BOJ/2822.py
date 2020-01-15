import sys

score = []
for _ in range(8):
    score.append(int(input()))

cont = sorted(score)[3:]

print(sum(sorted(score)[3:]))
for index, s in enumerate(score):
    if s in cont:
        print(index+1, end=" ")