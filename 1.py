# 1
x = 25
lis,lis3 =[x1 for x1 in range(1,x+1)],[x1 for x1 in range(1,x+1)]
lis1,lis2 = [y for y in lis if y%2 != 0],[lis.index(y) for y in lis if y%2 != 0]
print("list :",lis)
print("Even :",lis1)
for y1 in lis1:
     lis.remove(y1)
for y2 in lis2:
     lis.insert(y2,lis3[y2]**2)
print("Eeven**2 :",lis)

# 2
x = 25
lis =[x1 for x1 in range(1,x+1)]
print("list :",lis)
for y in range(len(lis)):
    if y%2==0:lis[y] = lis[y]**2
print("Index Eeven**2:",lis,end=" ")
