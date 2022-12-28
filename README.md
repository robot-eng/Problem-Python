# Code-Python

##### 1. กำหนดให้ list = [1,2,3,...,25] เขียนโปรเเกรมเปลี่ยนสมาชิกใน list ที่ index เป็นเลขคู่ให้เป็นค่ายกกำลัง 2 จากนั้นพิมค่า list ออกมา
```Python
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
```
Output
```Txt
list : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Even : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
Eeven**2 : [1, 2, 9, 4, 25, 6, 49, 8, 81, 10, 121, 12, 169, 14, 225, 16, 289, 18, 361, 20, 441, 22, 529, 24, 625]
```
