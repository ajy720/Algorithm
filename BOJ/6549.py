import sys, math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    
    else:
        left = init(node*2, start, (start+end)//2)
        right = init(node*2+1, (start+end)//2+1, end)

        tree[node] = left if arr[left] <= arr[right] else right

        return tree[node]
        
def mini(node, start, end, li, ri):
    if li > end or ri < start:
        return -1 # tree 배열을 초기화 할 때 마지막 값에 sys.maxsize를 넣어줌으로써 자동으로 탈락

    elif li <= start and end <= ri:
        return tree[node]

    else:
        left = mini(node*2, start, (start+end)//2, li, ri)
        right = mini(node*2+1, (start+end)//2+1, end, li, ri)

        return left if arr[left] <= arr[right] else right

def solve(i, j):
    if i == j: return arr[i] * (j-i+1)
    min_height = mini(1, 0, n-1, i, j)

    ans = arr[min_height] * (j-i+1)

    left = solve(i, min_height-1) if min_height > i else 0
    right = solve(min_height+1, j) if min_height < j else 0

    ans = max(ans, left, right)

    return ans

if __name__ == "__main__":
    
    while 1:
        global tree, arr, n

        n, *arr = map(int, input().split())
        arr+=[sys.maxsize]
        if n == 0: break
        tree = [None] * (2**math.ceil(math.log(n, 2)+1))
        init(1, 0, n-1)

        print(solve(0, n-1))
