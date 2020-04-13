import sys

input = sys.stdin.readline

class heap:
    arr = [None]
    def __init__(self):
        super().__init__()
    
    def insert(self, o):
        self.arr.append(o)
        node = len(self.arr)-1

        while node // 2:
            a = abs(self.arr[node])
            b = abs(self.arr[node//2])
            if a < b or (a == b and self.arr[node] < self.arr[node//2]):
                self.arr[node], self.arr[node//2] = self.arr[node//2], self.arr[node]
                node //= 2
            else:
                return

    def delete(self, o):
        if self.is_empty(): 
            print(0)
            return

        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        print(self.arr.pop())
        node, child = 1, 2

        while child < len(self.arr):
            a = abs(self.arr[node])
            b = abs(self.arr[child])
            try:
                c = abs(self.arr[child+1])
                if b > c or (b == c and self.arr[child] > self.arr[child+1]): child += 1
            except:
                pass

            if a > b or (a == b and self.arr[node] > self.arr[child]):
                self.arr[node], self.arr[child] = self.arr[child], self.arr[node]
                node = child
                child *= 2
            else:
                return
            
    def is_empty(self):
        return True if len(self.arr) == 1 else False

if __name__ == "__main__":
    hp = heap()

    for _ in range(int(input())):
        o = int(input())

        if o:
            hp.insert(o)
        else:
            hp.delete(o)