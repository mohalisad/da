def calc_grade(datas,grades,index):
    ld = len(datas)
    cost = 0
    if index == ld-1:
        pass
    else:
        for i in range(index+1,ld):
            cost += datas[i][0] - datas[index][0]
        distcost = 0
        for i in range(index+1,ld):
            #print (i,distcost)
            cost = min(distcost + grades[i],cost)
            distcost += datas[i][0]- datas[index][0]
    return cost + datas[index][1]
n = int(input())
ds = input().split()
ts = input().split()
datas = [(int(ds[i]),int(ts[i])) for i in range(n)]
datas.sort(key=lambda x:x[0])
grades = [0]*n
for i in range(len(datas)-1,-1,-1):
    grades[i] = calc_grade(datas,grades,i)
print(grades[0])
