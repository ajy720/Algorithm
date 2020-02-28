def solve(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0: 
            print(i)
            return solve(n//i)

    if n == 1:
        return
    
    print(n)
    
if __name__ == "__main__":
    solve(int(input()))