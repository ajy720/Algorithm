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
                node //= 2
            else:
                return

    def delete(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        ret = self.arr.pop()
        node, child = 1, 2

        while child < len(self.arr):
            try:
                if self.arr[child] > self.arr[child + 1]:
                    child += 1
            except:
                pass

            if self.arr[node] > self.arr[child]:
                self.arr[node], self.arr[child] = self.arr[child], self.arr[node]
                node = child
                child *= 2
            else:
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
