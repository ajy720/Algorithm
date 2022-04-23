from collections import deque
from bisect import bisect_left


def solution(begin:str, target:str, words:list):
    answer = 0
    n = len(begin)

    q = deque([begin])

    while q:
        q.popleft()

        for i in range(n):
            pass
            


    return answer


if __name__ == '__main__':
    pass