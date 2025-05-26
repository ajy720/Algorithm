from math import sqrt

if __name__ == "__main__":
    while True:
        n = int(input())

        if n == -1:
            break

        res = set()

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                res.add(i)
                res.add(n // i)

        res = sorted(list(res))

        if n == sum(res) - n:
            print(n, "=", ' + '.join(map(str, res[:-1])) )
        else:
            print(n, "is NOT perfect.")