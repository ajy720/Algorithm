def solution(n, arr1, arr2):
    answer = [
        ''.join([
            '#' if int(c) else ' '
            for c in eval("f'{" + str(arr1[i]) + " | " + str(arr2[i]) + ":0" + str(n) + "b}'")
        ])
        for i in range(n)
    ]

    return answer


if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    출력 = ["#####", "# # #", "### #", "# ##", "#####"]

    print(solution(n, arr1, arr2))
    print(출력)

    n = 6
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]
    출력 = ["######", "### #", "## ##", " #### ", " #####", "### # "]

    print(solution(n, arr1, arr2))
    print(출력)
