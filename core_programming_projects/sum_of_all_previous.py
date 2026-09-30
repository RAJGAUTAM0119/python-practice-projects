# Given Input: [1, 2, 3, 4]

# Expected Output:
# Cumulative Sum: [1, 3, 6, 10]

given_array = [1,2,3,4]
expected_array =[]
num = 0

for i in given_array:
  num += i
  expected_array.append(num)
print(expected_array)