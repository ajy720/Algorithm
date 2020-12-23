def solution(board, moves):
    answer = 0
    n = len(board)
    arr = []

    for pos in moves:
        pos -= 1
        for i in range(n):
            if board[i][pos]:
                arr.append(board[i][pos])
                board[i][pos] = 0
                break

    while 1:
        flag = True
        i = 0
        while i < len(arr) - 1:
            if arr[i] == arr[i+1]:
                answer += 2
                arr[i:i+2] = []
                flag = False

            i += 1

        if flag:
            break

    return answer


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]
    ]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]

    ans = solution(board, moves)

    print(ans)
