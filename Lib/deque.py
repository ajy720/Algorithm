head = 0

class deque(list):
    push_back = list.append
    def push_front(self, x):
        global head
        return self.insert(head, x)
    def pop_front(self):
        global head
        try: head += 1; return self[head-1]
        except: head -= 1; return False
    def pop_back(self):
        global head
        try: return self.pop(-1) if head < len(self) else False
        except: return False
    def size(self):
        global head
        return len(self)-head
    def empty(self):
        return True if self.size() == 0 else False
    def front(self):
        global head
        try: return self[head]
        except: return False
    def back(self):
        global head
        try: return self[-1] if head < len(self) else False
        except: return False

if __name__ == "__main__":
    dq = deque()
    while 1:
        oper = input()
        try: oper, param = oper.split()
        except: pass

        if oper == "push_front": dq.push_front(param)
        elif oper == "push_back": dq.push_back(param)
        elif oper == "pop_front": print("asd", dq.pop_front())
        elif oper == "pop_back": print("asd", dq.pop_back())
        elif oper == "size": print("asd", dq.size())
        elif oper == "empty": print("asd", dq.empty())
        elif oper == "front": print("asd", dq.front())
        elif oper == "back": print("asd", dq.back())
        elif oper == "exit": break



