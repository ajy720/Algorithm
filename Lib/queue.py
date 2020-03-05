head = 0

class queue(list):
    push = list.append
    def pop1(self):
        global head
        try: ret = self[head]; head += 1; return ret
        except: return "Empty"
    def get_size(self): 
        global head
        return len(self)-head
    def is_empty(self): return 1 if self.get_size() == 0 else 0
    def head(self):
        global head
        try: return self[head]
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