def prims(graph,V,labels):
    selected=[False]*V
    selected[0]=True
    edges=0
    cost=0
    print("Edge : Weight")
    while edges<V-1:
        min=999999
        x,y=0,0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]!=0:
                        if min>graph[i][j]:
                            min=graph[i][j]
                            x=i
                            y=j
        print(f'{labels[x]} - {labels[y]} : {graph[x][y]}')
        cost+=graph[x][y]
        selected[y]=True
        edges+=1
    print('MST cost: ',cost)
    
V=6
graph=[
    [0,7,8,0,0,0],
    [7,0,3,6,0,0],
    [8,3,0,4,3,0],
    [0,6,4,0,2,5],
    [0,0,3,2,0,2],
    [0,0,0,5,2,0]
]
labels=['A','B','C','D','E','F']
prims(graph,V,labels)
