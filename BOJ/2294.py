from collections import deque

def bfs():

    while len(dq):
        v = dq.popleft()

        for i in arr:
            if not chk[v+i] and v + i < k:
                dq.append(v+i)
                chk[v+i] = chk[v] + 1
            elif v + i== k:
                print(chk[v] + 1)
                return
            elif v + i > k:
                break
    
    print(-1)

if __name__ == "__main__":
    chk = [0] * 100000
    n, k = map(int, input().split())

    arr = []
    for i in " "*n:
        arr.append(int(input()))
        chk[arr[-1]] = 1

    arr = sorted(set(arr))

    dq = deque(arr)

    bfs()