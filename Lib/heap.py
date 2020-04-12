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
            try:
                if self.arr[child] > self.arr[child+1]: child += 1
            except:
                pass

            if self.arr[node] > self.arr[child]:
                self.arr[node], self.arr[child] = self.arr[child], self.arr[node]
                node = child
                child *= 2
            else:
                return
            
    def is_empty(self):
        return True if len(self.arr) == 1 else False