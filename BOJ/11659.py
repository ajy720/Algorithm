import sys

input = sys.stdin.readline

class sgTree(list):
    def __init__(self):
        self = []

    def setdata(self, _arr):
        self.append(0)
        for i in range(len(_arr)):
            self.append(_arr[i]+self[i])

    def getSum(self, i, j):
        return self[j]-self[i-1]

if __name__ == "__main__":
    st = sgTree()
    n, m = map(int, input().split())
    st.setdata(list(map(int, input().split())))

    for _ in range(m):
        i, j = map(int, input().split())

        print(st.getSum(i, j))