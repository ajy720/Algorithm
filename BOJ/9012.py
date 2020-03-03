import sys

input = sys.stdin.readline

class stack(list):
    push = list.append
    def pop1(self): 
        try: return self.pop(-1)
        except: return -1
    def get_size(self): 
        return len(self)
    def is_empty(self): return 0 if self else 1
    def peek(self): 
        try: return self[-1]
        except: return -1

if __name__ == "__main__":
    for i in range(int(input())):
        s = 0

        for i in input():
            if i == "(": s += 1
            elif i == ")": s -= 1

            if s < 0: break
            
        print("YES" if s == 0 else "NO")