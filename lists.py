if __name__ == '__main__':
    arr=[]
    N = int(input())
    for i in range(0,N):
        li=input().split()
        if li[0] == "print":
            print(arr)
        elif li[0]== "append":
            arr.append(int(li[1]))
        elif li[0]== "insert":
            arr.insert(int(li[1]),int(li[2]))
        elif li[0]== "remove":
            arr.remove(int(li[1]))
        elif li[0]== "sort":
            arr.sort()
        elif li[0]== "pop":
            arr.pop()
        else:
            arr.reverse()
