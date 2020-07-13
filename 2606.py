from collections import deque


ans = 0
def bfs():
    global ans

    q.append(1)
    chk[1] = False

    while len(q):
        t = q.popleft()

        ans += 1

        for i in arr[t]:
            if chk[i]:
                q.append(i)
                chk[i] = False


if __name__ == "__main__":
    n = int(input())
    arr = [[] for i in ' '*(n+1)]
    chk = [True] * (n+1)
    q = deque()

    for i in range(int(input())):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    bfs()

    print(ans-1)
