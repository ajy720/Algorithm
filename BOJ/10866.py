import sys

input = sys.stdin.readline

head = 0

class deque(list):
    push_back = list.append
    def push_front(self, x):
        global head
        return self.insert(head, x)
    def pop_front(self):
        global head
        try: head += 1; return self[head-1]
        except: head -= 1; return -1
    def pop_back(self):
        global head
        try: return self.pop(-1) if head < len(self) else -1
        except: return -1
    def size(self):
        global head
        return len(self)-head
    def empty(self):
        return 1 if self.size() == 0 else 0
    def front(self):
        global head
        try: return self[head]
        except: return -1
    def back(self):
        global head
        try: return self[-1] if head < len(self) else -1
        except: return -1

if __name__ == "__main__":
    dq = deque()
    for _ in range(int(input())):
        oper = input().strip("\n")
        try: oper, param = oper.split()
        except: pass

        if oper == "push_front": dq.push_front(param)
        elif oper == "push_back": dq.push_back(param)
        elif oper == "pop_front": print(dq.pop_front())
        elif oper == "pop_back": print(dq.pop_back())
        elif oper == "size": print(dq.size())
        elif oper == "empty": print(dq.empty())
        elif oper == "front": print(dq.front())
        elif oper == "back": print(dq.back())
        elif oper == "exit": break