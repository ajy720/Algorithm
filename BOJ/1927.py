import sys

input = sys.stdin.readline

if __name__ == "__main__":
    arr = [None]
    for _ in range(int(input())):
        o = int(input())
        if o:
            arr.append(o)
            node = len(arr)-1

            while node // 2:
                if arr[node] < arr[node//2]:
                    arr[node], arr[node//2] = arr[node//2], arr[node]
                    node //= 2
                else:
                    break
        else:
            if len(arr) == 1: 
                print(0)
                continue

            arr[1], arr[-1] = arr[-1], arr[1]
            print(arr.pop())
            node, child = 1, 2

            while child < len(arr):
                try:
                    if arr[child] > arr[child+1]: child += 1
                except:
                    pass

                if arr[node] > arr[child]:
                    arr[node], arr[child] = arr[child], arr[node]
                    node = child
                    child *= 2
                else:
                    break