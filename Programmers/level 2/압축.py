def solution(msg):
    answer = []
    d = dict()

    for i in range(1, 27):
        d[chr(i+ord('A')-1)] = i

    i = 0
    while i < len(msg):
        idx = d[msg[i]]
        answer.append(idx)

        if i == len(msg) - 1:
            break
            
        msg[i:i+2]



    return answer


if __name__ == "__main__":
    pass
