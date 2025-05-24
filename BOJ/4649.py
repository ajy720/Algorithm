if __name__ == "__main__":
    while True:

        s = input()

        if s == "0":
            exit()

        n, seq = s.split()
        n = int(n)

        pool = set()
        away_pool = set()
        res = 0

        for x in seq:
            if x in away_pool:
                away_pool.remove(x)
                continue

            if x not in pool:
                if len(pool) >= n:
                    away_pool.add(x)
                    res += 1
                else:
                    pool.add(x)
            else:
                pool.remove(x)

        if res:
            print(f"{res} customer(s) walked away.")
        else:
            print("All customers tanned successfully.")
