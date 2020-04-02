import sys, math

input = sys.stdin.readline

def propagtion(node, start, end):
    if lazy[node]:
        lazy[node] = False
        if not start == end:
            lazy[node*2]^=True
            lazy[node*2+1]^=True
        tree[node] = end - start + 1 - tree[node]

def init(node, start, end):
    if start == end: # 리프노드라면 데이터를 추가
        tree[node] = 0
        return 0 # 부모 노드에게 값 전달
    
    else: # 리프 노드가 아닌 경우 좌우 자식으로 가지를 뻗고, 두 자식의 합을 저장.
        l = init(node*2, start, (start+end)//2)
        r = init(node*2+1, (start+end)//2+1, end)
        tree[node] = l + r

        return tree[node] # 부모노드에게 값 전달

def query(node, start, end, left, right):
    propagtion(node, start, end)

    if left > end or right < start: 
        return 0

    elif start >= left and end <= right: 
        return tree[node]

    else:
        l = query(node*2, start, (start+end)//2, left, right)
        r = query(node*2+1, (start+end)//2+1, end, left, right)

        return l+r
        
def update(node, start, end, left, right):
    propagtion(node, start, end)
            
    if left > end or right < start: 
        return tree[node]

    elif start == end:
        tree[node] ^= 1
        return tree[node]

    elif start >= left and end <= right:
        lazy[node] = True
        return end - start + 1 - tree[node]
    
    else:
        l = update(node*2, start, (start+end)//2, left, right)
        r = update(node*2+1, (start+end)//2+1, end, left, right)
        tree[node] = l + r

        return tree[node]

if __name__ == "__main__":
    global tree, n
    n, m = map(int, input().split())

    tree = [None] * (2**math.ceil(math.log(n, 2)+1))
    lazy = [False] * (2**math.ceil(math.log(n, 2)+1))

    init(1, 0, n-1)

    for _ in range(m):
        task, s, e = map(int, input().split())
        if task:
            print(query(1, 0, n-1, s-1, e-1))
        else:
            update(1, 0, n-1, s-1, e-1)