def Non_rec_fib(n):
  fib=[]
  a,b=0,1
  for i in range(n):
    fib.append(a)
    a,b=b,a+b
  return fib
print("Non-Recursive Fibonacci Series: ",Non_rec_fib(10))

def Rec_fib(n):
  if n==0:
    return []
  elif n==1:
    return [0]
  elif n==2:
    return [0,1]
  else:
    fib=Rec_fib(n-1)
    fib.append(fib[-1]+fib[-2])
    return fib
print("Recursive Fibonacci Series: ",Rec_fib(10))
