def selectionSort(arr):
	n=len(arr)
	for i in range(n):
		min=i
		for j in range(i+1,n):
			if arr[j]<arr[min]:
				min=j
		arr[i],arr[min]=arr[min],arr[i]
	return arr
	
def main():
	arr=[]
	n=int(input("ENTER NUMBER OF ELEMENTS IN ARRAY: "))
	for i in range(n):
		ele=int(input(f"ENTER ELEMENT {i}: "))
		arr.append(ele)
	while True:
		print("\n\n\t**************MENU***************")
		print("\n\t1.SELECTION SORT\n\t2.EXIT")
		choice=int(input("\n\tENTER YOUR CHOICE: "))
		if choice==1:
			selectionSort(arr)
			print(f"\n\tArray: {arr}")
		elif choice==2:
			print("\n\tExiting....")
			break
		else: 
			print("\n\tInvalid Choice!!!")
main()
"""
	arr = [64, 25, 12, 22, 11]
	n = 5
	
	It 1:
		min=0 arr[0]=64
		for loop
			25<64  true
			min=1
			
			12<25  true
			min=2
			
			22<12  false
			
			11<12  true
			min=4
		swap index 0 and 4
		arr[11,25,12,22,64]
	It 2: 
		min=1 arr[1]=25
		for loop
			12<25  true
			min=2
			
			22<12  false
			
			64<12  false

		swap index 1 and 2
		arr[11,12,25,22,64]
	It 3: 
		min=2 arr[2]=25
		for loop
			22<25  true
			min=3
			
			64<22  false
			
		swap index 2 and 3
		arr[11,12,22,25,64]
	It 4: 
		min=3 arr[2]=25
		for loop
			64<25  false
			
		no change in min
		arr[11,12,22,25,64]
	It 5: 
		min=4 arr[4]=64
		last element already sorted
		no change in min
		arr[11,12,22,25,64]
				
		
"""
