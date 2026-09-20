# Enter the row size for the pattern: 5
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

rows = 5
ascii_value = 65

for i in range(1,rows+1):
  for j in range(i):
    letter = chr(ascii_value + j )
    print(letter,end=" ")
  print()

# Enter the row size for the pattern: 5
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

for i in range(1,rows+1):
  for j in range(rows-i+1):
    letter = chr(ascii_value + j)
    print(letter,end=" ")
  print()