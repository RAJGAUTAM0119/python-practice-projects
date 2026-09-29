# Enter the row size for the pattern: 5
# *                 * 
# * *             * * 
# *   *         *   * 
# *     *     *     * 
# *       * *       * 
# *       * *       * 
# *     *     *     * 
# *   *         *   * 
# * *             * * 
# *                 * 

rows = 5

# Traditional method

for i in range(1,rows+1):
  for j in range(i):
    if i == 1 or j == 0 or j - i == -1 :
      print("*",end=" ")
    else:
      print(" ",end=" ")
  for k in range(2 * (rows - i)):
    print(" ", end=" ")
  for l in range(i):
    if i == 1 or l == 0 or l - i == -1 :
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

for i in range(1,rows+1):
  for j in range(rows-i+1):
    if j == 0 or i+j == 5:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  for k in range(2 * ( i-1 )):
    print(" ", end=" ")
  for l in range(rows-i+1):
    if l == 0 or i + l == 5:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()