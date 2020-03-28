import sys, math

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = a[start]
        return a[start]
    
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]

def query(node, start, end, i, j):
    if i > end or  j < start:
        return 0
    elif i <= start and j >= end:
        return tree[node]
    else:
        left = query(node*2, start, (start+end)//2, i, j) 
        right = query(node*2+1, (start+end)//2+1, end, i, j)
        return left+right

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    
    tree[node] += diff
    
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

if __name__ == "__main__":
    global a, tree

    n, m, k = map(int, input().split())

    a = [int(input()) for _ in range(1, n+1)]
    tree = [None] * (2**(math.ceil(math.log(n, 2))+1))

    init(1, 0, n-1)

    for i in range(m+k):
        oper, o1, o2 = map(int, input().split())

        if oper == 1:
            update(1, 0, n-1, o1-1, o2-a[o1-1])
            a[o1-1] = o2
        elif oper == 2:
            print(query(1, 0, n-1, o1-1, o2-1))