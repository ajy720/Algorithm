import sys

input = sys.stdin.readline

class stack(list):
    push = list.append
    def pop1(self): 
        try: return self.pop(-1)
        except: return "Empty"
    def get_size(self): 
        return len(self)
    def is_empty(self): return True if not self else False
    def peek(self): 
        try: return self[-1]
        except: return "Empty"

if __name__ == "__main__":
    s = stack()
    n = int(input())
    arr = []
    pos = 0
    ans = ""

    for i in range(n):
        arr.append(int(input()))
    
    for i in range(1, n+1):
        s.push(i); ans += "+\n"
        while arr[pos] == s.peek():
            s.pop1(); ans += "-\n"
            pos += 1
            if pos == n:
                print(ans)
                exit()

    if not s.is_empty(): print("NO")