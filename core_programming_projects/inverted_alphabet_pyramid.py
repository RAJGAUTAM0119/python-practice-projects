# Enter the row size for the pattern: 5
# A B C D E D C B A 
#   A B C D C B A 
#     A B C B A 
#       A B A 
#         A 

rows = 5

for i in range(1,rows+1):
  for j in range(i-1):
    print(" ",end=" ")
  for k in range(1,rows-i+2):
    print(chr(64+k),end=" ")
  for l in range(rows-i,0,-1):
    print(chr(64+l),end=" ")
  print()