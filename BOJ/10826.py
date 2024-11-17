def matrix_multiply(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]]  # 단위 행렬 (identity matrix)
    base = matrix

    while n > 0:
        if n & 1:  # n의 마지막 비트가 1인 경우
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        n >>= 1  # n을 오른쪽으로 1비트 이동 (즉, n을 2로 나눔)

    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    A = [[1, 1], [1, 0]]
    result_matrix = matrix_power(A, n - 1)
    return result_matrix[0][0]

n = int(input())
print(fibonacci(n))
