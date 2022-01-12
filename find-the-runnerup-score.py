if __name__ == '__main__':
    n=int(input())
    arr=sorted(map(int, input().split()))
    arr.reverse()
    for i in range(len(arr)):
        if arr[0]==arr[i]:
            continue
        else:
            print(arr[i])
            break
