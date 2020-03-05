import sys
from collections import deque

input = sys.stdin.readline

q = deque([])

if __name__ == "__main__":
    q = deque()

    for _ in range(int(input())):
        oper = input().rstrip("\n")
        try: oper, param = oper.split()
        except: pass

        if oper == "push": q.append(int(param))
        elif oper == "pop": print(q.popleft() if q else -1)
        elif oper == "size": print(len(q))
        elif oper == "empty": print(0 if q else 1)
        elif oper == "front": print(q[0] if q else -1)
        elif oper == "back": print(q[-1] if q else -1)
        elif oper == "exit": break