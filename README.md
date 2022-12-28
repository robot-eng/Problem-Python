# Code-Python

#### **1. กำหนดให้ $\color[rgb]{1,0,1}list$ $\color[rgb]{1,0,1}=$ $\color[rgb]{1,0,1}[1,2,3,...,25]$ เขียนโปรเเกรมเปลี่ยนสมาชิกใน $\color[rgb]{1,0,1}list$ ที่ index เป็นเลขคู่ให้เป็นค่ายกกำลัง 2 จากนั้นพิมค่า list ออกมา**
```Python
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
```
$\color[rgb]{1,0,1}OR$
```Python
# 2
x = 25
lis =[x1 for x1 in range(1,x+1)]
print("list :",lis)
for y in range(len(lis)):
    if y%2==0:lis[y] = lis[y]**2
print("Index Eeven**2:",lis,end=" ")
```
$\color[rgb]{0,1,0}Output$
```Txt
# 1
list : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Index Even : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
Index Even**2 : [1, 2, 9, 4, 25, 6, 49, 8, 81, 10, 121, 12, 169, 14, 225, 16, 289, 18, 361, 20, 441, 22, 529, 24, 625]
```
```Txt
# 2
list : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Index Even**2: [1, 2, 9, 4, 25, 6, 49, 8, 81, 10, 121, 12, 169, 14, 225, 16, 289, 18, 361, 20, 441, 22, 529, 24, 625]
```
#### **2.จงปริ้นค่า 1+2+3+...+20 โดยใช้ while และ for**
```Python
# 1
while 1:
    for i in range(1,21):
        if i <=19:print(i,end="+")
        if i == 20: print(i)
    if i == 20:
        break
```
$\color[rgb]{1,0,1}OR$
```Python
# 2
i1 = []
dis = ["[","","]","+",","," "] # [0 1 2 3 4 5] 
while 1:
    for i in range(1,21):i1.append(i)   
    if i == 20:break
i2 = str(i1)
i3 = i2.replace(dis[0],dis[1]).replace(dis[4],dis[3]).replace(dis[5],dis[1]).replace(dis[2],dis[1])
print(i3)
```
$\color[rgb]{1,0,1}OR$
```Python
# 3
i1 = []
while 1:
    for i in range(1,21):i1.append(i)   
    if i == 20:break
for x in range((len(i1)*2)-1):
    if x%2 != 0:i1.insert(x,'+')
for x1 in range(len(i1)):
    print(i1[x1],end="")
```
$\color[rgb]{0,1,0}Output$
```Txt
1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20
```
