arr = [
    [1,2,3,4,5],
    [2,1,2,3,2,4,2,5],
    [3,3,1,1,2,2,4,4,5,5]
]


def solution(answers):
    answer = [0] * 3
    n = len(answers)
    
    for i in range(n):d
        for j in range(3):
            if arr[j][i%len(arr[j])] == answers[i]:
                answer[j] += 1
                
    m = max(answer)
    
    return [i+1 for i in range(3) if m == answer[i]]
        
    
    
if __name__ == '__main__':
    answers = [1,2,3,4,5]
    print(solution(answers))
    
    answers = [1,3,2,4,2]	
    print(solution(answers))