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
    s = stack()

    for i in range(int(input())):
        oper = input().strip("\n")
        try: oper, param = oper.split()
        except: pass

        if oper == "push": s.push(int(param))
        elif oper == "pop": print(s.pop1())
        elif oper == "size": print(s.get_size())
        elif oper == "empty": print(s.is_empty())
        elif oper == "top": print(s.peek())
        elif oper == "exit": break