import sys, math

#input = sys.stdin.readline

def init(node, start, end):
    if start == end: # 리프노드라면 데이터를 추가
        tree[node] = a[start]
        return a[start] # 부모 노드에게 값 전달
    
    else: # 리프 노드가 아닌 경우 좌우 자식으로 가지를 뻗고, 두 자식의 합을 저장. 이 부분에서 구간합, 최소/최대값 세그먼트 트리 등 속성이 결정된다.
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node] # 부모노드에게 값 전달

def query(node, start, end, i, j):
    if i > end or  j < start: # 요청을 받은 구간에 현재 구간이 포함되지 않는다면 0을 리턴.
        return 0 # 다른 속성일 경우 여기 값도 수정

    elif i <= start and j >= end: # 요청을 받은 구간에 현재 구간이 모두 포함될 경우
        return tree[node] # 굳이 자식까지 탐색 안 하고 현재 노드의 값을 반환.

    else: # 그렇지 않을 경우 좌우 자식에게 똑같이 적용
        left = query(node*2, start, (start+end)//2, i, j) 
        right = query(node*2+1, (start+end)//2+1, end, i, j)

        return left+right # 부모 노드에게 값 전달

def update(node, start, end, index, diff):
    if index < start or index > end: # 현재 노드의 자식에 변경된 노드가 없으면 리턴
        return
    
    tree[node] += diff # 변경된 값 만큼 현재 노드에 반영

    if start != end: # 리프 노드가 아닌 경우 좌우 자식에게 똑같이 적용
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

if __name__ == "__main__":
    global a, tree

    n = int(input("자료의 갯수를 입력하세요. : "))
    a = [int(input(f"{i}번쨰 자료를 입력하세요. : ")) for i in range(n)]
    tree = [None] * ((math.ceil(math.log(n, 2))+1)**2)

    init(1, 0, n-1)

    while 1:
        print("입력 형식 : (1=업데이트, 2=구간합) (변경할/시작 노드 인덱스) (변경할 값/끝 노드 인덱스)")
        oper, o1, o2 = map(int, input().split())
        
        # 리스트 인덱스는 0부터 시작하니까 인덱스 인수는 모두 -1
        if oper == 1:
            update(1, 0, n-1, o1-1, o2-a[o1-1])
            a[o1-1] = o2
        elif oper == 2:
            print(query(1, 0, n-1, o1-1, o2-1))