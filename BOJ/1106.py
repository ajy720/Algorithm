if __name__ == "__main__":
    c, n = map(int, input().split())

    items = sorted(
        [tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[1]
    )

    max_cost = items[-1][1]

    # print(items)

    dp = [0] + [10**5] * (c + max_cost)

    for i in range(1, c + 1 + max_cost):
        # print(f"i : {i}")
        for weight, cost in items:
            if cost > i:
                break
            dp[i] = min(dp[i], dp[i - cost] + weight)

    # print(dp[c:])
    print(min(dp[c:]))
