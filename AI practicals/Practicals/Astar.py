from queue import PriorityQueue

goal=[
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

def heuristic(state):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0 and state[i][j]!=goal[i][j]:
                count+=1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def print_state(state):
    for row in state:
        print(*row)
    print()

def astar(start):
    pq=PriorityQueue()
    h=heuristic(start)
    pq.put((h,0,start,[]))
    visited=set()
    
    while not pq.empty():
        f,g,current,path=pq.get()
        if current==goal:
            print('Goal Reached!\n ')
            for step in path+[current]:
                print_state(step)
            return
        
        visited.add(to_tuple(current))
        x,y=find_blank(current)
        moves=[(1,0),(-1,0),(0,1),(0,-1)]
        
        for dx,dy in moves:
            nx=x+dx
            ny=y+dy
            
            if 0<=nx<3 and 0<=ny<3:
                new_state=[row[:] for row in current]
                
                new_state[x][y],new_state[nx][ny]=new_state[nx][ny],new_state[x][y]
                
                if to_tuple(new_state) not in visited:
                    new_g=g+1
                    new_h=heuristic(new_state)
                    new_f=new_g+new_h
                    
                    pq.put((new_f,new_g,new_state,path+[current]))
        
            
start=[
    [1,2,3],
    [4,0,6],
    [7,5,8]
]
 
astar(start)
