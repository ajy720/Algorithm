def solution(phone_book):
    answer = True

    n = len(phone_book)

    phone_book.sort()

    for i in range(n):
        m = len(phone_book[i]) 
        for j in range(i+1, n):
            k = len(phone_book[j]) 

            if k < m: 
                break
                
            if phone_book[j][:m] == phone_book[i]:
                return False

    return answer

if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]
    print(solution(phone_book))

    phone_book = ["123","456","789"]	
    print(solution(phone_book))

    phone_book = ["12","123","1235","567","88"]
    print(solution(phone_book))