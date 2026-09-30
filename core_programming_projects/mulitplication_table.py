# 1	2	3	4	5	6	7	8	9	10	
# 2	4	6	8	10	12	14	16	18	20	
# ...
# 10	20	30	40	50	60	70	80	90	100


rows = 10

for i in range(1,rows+1):
  for j in range(1,rows+1):
    print(i*j,end="\t")
  print()