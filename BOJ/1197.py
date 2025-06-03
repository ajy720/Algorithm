from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)


def find_root(child):
    global parents

    if child == parents[child]:
        return child

    parents[child] = find_root(parents[child])

    return parents[child]


if __name__ == "__main__":
    v, e = map(int, input().split())

    parents = [i for i in range(v + 1)]

    # O(e log e)
    edges = sorted(
        [tuple(map(int, input().split())) for _ in range(e)], key=lambda x: x[2]
    )

    cost = 0

    # O(e)
    for a, b, weight in edges:
        # O(log v) * 2
        a_root = find_root(a)
        b_root = find_root(b)

        # a_root와 b_root가 같지 않다면 이어지지 않음
        if a_root != b_root:
            # a_root의 부모를 b_root의 자식으로 병합(그래프 연결)
            parents[a_root] = b_root
            cost += weight

            # print(f"Connect graph {a_root} -> {b_root}")

    # print(f"Union graph: {parents}")
    print(cost)
