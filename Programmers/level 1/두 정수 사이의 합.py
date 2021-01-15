def solution(a, b):
    if a < b:
        a, b = b, a
        
    return (a+b)*(a-b+1)//2

if __name__ == "__main__":
    pass