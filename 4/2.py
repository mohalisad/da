def all_subsequence(str):
    retu = {}
    for i in range(len(str)):
        retu[str[i]] = 1
        for j in range(i+1,len(str)):
            temp = str[i]+str[j]
            retu[temp] = 1
            for k in range(j+1,len(str)):
                temp = str[i]+str[j]+str[k]
                retu[temp] = 1
                for l in range(k+1,len(str)):
                    temp = str[i]+str[j]+str[k]+str[l]
                    retu[temp] = 1
    return retu
n = int(input())
all_words = {}
counter = 0
nodes = [[] for i in range(n)]
for i in range(n):
    word = input()
    subs = all_subsequence(word)
    for item in subs:
        if item not in all_words:
            all_words[item] = counter
            counter += 1
        nodes[i].append(all_words[item])
new_all_words = [0]*len(all_words)
for key,val in all_words.items():
    new_all_words[val] = key
all_words = new_all_words
length = len(all_words) + n + 2 # source + all_words + nodes + sink
matrix = [[0]*length for i in range(length)]
for i in range(len(nodes)):
    for item in nodes[i]:
        matrix[1+item][1+len(all_words)+i] = 1
for i in range(1,len(all_words)+1):
    matrix[0][i] = 1
for i in range(1+len(all_words),len(all_words)+1+len(nodes)):
    matrix[i][-1] = 1
exit(0)
def bfs():
    que = [0]
    all_parent = [-1]*(length)
    visited    = [False]*(length)
    while len(que)>0:
        item = que.pop(0)
        for next_v,check in enumerate(matrix[item]):
            if check>0 and not visited[next_v]:
                que.append(next_v)
                visited[next_v] = True
                all_parent[next_v] = item
    return visited[-1],all_parent
def find_min(path):
    mini = 100000
    c = -1
    while c != 0:
        p = path[c]
        mini = min(mini,matrix[p][c])
        c = p
    return mini
max_flow = 0
while True:
    check,path = bfs()
    if not check:
        break
    mini = find_min(path)
    max_flow += mini
    c = -1
    while c != 0:
        p = path[c]
        matrix[p][c] -= mini
        matrix[c][p] += mini
        c = p
if max_flow == n:
    for i in range(1+len(all_words),len(all_words)+1+len(nodes)):
        word_index = matrix[i].index(1) - 1
        print(all_words[word_index])
else:
    print(-1)
