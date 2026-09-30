# Enter the row size for the pattern: 5
#     *     
#     *     
# * * * * * 
#     *     
#     *     

rows = 11

for i in range(1,rows+1):
  for j in range(1,rows+1):
      if  i == ( rows  ) // 2 + 1 or j == ( rows ) // 2 + 1 :
        print("*",end=" ")
      else:
        print(" ",end=" ")
  print()