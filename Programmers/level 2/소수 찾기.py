primeN = []

def solution(numbers):
    global primeN
    global s

    s = set()

    numbers = sorted(list(numbers), reverse=True)

    n = int(''.join(numbers))

    primeN = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if primeN[i]:
            for j in range(i*2, n+1, i):
                primeN[j] = False


    for i in range(len(numbers)):
        t = numbers.copy()
        t.remove(numbers[i])

        bt(numbers[i], t)


    return len(s)


def bt(arr, rest):
    global primeN
    global s

    n = int(''.join(arr))

    if primeN[n]:
        s.add(n)

    for i in range(len(rest)):
        t = rest.copy()
        t.remove(rest[i])
        
        bt(arr + rest[i], t)

if __name__ == "__main__":
    print(solution('17'))
    print(solution('011'))
