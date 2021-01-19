def solution(board):
    answer = 0

    n, m = len(board), len(board[0])
    
    for i in range(n):
        for j in range(m):
            

            if board[i][j] == 0:
                continue

            if i > 0 and j > 0:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1

            answer = max(board[i][j], answer)

    return answer**2

if __name__ == "__main__":
    board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    print(solution(board))
    
    board = [[0,0,1,1],[1,1,1,1]]
    print(solution(board))

