def all_subsequence(str):
    retu = set()
    for i in range(len(str)):
        retu.add(str[i])
        for j in range(i+1,len(str)):
            temp2 = str[i]+str[j]
            retu.add(temp2)
            for k in range(j+1,len(str)):
                temp3 = temp2+str[k]
                retu.add(temp3)
                for l in range(k+1,len(str)):
                    temp4 = temp3+str[l]
                    retu.add(temp4)
    return retu
n = int(input())
nodes = [[] for i in range(n)]
all_words = {}
counter = 0
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
matrix = [[0]*len(all_words) for i in range(n)]
for i in range(len(nodes)):
    for item in nodes[i]:
        matrix[i][item] = 1
def bpm(u,match,visited):
    for v in range(len(all_words)):
        if matrix[u][v] and not visited[v]:
            visited[v] = True
            if match[v] == -1 or bpm(match[v],match,visited):
                match[v] = u
                return True
    return False
max_flow = 0
match = [-1]*len(all_words)
for i in range(n):
    visited = [False]*len(all_words)
    if bpm(i,match,visited):
        max_flow += 1
if max_flow == n:
    for i in range(n):
        word_index = match.index(i)
        print(all_words[word_index])
else:
    print(-1)
