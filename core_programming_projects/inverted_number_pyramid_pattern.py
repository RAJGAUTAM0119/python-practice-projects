# Enter the row size for the pattern: 5
# 1 2 3 4 5 4 3 2 1 
#   1 2 3 4 3 2 1 
#     1 2 3 2 1 
#       1 2 1 
#         1 

rows = 9

for i in range(1,rows+1):
  for j in range(i):
    print(" ", end = " ")
  for j in range (1,rows-i+2):
    print(j, end = " ")
  for j in range(rows-i,0,-1):
    print(j, end = " ")
  print()