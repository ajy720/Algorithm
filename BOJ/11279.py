import sys

input = sys.stdin.readline

if __name__ == "__main__":
    arr = [None]
    for _ in range(int(input())):
        o = int(input())
        if o == 0:
            if len(arr)==1:
                print(0)
                continue

            arr[1], arr[-1] = arr[-1], arr[1]
            print(arr.pop())

            node = 1
            big = 2
            
            while big < len(arr):
                try:
                    if arr[big] < arr[big+1]: big += 1
                except:
                    pass

                if arr[node] < arr[big]:
                    arr[node], arr[big] = arr[big], arr[node]
                    node = big
                    big *= 2
                else:
                    break

        else:
            arr.append(o)
            node = len(arr)-1

            while node//2:
                if arr[node//2] < arr[node]:
                    arr[node//2], arr[node] = arr[node], arr[node//2]
                    node //= 2
                else: 
                    break