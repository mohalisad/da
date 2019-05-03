n,m = [int(x) for x in input().split()]
exits = [[]for i in range(n)]
closed = [0]*n
for i in range(m):
    src,dst,time = ([int(x) for x in input().split()])
    exits[src-1].append((dst-1,time))
    exits[dst-1].append((src-1,time))
for i in range(n):
    closed[i] = ([int(x) for x in input().split()[1:]])
closed[-1] = []
INFINITY = 10000000
costs = [[INFINITY,False]for i in range(n)]
costs[0][0] = 0
if 0 in closed[0]:
    costs[0][0] = 1
def get_min_index():
    mini = 100*INFINITY
    mini_index = 0
    all_true = True
    for i in range(0,n):
        if not costs[i][1]:
            all_true = False
            if mini>costs[i][0]:
                mini = costs[i][0]
                mini_index = i
    if all_true:
        return -1,0
    return mini_index,mini
while True:
    index,mini = get_min_index()
    if mini >= INFINITY:
        break
    if index == -1:
        break
    for exit in exits[index]:
        if not costs[exit[0]][1]:
            new_cost = costs[index][0] + exit[1]
            if new_cost in closed[exit[0]]:
                new_cost += 1
            costs[exit[0]][0] = min(costs[exit[0]][0],new_cost)
    costs[index][1] = True
if costs[-1][0]>=INFINITY:
    print (-1)
else:
    print(costs[-1][0])
