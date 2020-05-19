arr = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

while 1:
    p = input().split()
    if p[0] == "***": exit()

    n = int(input())
    
    for i in range(len(p)):
        try: 
            if p[i][1] == "b": p[i] = arr[arr.index(p[i][0])-1]
            elif p[i][1] == "#": p[i] = arr[arr.index(p[i][0])+1]
        except: 
            pass
        
        idx = arr.index(p[i]) + n
        if  idx >= len(arr): idx %= len(arr)
        p[i] = arr[idx]

    print(*p)