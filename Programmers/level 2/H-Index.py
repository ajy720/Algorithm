from bisect import bisect_left

def solution(citations):
    answer = 0

    citations.sort()

    for i in range(citations[-1]):
        t = len(citations) - bisect_left(citations, i)
        if t >= i:
            answer = i

    return answer

if __name__ == "__main__":
    pass