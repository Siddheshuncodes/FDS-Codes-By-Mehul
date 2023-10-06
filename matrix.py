row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))


matrix = []
print("Enter the entries row wise: ")


for i in range(row):		
	arr =[]
	
	for j in range(col):	 
		arr.append(int(input()))
		
	matrix.append(arr)
	


for i in range(row):
	
	for j in range(col):
		print(matrix[i][j], end = " ")
		
	print()