import java.util.*;

public class GraphTraversal
{
	private int vertices;
	private ArrayList<ArrayList<Integer>> adjList;
	
	public GraphTraversal(int vertices)
	{
		this.vertices = vertices;
		adjList = new ArrayList<>();
		for (int i = 0; i < vertices; i++)
		{
			adjList.add(new ArrayList<>());
		}
	}
	
	public void addEdge(int u, int v)
	{
		adjList.get(u).add(v);
		adjList.get(v).add(u);
	}
	// 0-> [1,2]
	// 1-> [0,3]
	// 2-> [0,4]
	// 3-> [1,5]
	// 4-> [2]
	// 5-> [3]
	
	public void dfsRecursive(int node, boolean[] visited)
	{
		visited[node] = true;
		System.out.print(node + " ");
		
		for( int neighbor : adjList.get(node))
		{
			if( !visited[neighbor])
			{
				dfsRecursive(neighbor, visited);
			}
		}
	}
	/*
		visited=[false,false,false,false,false,false]
	It 1: 
			0->visied
		O/P: 0 
			visited=[T,F,F,F,F,F]
			neighbor=1,2
			1->not visited
			dfs(1,visited)
	It 2:
			1->visited
		O/P: 0 1
			visited=[T,T,F,F,F,F]
			neighbor=0,3
			0->visited
			3->not visited
			dfs(3,visited)
	It 3:
			3->visited
		O/P: 0 1 3
			visited=[T,T,F,T,F,F]
			neighbor=1,5
			1->visited
			5->not visited
			dfs(5,visited)
	It 4:
			5->visited
		O/P: 0 1 3 5
			visited=[T,T,F,T,F,T]
			neighbor=3 
			3->visited
		backtrack
	It 5: 
			2->visited
		O/P: 0 1 3 5 2 
			visited=[T,T,T,T,F,T]
			neighbor=0,4 
			0->visited
			4->not visited
			dfs(4,visited)
	It 6: 
			4->visited
		O/P: 0 1 3 5 2 4 
			visited=[T,T,T,T,T,T]
			neighbor=2
			2->visited
	*/
	
	public void bfsRecursive(Queue<Integer> queue, boolean[] visited)
	{
		if (queue.isEmpty()) return;
		
		int node = queue.poll();
		System.out.print( node + " " );
		
		for(int neighbor : adjList.get(node))
		{
			if(!visited[neighbor])
			{
				visited[neighbor] = true;
				queue.add(neighbor);
			}
		}
		
		bfsRecursive(queue, visited);
	}
	
	/*
	visited[0]=True
	queue[0]
	It 1: 
		poll->node: 0
		O/P: 0
		poll->node: 0
		neighbor: 1,2
		both not visited
		visited[1]=true
		visited[2]=true
		queue[1,2]
	It 2: 
		queue[1,2]
		poll->node: 1
		O/P: 0 1
		neighbor: 0,3
		0-> visited
		visited[3]=true
		queue[2,3]
	It 3: 
		queue[2,3]
		poll->node: 2
		O/P: 0 1 2
		neighbor: 0,4
		0-> visited
		visited[4]=true
		queue[3,4]
	It 4: 
		queue[3,4]
		poll->node: 3
		O/P: 0 1 2 3
		neighbor: 1,5
		1-> visited
		visited[5]=true
		queue[4,5]
	It 5: 
		queue[4,5]
		poll->node: 4
		O/P: 0 1 2 3 4
		neighbor: 2
		2->visited
		queue[5]
	It 6: 
		queue[5]
		poll->node: 5
		O/P: 0 1 2 3 4 5
		neighbor: 3
		3->visited
		queue[]
		
	*/
	
	public static void main(String[] args)
	{
		GraphTraversal graph = new GraphTraversal(6);
		
		graph.addEdge(0, 1);
		graph.addEdge(0, 2);
		graph.addEdge(1, 3);
		graph.addEdge(2, 4);
		graph.addEdge(3, 5);
		
		
		System.out.println("DFS Traversal : ");
		boolean[] visited = new boolean[6];
		graph.dfsRecursive(0, visited);
		
		System.out.println("\n\n BFS Traversal : ");
		visited = new boolean[6];
		Queue<Integer> queue = new LinkedList<>();
		visited[0] = true;
		queue.add(0);
		graph.bfsRecursive(queue, visited);
	}
}
		
