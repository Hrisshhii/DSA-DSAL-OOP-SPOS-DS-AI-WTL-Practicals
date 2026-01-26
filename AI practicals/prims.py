import sys
def prims(graph,V,labels):
	selected=[False]*V
	selected[0]=True
	edges=0
	cost=0
	print("Edge : Weight")
	while edges < V-1:
		min=sys.maxsize
		x=0
		y=0
		for i in range(V):
			if selected[i]:
				for j in range(V):
					if not selected[j] and graph[i][j]!=0:
						if min>graph[i][j]:
							min=graph[i][j]
							x=i
							y=j
		print(f"{labels[x]}-{labels[y]} : {graph[x][y]}")
		cost+=graph[x][y]
		selected[y]=True
		edges+=1
	print("Total weight of MST: ",cost)

"""
	Vertices:
	0-A, 1-B, 2-C, 3-D, 4-E, 5-F

	Initial:
	selected = [T,F,F,F,F,F]
	edges = 0
	cost = 0


	It 1:
		selected vertices = {A}
		possible edges:
			A-B = 7
			A-C = 8
		min edge = A-B (7)

		O/P: A-B : 7
		selected = [T,T,F,F,F,F]
		cost = 7
		edges = 1

	It 2:
		selected vertices = {A,B}
		possible edges:
			A-C = 8
			B-C = 3
			B-D = 6
		min edge = B-C (3)

		O/P: B-C : 3
		selected = [T,T,T,F,F,F]
		cost = 10
		edges = 2

	It 3:
		selected vertices = {A,B,C}
		possible edges:
			C-D = 4
			C-E = 3
			B-D = 6
		min edge = C-E (3)

		O/P: C-E : 3
		selected = [T,T,T,F,T,F]
		cost = 13
		edges = 3

	It 4:
		selected vertices = {A,B,C,E}
		possible edges:
			E-D = 2
			E-F = 2
			C-D = 4
		min edge = E-D (2)

		O/P: E-D : 2
		selected = [T,T,T,T,T,F]
		cost = 15
		edges = 4
		
	It 5:
		selected vertices = {A,B,C,D,E}
		possible edges:
			E-F = 2
			D-F = 5
		min edge = E-F (2)

		O/P: E-F : 2
		selected = [T,T,T,T,T,T]
		cost = 17
		edges = 5

	Final MST Cost = 17	

"""

graph=[
	[0,7,8,0,0,0],
	[7,0,3,6,0,0],
	[8,3,0,4,3,0],
	[0,6,4,0,2,5],
	[0,0,3,2,0,2],
	[0,0,0,5,2,0]
]		
labels=['A','B','C','D','E','F']
prims(graph,6,labels)
