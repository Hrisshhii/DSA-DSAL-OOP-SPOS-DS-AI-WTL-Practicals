class GraphColoring:
    def __init__(self,graph,m):
        self.graph=graph
        self.m=m
        self.V=len(graph)
        self.colors=[0]*self.V
        
    def is_safe(self,v,c):
        for i in range(self.V):
            if self.graph[v][i]==1 and self.colors[i]==c:
                return False
        return True
    
    def coloring(self,v):
        if v==self.V:
            return True
        for c in range(1,self.m+1):
            if self.is_safe(v,c):
                self.colors[v]=c
                if self.coloring(v+1):
                    return True
                self.colors[v]=0
        return False
    
    def print_result(self):
        print('Vertex Colors:')
        for i in range(self.V):
            print(f'Vertex {i}----->color {self.colors[i]}')


def main():
    graph=[
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,1],
        [1,0,1,0]
    ]
    
    m=3
    g=GraphColoring(graph,m)
    
    if g.coloring(0):
        g.print_result()
    else:
        print("No Solution Exists")
main()
