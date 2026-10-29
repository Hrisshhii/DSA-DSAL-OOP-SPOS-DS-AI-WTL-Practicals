n=int(input("Enter the Number of Queens: "))
board=[[0 for i in range(n)] for i in range(n)]
board[0][0]=1

def is_safe(row,col):
  for i in range(row):
    if board[i][col]==1:
      return False
  i=row-1
  j=col-1
  while i>=0 and j>=0:
    if board[i][j]==1:
      return False
    i-=1
    j-=1
  i=row-1
  j=col+1
  while i>=0 and j<n:
    if board[i][j]==1:
      return False
    i-=1
    j+=1
  return True

def solve(row):
  if row==n:
    return True

  for col in range(n):
    if is_safe(row,col):
      board[row][col]=1
      if solve(row+1):
        return True
      board[row][col]=0
  return False

if n==1:
  result=True
elif n<4:
  result=False
else: 
  result=solve(1)

if result:
  print("N QUEEN BOARD: ")
  for row in board:
    print(row)
else:
  print("Solution does not exist!!")
