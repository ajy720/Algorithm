<<<<<<< HEAD
class heap:
    arr = [None]
    def __init__(self):
        super().__init__()
    
    def insert(self, o):
        self.arr.append(o)
        node = len(self.arr)-1

        while node // 2:
            if self.arr[node] < self.arr[node//2]:
                self.arr[node], self.arr[node//2] = self.arr[node//2], self.arr[node]
=======
import sys

input = sys.stdin.readline


class min_heap:
    arr = [None]

    def insert(self, o):
        self.arr.append(o)
        node = len(self.arr) - 1

        while node // 2:
            if self.arr[node] < self.arr[node // 2]:
                self.arr[node], self.arr[node // 2] = (
                    self.arr[node // 2],
                    self.arr[node],
                )
>>>>>>> bb038e66d8d7365f6cccd2c82d3fbf0b1f94bd05
                node //= 2
            else:
                return

<<<<<<< HEAD
    def delete(self, o):
        if self.is_empty(): 
            print(0)
            return

        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        print(self.arr.pop())
=======
    def delete(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        ret = self.arr.pop()
>>>>>>> bb038e66d8d7365f6cccd2c82d3fbf0b1f94bd05
        node, child = 1, 2

        while child < len(self.arr):
            try:
<<<<<<< HEAD
                if self.arr[child] > self.arr[child+1]: child += 1
=======
                if self.arr[child] > self.arr[child + 1]:
                    child += 1
>>>>>>> bb038e66d8d7365f6cccd2c82d3fbf0b1f94bd05
            except:
                pass

            if self.arr[node] > self.arr[child]:
                self.arr[node], self.arr[child] = self.arr[child], self.arr[node]
                node = child
                child *= 2
            else:
<<<<<<< HEAD
                return
            
    def is_empty(self):
        return True if len(self.arr) == 1 else False
=======
                break
        return ret


class max_heap:
    arr = [None]

    def insert(self, o):
        self.arr.append(o)
        node = len(self.arr) - 1

        while node // 2:
            if self.arr[node] > self.arr[node // 2]:
                self.arr[node], self.arr[node // 2] = (
                    self.arr[node // 2],
                    self.arr[node],
                )
                node //= 2
            else:
                return

    def delete(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        ret = self.arr.pop()
        node, child = 1, 2

        while child < len(self.arr):
            try:
                if self.arr[child] < self.arr[child + 1]:
                    child += 1
            except:
                pass

            if self.arr[node] < self.arr[child]:
                self.arr[node], self.arr[child] = self.arr[child], self.arr[node]
                node = child
                child *= 2
            else:
                break

        return ret


if __name__ == "__main__":
    less = max_heap()
    more = min_heap()
    mid = sys.maxsize
    for _ in range(int(input())):
        o = int(input())

        if o <= mid:
            less.insert(o)
        else:
            more.insert(o)

        if len(more.arr) > len(less.arr):
            less.insert(more.delete())
        elif len(more.arr) < len(less.arr) - 1:
            more.insert(less.delete())

        mid = less.arr[1]
        print(mid)
>>>>>>> bb038e66d8d7365f6cccd2c82d3fbf0b1f94bd05
