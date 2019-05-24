n,m = [int(x) for x in input().split()]
edges = [[0]*(n+2) for i in range(n+2)]
votes = [int(x) for x in input().split()]
for i in range(m):
    a,b = [int(x) for x in input().split()]
    edges[a][b] = 1
    edges[b][a] = 1
for index,item in enumerate(votes):
    if item == 1:
        edges[0][index+1] = 1
    else:
        edges[index+1][-1] = 1
def bfs():
    que = [0]
    all_parent = [-1]*(n+2)
    visited    = [False]*(n+2)
    while True:
        item = que.pop(0)
        for next_v,check in enumerate(votes):
            if check>0 and not visited[next_v]:
                que.append(next_v)
                visited[next_v] = True
                all_parent[next_v] = item
    return visited[-1],all_parent
while True:
    check,path = bfs()
    if not check:
        break
    
