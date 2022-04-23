def solution(expression):
    answer = 0

    rank = ["*", "+", "-"]
    n = len(expression)

    for i in range(n):
        if expression[i] in "+-*":
            for j in range(i, -1, -1):
                start = j+1
                if expression[j] in "+-*":
                    break
 
            for j in range(i, n):
                end = j
                if expression[j] in "+-*":
                    break
                    
            expression[start:end] = str(eval(expression[start:end]))
            print(expression)


    return answer


if __name__ == "__main__":
    print(solution(input()))
