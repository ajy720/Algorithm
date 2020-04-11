import sys

if __name__ == "__main__":
    arr = [None]
    l = 0
    for _ in range(int(input())):
        o = int(sys.stdin.readline())
        if o == 0:
            if not l:
                print(0)
                continue

            arr[1], arr[-1] = arr[-1], arr[1]
            print(arr.pop())

            node = 1
            big = 2
            
            while big <= l:
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

            l-=1

        else:
            arr.append(o)
            l += 1
            node = l
            while node//2:
                if arr[node//2] < arr[node]:
                    arr[node//2], arr[node] = arr[node], arr[node//2]
                    node //= 2
                else: 
                    break

            