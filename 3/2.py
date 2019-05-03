import heapq
import bisect

def find_distance(path_to_nodes,roades_city_wise,begin,end):
    if path_to_nodes[begin][1] > path_to_nodes[end][1]:
        begin,end = end,begin
    maxi1 = 0
    maxi2 = 0
    while path_to_nodes[begin][1] != path_to_nodes[end][1]:
        maxi1 = max(maxi1,roades_city_wise[end][path_to_nodes[end][0]])
        end = path_to_nodes[end][0]
    while begin != end:
        maxi1 = max(maxi1,roades_city_wise[end][path_to_nodes[end][0]])
        maxi2 = max(maxi2,roades_city_wise[begin][path_to_nodes[begin][0]])
        begin = path_to_nodes[begin][0]
        end = path_to_nodes[end][0]
    return max(maxi1,maxi2)


n,r = [int(x) for x in input().split()]
roades_city_wise = [{} for i in range(n+1)]
for i in range(r):
    inp = [int(x) for x in input().split()]
    src,dst = inp[0],inp[1]
    roades_city_wise[src][dst] = inp[2]
    roades_city_wise[dst][src] = inp[2]
cost = 0
heap = []
next_v = 1
tvectors = 0
seen = []
path_to_nodes = [0]*(n+1)
path_to_nodes[1] = (1,0)
while tvectors < n - 1:
    bisect.insort_left(seen,next_v)
    for dst,_cost in roades_city_wise[next_v].items():
        heapq.heappush(heap,(_cost,next_v,dst))
    while True:
        n_cost,src,next_v = heapq.heappop(heap)
        index = bisect.bisect_left(seen,next_v)
        if index == len(seen) or seen[index] != next_v:
            break
    cost += n_cost
    path_to_nodes[next_v] = (src,path_to_nodes[src][1]+1)
    tvectors += 1
q = int(input())
for i in range(q):
    src,dst = [int(x) for x in input().split()]
    path = find_distance(path_to_nodes,roades_city_wise,src,dst)
    print (cost - path + roades_city_wise[src][dst])
