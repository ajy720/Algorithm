c = int(input())
avg = temp = 0
for i in range(c):
    score = map(int, input().split())
    score = list(score)
    avg = sum(score[1:])/score[0]
    for j in score[1:]:
        if j > avg:
            temp += 1
    print("%0.3f%%"%(temp/score[0]*100))
    temp = 0