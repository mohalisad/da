def calc(n,k,inps,reg_arr,beg = 0):
    if n <= k:
        return 0
    sum = 0
    sum2 = 0
    dev = 0
    if k == 1:
        for i in range(beg,n):
            sum+=inps[i][0]*inps[i][1]
            sum2+=inps[i][0]*inps[i][0]*inps[i][1]
            dev+=inps[i][1]
        avg = round(sum/dev)
        val = sum2 + dev*avg*avg - 2*avg*sum
        return val
    else:
        ret = -1
        for i in range(beg,n-k+1):
            sum+=inps[i][0]*inps[i][1]
            sum2+=inps[i][0]*inps[i][0]*inps[i][1]
            dev+=inps[i][1]
            if reg_arr [i+1][k-1] == -1:
                reg_arr [i+1][k-1] = calc(n,k-1,inps,reg_arr,i+1)
            avg = round(sum/dev)
            val = sum2 + dev*avg*avg - 2*avg*sum
            if ret == -1:
                ret = val + reg_arr [i+1][k-1]
            else:
                ret = min(ret,val + reg_arr [i+1][k-1])
        return ret
n,k  = [int(x) for x in input().split()]
inps = [[int(x) for x in input().split()]for i in range(n)]
reg_arr = [[-1]*k for i in range(n)]
print(calc(n,k,inps,reg_arr))
