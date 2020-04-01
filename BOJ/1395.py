import sys, math

#input = sys.stdin.readline
def propagtion(node):
    pass

def init(node, start, end):
    if start == end: # 리프노드라면 데이터를 추가
        tree[node] = a[start]
        return a[start] # 부모 노드에게 값 전달
    
    else: # 리프 노드가 아닌 경우 좌우 자식으로 가지를 뻗고, 두 자식의 합을 저장. 이 부분에서 구간합, 최소/최대값 세그먼트 트리 등 속성이 결정된다.
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node] # 부모노드에게 값 전달

def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    
    elif start == end:
        if lazy[node]:
            lazy[node] = False
            tree[node]^=1

        return tree[node]

    elif start >= left and end <= right:
        if lazy[node]:
            tree[node] = end - start + 1 - tree[node]
            propagtion(node)
            lazy[node] = False
        
        return tree[node]

    else:
        if lazy[node]:
            propagtion(node)
            lazy[node] = False
            
        left = query(node*2, start, (start+end)//2, left, right)
        right = query(node*2+1, (start+end)//2+1, end, left, right)

        return left + right
        

def update(node, start, end, left, right):
    if left > end or right < start:
        return

    elif start == end:
        lazy[node] ^= True

    elif start >= left and end <= right:
        lazy[node] ^= True
    
    else:
        if lazy[node]:
            propagtion(node)

        update(node*2, start, (start+end)//2, left, right)
        update(node*2+1, (start+end)//2+1, end, left, right)

if __name__ == "__main__":
    global tree, a, n
    n, m = map(int, input().split())

    a = [0]*(n+1)
    tree = [None] * (2**math.ceil(math.log(n, 2)+1))
    lazy = [False] * (2**math.ceil(math.log(n, 2)+1))

    init(1, 0, n-1)

    for _ in range(m):
        task, s, e = map(int, input().split())
        if task:
            print(query(1, 0, n-1, s-1, e-1))
        else:
            update(1, 0, n-1, s-1, e-1)
