n = int(input())-1
bn = bin(n)[2:]
m = len(bn)
arr = [[] for i in range(2*m)]
for i in range(n+1):
    bn = bin(i)[2:]
    bn = '0'*(m-len(bn))+bn
    for j in range(m):
        if bn[j] == '1':
            arr[j].append(i+1)
        else:
            arr[j+m].append(i+1)
print(2*m)
for row in arr:
    print (str(len(row))+' '+' '.join(str(item) for item in row))
