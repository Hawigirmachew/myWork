if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    y=-90909090
    for i in range(len(arr)):
        if arr[i]< max(arr):
            y=arr[i]
            break
         
    print(y)
    
