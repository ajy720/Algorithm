def solution(works, n):
    answer = 0

    d = dict()
    d[0] = 0

    for i in works:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    works = sorted(d.keys(), reverse=True)

    for i in range(len(works)-1):
        t = d[works[i]]

        if (works[i] - works[i+1]) * d[works[i]] > n:
            i -= 1
            break

        n -= (works[i] - works[i+1]) * d[works[i]]
        d[works[i+1]] += d[works[i]]  
        del(d[works[i]])

    i += 1
    nextHeight = works[i] - n // d[works[i]]
    n -= t * (n // t)



    if nextHeight != works[i]:
        d[nextHeight] = d[works[i]]
        del(d[works[i]])

    d[nextHeight] -= n
    if nextHeight-1 in d:
        d[nextHeight-1] += n   
    else:
        d[nextHeight-1] = n   


        

    for key in d:
        if key < 0:
            continue
        
        answer += d[key] * (key**2)
        
    return answer


if __name__ == "__main__":
    # print(solution([4, 3, 3], 4))
    # print(solution([2, 1, 2], 1))
    print(solution([1,1], 3))