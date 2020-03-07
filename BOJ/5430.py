import sys

input = sys.stdin.readline

for _ in range(int(input())):
    oper = input().rstrip("\n")
    n = int(input())
    try:
        try: arr = list(map(int, input().strip("[]\n").split(',')))
        except: arr = []
        head = 0
        tail = n
        is_reverse = False

        for o in oper:
            if o == "R": is_reverse = not is_reverse^False
            if o == "D":
                if is_reverse: tail -= 1
                else: head += 1
            
            if head > tail: raise
        
        if head == tail: print("[]")
        else:
            if is_reverse: 
                print("[", end="")
                for i in reversed(arr[head+1:tail]): print(f"{i},", end="")
                print(f"{arr[head]}", end="")
                print("]")  

            else:
                print("[", end="")
                for i in arr[head:tail-1]: print(f"{i},", end="")
                print(f"{arr[tail-1]}", end="")
                print("]")

    except:
        print("error")