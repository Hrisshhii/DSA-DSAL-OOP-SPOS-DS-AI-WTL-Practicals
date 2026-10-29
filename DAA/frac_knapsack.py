n=int(input("Enter the number of items: "))
weight=[]
profit=[]

for i in range(n):
  w=int(input(f"\nEnter Weight for {i}: "))
  p=int(input(f"\nEnter Profit for {i}: "))
  weight.append(w)
  profit.append(p)
capacity=int(input("\nEnter Knapsack Capacity: "))

ratio=[]
for i in range(n):
  ratio.append(profit[i]/weight[i])

for i in range(n):
  for j in range(i+1,n):
    if ratio[i]<ratio[j]:
      ratio[i],ratio[j]=ratio[j],ratio[i]
      weight[i],weight[j]=weight[j],weight[i]
      profit[i],profit[j]=profit[j],profit[i]
      
totalProfit=0
selected=[]
for i in range(n):
  if capacity==0:
    break
  if capacity>=weight[i]:
    capacity-=weight[i]
    totalProfit+=profit[i]
    selected.append((i,capacity,ratio[i]*capacity,1))
  else:
    fraction=capacity/weight[i]
    itemProfit=ratio[i]*capacity
    totalProfit+=itemProfit
    selected.append((i,capacity,ratio[i]*capacity,fraction))
    capacity=0
    break

print("\nSelected Items:")
for item, w, p, fraction in selected:
    print(f"Item {item}: Weight = {w}, Profit = {p:.2f}, Fraction = {fraction:.2f}")
print("Maximum Profit: ",totalProfit)
  
