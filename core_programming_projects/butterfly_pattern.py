# * - - - - - - - - * 
# * * - - - - - - * * 
# * * * - - - - * * * 
# * * * * - - * * * * 
# * * * * * * * * * * 
# * * * * * * * * * * 
# * * * * - - * * * * 
# * * * - - - - * * * 
# * * - - - - - - * * 
# * - - - - - - - - * 

rows = 5

# Minimum for loop method

for i in range(1,rows+1):
  print("* "*i,end=" ")
  print("  "* (rows-i)*2,end=" ")
  print("* "*i,end=" ")
  print()

for i in range(rows):
  print("* " * (rows-i),end=" ")
  print("  "*i*2,end=" ")
  print("* " * (rows-i),end=" ")
  print()

# Traditional method

# for i in range(1,rows+1):
#   for j in range(i):
#     print("*",end=" ")
#   for k in range(rows-i):
#     print(" ",end=" ")
#   for l in range(rows-i):
#     print(" ", end=" ")
#   for m in range(i):
#     print("*",end=" ")
#   print()

# for i in range(1,rows+1):
#   for j in range(rows-i+1):
#     print("*",end=" ")
#   for k in range(i-1):
#     print(" ",end=" ")
#   for l in range(i-1):
#     print(" ",end=" ")
#   for m in range(rows-i+1):
#     print("*",end=" ")
#   print() 