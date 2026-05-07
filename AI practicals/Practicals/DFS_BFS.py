from collections import deque

def bfs(queue,adj,visited):
    if not queue:
        return
    node=queue.popleft()
    print(node,end=" ")
    for neighbor in adj[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    bfs(queue,adj,visited)

def dfs(visited,adj,vertex):
    visited.add(vertex)
    print(vertex,end=" ")
    for n in adj[vertex]:
        if n not in visited:
            dfs(visited,adj,n)

def main():
    adj={}
    n=int(input("Enter the number of Nodes: "))
    for i in range(n):
        node=input(f'Enter node {i+1}: ')
        neighbor=input(f'Enter the neighbors of {node}: ').split()
        if node not in adj:
            adj[node]=[]
        for neigh in neighbor:
            adj[node].append(neigh)
            if neigh not in adj:
                adj[neigh]=[]
            adj[neigh].append(node)
    num=input("\nEnter starting node: ")
    visited=set()
    print('DFS Traversal: ')
    dfs(visited,adj,num)
    
    num=input("\nEnter starting node: ")
    print('BFS Traversal: ')
    visited=set([num])
    q=deque([num])
    bfs(q,adj,visited)
main()
