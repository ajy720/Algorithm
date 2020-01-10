n = int(input())

temp = index = 0
for i in range(1, n+1):
    for j, value in enumerate(str(i)): # 인덱스와 값을 한번에 가져온다
        index+=1 # 자릿수를 계산
        temp = (temp * 10) + int(value) # 일종의 힙이라고 생각하자. 있던 것들을 한칸씩 밀고 뒤에다 한자리 추가.
        if len(str(temp)) > len(str(n)): # 구하고 싶은 값보다 자리수가 많아지면 
            temp %= 10**len(str(n)) # 앞에 한 자리 OUT
        
        if temp == n:
            print(index - len(str(n)) +1)
            exit()