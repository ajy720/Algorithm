import sys, math

#input = sys.stdin.readline

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
    
    left = query(node*2, start, (start+end)//2, i, j)
    right = query(node*2+1, (start+end)//2+1, end, i, j)

    return left+right

if __name__ == "__main__":
    global a, tree

    n = int(input("자료의 갯수를 입력하세요. : "))
    a = [int(input(f"{i}번쨰 자료를 입력하세요. : ")) for i in range(n)]
    tree = [None] * ((math.ceil(math.log(n, 2))+1)**2)

    init(1, 0, n-1)

    while int(input("구간합=1, 종료=0 : ")):
        print(query(1, 0, n, int(input("시작 : ")), int(input("끝 : "))))
        

