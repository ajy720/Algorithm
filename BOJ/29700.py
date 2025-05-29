if __name__ == "__main__":
    n, m, k = map(int, input().split())

    print(
        sum(
            [
                sum([len(part) - k + 1 for part in line.split("1") if len(part) >= k])
                for line in [input() for _ in range(n)]
            ]
        )
    )
