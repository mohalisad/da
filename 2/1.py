def calc(arr,n,a=0,b=0,c=0):
    if a==n and b==n and c==n:
        return 1
    total = 0
    if n>a:
        if arr[a+1][b][c] == -1:
            arr[a+1][b][c] = calc(arr,n,a+1,b,c)
        total += arr[a+1][b][c]
    if a>b and n>b:
        if arr[a][b+1][c] == -1:
            arr[a][b+1][c] = calc(arr,n,a,b+1,c)
        total += arr[a][b+1][c]
    if b>c and n>c:
        if arr[a][b][c+1] == -1:
            arr[a][b][c+1] = calc(arr,n,a,b,c+1)
        total += arr[a][b][c+1]
    return total
count = int(input())
for k in range(count):
    n = int(input())
    arr = [[[-1]*(n+1) for i in range(n+1)]for j in range(n+1)]
    print(calc(arr,n))
