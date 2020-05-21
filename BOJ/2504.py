arr = input()
s = []

try:
    for i in range(len(arr)):
        if arr[i] == "(": s.append(arr[i])
        elif arr[i] == "[": s.append(arr[i])

        elif arr[i] == ")":
            a = 0
            while 1:
                t = s.pop()
                if type(t) == int: 
                    a += t
                elif t == "(":
                    s.append(2 if a == 0 else a*2)
                    break
                else: raise

        elif arr[i] == "]":
            a = 0
            while 1:
                t = s.pop()
                if type(t) == int:
                    a += t
                elif t == "[":
                    s.append(3 if a == 0 else a*3)
                    break
                else: raise
            
    print(sum(s))
except:
    print(0)