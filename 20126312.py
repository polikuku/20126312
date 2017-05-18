n,m,v=map(int,input().split())

node={}
for _ in range(m):
    a,b=map(int,input().split())
    if not (a in node): node[a]=[]
    if not (b in node): node[b]=[]
    node[a].append(b)
    node[b].append(a)

for key in node.keys():
    node[key].sort()

def dfs(root):
    stack=[root]
    visited={key:0for key in node.keys()}
    while(stack):
        cur=stack.pop(-1)
        if visited[cur]: continue
        visited[cur]=1
        print(cur,end=' ')
        for near in reversed(node[cur]):
            stack.append(near)
    print()

def bfs(root):
    queue=[root]
    visited={key:0for key in node.keys()}
    while(queue):
        cur=queue.pop(0)
        if visited[cur]: continue
        visited[cur]=1
        print(cur,end=' ')
        for near in node[cur]:
            queue.append(near)
    print()

dfs(v)
bfs(v)
