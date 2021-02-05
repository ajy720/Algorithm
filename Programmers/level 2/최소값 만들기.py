def solution(a:list, b:list):
    a.sort()
    b.sort(reverse=True)

    return sum([a[i]*b[i] for i in range(len(a))])


if __name__ == "__main__":
    print(solution([1, 4, 2], [5, 4, 4]), 29)
    print(solution([1, 2], [3, 4]), 10)


