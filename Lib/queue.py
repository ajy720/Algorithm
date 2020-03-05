class queue(list):
    push = list.append
    def pop1(self): 
        try: return self.pop(0)
        except: return "Empty"
    def get_size(self): 
        return len(self)
    def is_empty(self): return True if not self else False
    def front(self):
        try: return self[0]
        except: return "Empty"
    def back(self): 
        try: return self[-1]
        except: return "Empty"

if __name__ == "__main__":
    q = queue()

    while 1:
        oper = input()
        try: oper, param = oper.split()
        except: pass

        if oper == "push": q.push(int(param))
        elif oper == "pop": print(q.pop1())
        elif oper == "size": print(q.get_size())
        elif oper == "empty": print(q.is_empty())
        elif oper == "front": print(q.front())
        elif oper == "back": print(q.back())
        elif oper == "exit": break