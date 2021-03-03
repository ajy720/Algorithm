from collections import deque

px = [0, -1, 1, 0]
py = [-1, 0, 0, 1]


def solution(maps):
    answer = -1

    n = len(maps)
    m = len(maps[0])

    q = deque([(0, 0, 1)])
    maps[0][0] = 0

    while q:
        x, y, d = q.popleft()

        if x == n-1 and y == m-1:
            answer = d

        for i in range(4):
            ox = x + px[i]
            oy = y + py[i]

            if 0 <= ox < n and 0 <= oy < m and maps[ox][oy]:
                q.append((ox, oy, d+1))
                maps[ox][oy] = 0

    return answer


if __name__ == "__main__":
    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 1]]))

    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1]]))
