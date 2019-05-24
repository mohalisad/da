n,m = [int(x) for x in input().split()]
vertics = [[i for i in range(1,n+1)]]+[[]for i in range(n)]
for i in range(m):
    a,b = [int(x) for x in input().split()]
    vertics[a].append(b)
    vertics[b].append(a)
def dfs(path):
    best_way = []
    for exit in vertics[path[-1]]:
        if exit not in path:
            path.append(exit)
            ret = dfs(path)
            if len(ret) >= len(best_way):
                if len(ret) > len(best_way):
                    best_way = ret
                else:
                    for i in range(len(best_way)):
                        if ret[i]!=best_way[i]:
                            if ret[i]<best_way[i]:
                                best_way = ret
                            break
            path.pop()
    if len(best_way) == 0:
        return path[:]
    return best_way
r = dfs([0])
r = r[1:]
print(len(r))
print(' '.join([str(x) for x in r]))
