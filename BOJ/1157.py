s = input().upper()

alphaDict = dict()

for ch in s:
    if alphaDict.get(ch, 0) == 0:
        alphaDict.setdefault(ch, 1)
    else:
        alphaDict.update([[ch, alphaDict.get(ch)+1]])

alphaDict = list(alphaDict.items())

maxIndex = maxCount = 0

for i in range(1, len(alphaDict)):
    if alphaDict[maxIndex][1] < alphaDict[i][1]:
        maxIndex = i
        maxCount = 0
    elif alphaDict[maxIndex][1] == alphaDict[i][1]:
        maxCount += 1
    
if maxCount > 0:
    print('?')
else:
    print(alphaDict[maxIndex][0])
