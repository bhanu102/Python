# # printing the letter "B"
# for row in range(7):
#     for col in range(5):
#         if (col == 0 or col == 4) or (row == 0 or row == 3 or row == 6) and (col > 0 and col < 4):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# #printing the letter "T"
# for row in range(5):
#     for col in range(7):
#         if (row == 0) or (col == 3 and row > 0):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# #printing the right angle triangle
# for row in range(5):
#     for col in range(row):
#             print("*", end='')
#     print()
# Python 3.x code to demonstrate star pattern

# # Function to demonstrate printing pattern triangle
# def triangle(n):
	
# 	# number of spaces
# 	k = n - 1

# 	# outer loop to handle number of rows
# 	for i in range(0, n):
	
# 		# inner loop to handle number spaces
# 		# values changing acc. to requirement
# 		for j in range(0, k):
# 			print(end=" ")
	
# 		# decrementing k after each loop
# 		k = k - 1
	
# 		# inner loop to handle number of columns
# 		# values changing acc. to outer loop
# 		for j in range(0, i+1):
		
# 			# printing stars
# 			print("* ", end="")
	
# 		# ending line after each row
# 		print("\r")

# # Driver Code
# n = 5
# triangle(n)

