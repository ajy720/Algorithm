def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    k = len(arr2)

    answer = [[0]*m for _ in ' '*n]

    for i in range(n):
        for j in range(m):
            answer[i][j] = sum([
                arr1[i][o]*arr2[o][j] for o in range(k)
            ])

    return answer


if __name__ == "__main__":
    print(solution([[1, 4],
                    [3, 2],
                    [4, 1]],
                   [[3, 3],
                    [3, 3]]),
          [[15, 15],
           [15, 15],
           [15, 15]])

    print(solution([[2, 3, 2],
                    [4, 2, 4],
                    [3, 1, 4]],
                   [[5, 4, 3],
                    [2, 4, 1],
                    [3, 1, 1]]),
          [[22, 22, 11],
           [36, 28, 18],
           [29, 20, 14]])
