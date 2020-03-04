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
    while 1:
        ans = True
        s = stack()
        string = input().strip("\n")

        if string == '.': exit()

        for i in string:
            if i == "(" or i == "[":
                s.push(i)
            elif i == ")":
                if s.pop1() == "(" : continue
                else: ans = False; break
            elif i == "]":
                if s.pop1() == "[" : continue
                else: ans = False; break
        
        print("yes" if ans and s.is_empty() else "no")