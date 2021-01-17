def solution(clothes):
    answer = 1
    d = dict()

    for cloth, cat in clothes:
        if cat in d.keys():
            d[cat] += 1
        else:
            d[cat] = 2

    for i in d.values():
        answer *= i

    return answer - 1


if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"],
               ["blue_sunglasses", "eyewear"],
               ["green_turban", "headgear"]]
    print(solution(clothes))

    clothes = [["crow_mask", "face"],
               ["blue_sunglasses", "face"],
               ["smoky_makeup", "face"]]
    print(solution(clothes))
