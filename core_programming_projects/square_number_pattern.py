# Enter the row size for the pattern: 4
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 

rows = 4

for i in range(1,rows+1):
  for j in range(1,rows+1):
    print(j,end=" ")
  print()
  

print()
print()
# Enter the row size for the pattern: 5
# 1 2 3 4 5 
# 1       5 
# 1       5 
# 1       5 
# 1 2 3 4 5 

rows = 5

for i in range(1,rows+1):
  for j in range(1,rows+1):
    if i == 1 or j == 1 or j == rows or i == rows:
      print(j,end=" ")
    else:
      print(" ",end=" ")
  print()

print()
print()
# Enter the row size for the pattern: 4
# 1 0 1 0 
# 0 1 0 1 
# 1 0 1 0 
# 0 1 0 1 

rows = 4

for i in range(1,rows+1):
  for j in range(1,rows+1):
    if (i+j) % 2 == 0:
      print(1,end=" ")
    else:
      print(0,end=" ")
  print()