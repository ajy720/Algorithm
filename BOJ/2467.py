from sys import maxsize


if __name__ == "__main__":
    n = int(input())

    arr = [*map(int, input().split())]

    head = 0
    tail = n - 1
    m = maxsize
    m_set = (head, tail)
    while head < tail:

        if abs(arr[head] + arr[tail]) < m:
            m = abs(arr[head] + arr[tail])
            m_set = arr[head], arr[tail]
            # print(f"Min is updated: {m} ({arr[head]} + {arr[tail]})")
        if arr[head + 1] > 0:
            tail -= 1
        elif arr[tail - 1] < 0:
            head += 1
        elif abs(arr[head]) > abs(arr[tail]):
            head += 1
        else:
            tail -= 1

    m_abs = sorted(sorted(arr, key=abs)[:2])
    if abs(sum(m_abs)) < m:
        m_set = m_abs
        # print(f"Min is updated: {sum(m_abs)} ({m_set[0]} + {m_set[1]})")

    print(*m_set)
