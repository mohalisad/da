n,m = [int(x) for x in input().split()]
neighbors = [[] for i in range(n)]
votes = [int(x) for x in input().split()]
edges = []
final_votes = votes[:]
for i in range(m):
    a,b = [int(x) for x in input().split()]
    a = a-1
    b = b-1
    neighbors[a].append(b)
    neighbors[b].append(a)
    edges.append((a,b))
def calc_most_neigbors(index):
    counter = [0,0]
    counter[votes[index]]+=1
    for item in neighbors[index]:
        counter[final_votes[item]]+=1
    return counter.index(max(counter))
for i in range(n):
    back_f = final_votes[:]
    for i in range(n):
        final_votes[i] = calc_most_neigbors(i)
    if back_f == final_votes:
        break
cost = 0
for i in range(n):
    if final_votes[i] != votes[i]:
        cost += 1
for edge in edges:
    if final_votes[edge[0]] != final_votes[edge[1]]:
        cost += 1
print(cost)
