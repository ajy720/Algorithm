from heapq import heappop, heappush
from collections import deque

def solution(jobs):
    answer = 0
    n = len(jobs)

    head = 0
    hq = []

    jobs.sort()
    jobs = deque(jobs)
     
    while 1:
        if hq:
            prc, req = heappop(hq)
        else:
            if jobs:
                req, prc = jobs.popleft()
                head = req      
            else:
                break
            
        head += prc
        answer += head - req

        while jobs:
            if jobs[0][0] > head:
                break

            nReq, nPrc = jobs.popleft()

            heappush(hq, (nPrc, nReq))

    return answer//n


if __name__ == "__main__":
    print(solution([[0, 3], [15, 9], [2, 6]]))
