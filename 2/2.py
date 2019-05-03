def count (neg_arr,pos_arr):
    c = 0
    i = 0
    neg_arr.sort()
    pos_arr.sort(reverse=True)
    for item in pos_arr:
        if i == len(neg_arr):
            break
        if neg_arr[i] + item<0:
            i+=1
    return i

input()
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
neg_arr1=[]
neg_arr2=[]
pos_arr1=[]
pos_arr2=[]

for x in arr1:
    if x>=0:
        pos_arr1.append(x)
    else:
        neg_arr1.append(x)
for x in arr2:
    if x>=0:
        pos_arr2.append(x)
    else:
        neg_arr2.append(x)
print(count(neg_arr1,pos_arr2)+count(neg_arr2,pos_arr1))
