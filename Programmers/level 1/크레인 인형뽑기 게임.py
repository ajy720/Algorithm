def solution(board, moves):
    answer = 0
    n = len(board)
    arr = []

    for pos in moves:
        pos -= 1

        for i in range(n):
            pick = board[i][pos]

            if pick:
                board[i][pos] = 0

                if arr and arr[-1] == pick:
                    arr.pop(-1)
                    answer += 2

                else:
                    arr.append(pick)
            
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
