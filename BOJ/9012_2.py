import sys

input = sys.stdin.readline

class stack(list):
    push = list.append
    def pop1(self): 
        try: return self.pop(-1)
        except: return False
    def get_size(self): 
        return len(self)
    def is_empty(self): return True if not self else False
    def peek(self): 
        try: return self[-1]
        except: return False

if __name__ == "__main__":
    for i in range(int(input())):
        s = stack()
        flag = False

        for i in input():
            if i == "(": s.push(i)
            elif i == ")":
                if not s.pop1():
                    print("NO")
                    flag = True
                    break
        
        if flag: continue
        if s.is_empty(): print("YES")
        else: print("NO")