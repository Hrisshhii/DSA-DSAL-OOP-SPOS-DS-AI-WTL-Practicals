n=int(input("Enter Number of Items: "))
weight=[]
profit=[]

for i in range(n):
  weight.append(int(input(f"Enter the weight of Item {i}: ")))
  profit.append(int(input(f"Enter the profit of Item {i}: ")))
capacity=int(input("Enter the Capacity of Kanpsack: "))

dp=[[0 for j in range(capacity+1)] for i in range(n+1)]

for i in range(1,n+1):
  for j in range(1,capacity+1):
    if weight[i-1]<=j:
      dp[i][j]=max(profit[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])
    else:
      dp[i][j]=dp[i-1][j]
print("\nDP TABLE")
for i in range(n+1):
  for j in range(capacity+1):
    print(dp[i][j],end="\t")
  print()
print("Maximum Profit: ",dp[n][capacity])

"""
Enter Number of Items: 3
Enter the weight of Item 0: 1
Enter the profit of Item 0: 6
Enter the weight of Item 1: 2
Enter the profit of Item 1: 10
Enter the weight of Item 2: 3
Enter the profit of Item 2: 12
Enter the Capacity of Kanpsack: 5

DP TABLE
0	0	0	0	0	0	
0	6	6	6	6	6	
0	6	10	16	16	16	
0	6	10	16	18	22	
Maximum Profit:  22
"""
