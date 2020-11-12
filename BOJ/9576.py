import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(i):
    for j in range(arr[i][0], arr[i][1]+1):
        # 만약 j번째 책을 받은 사람이 없다면
        if books[j] == -1:
            # j번째 책을 i번째 사람에게 배정
            books[j] = i
            # j번째 책은 이미 거쳐갔으니 앞 부분 축약
            arr[i][0] += 1
            return True

        # 그렇지 않고 j번째 책을 받은 사람이 있다면 
        else:
            # j번째 책을 배정받은 사람에게
            # j+1번째 책을 배정해주고
            if solve(books[j]): 
                # i번째 사람이 j번째 책을 배정받는다
                books[j] = i
                arr[i][0] += 1
                return True
    
    return False
    

for _ in ' '*int(input()):
    n, m = map(int, input().split())

    arr = [[*map(int, input().split())] for _ in ' '*m]
    books = [-1] + [-1] * n

    ans = sum([solve(i) for i in range(m)])
    print(ans)

    del(arr, books, n, m, ans)
