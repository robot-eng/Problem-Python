# Code-Python

##### **1. กำหนดให้ $\color[rgb]{1,0,1}list$ $\color[rgb]{1,0,1}=$ $\color[rgb]{1,0,1}[1,2,3,...,25]$ เขียนโปรเเกรมเปลี่ยนสมาชิกใน $\color[rgb]{1,0,1}list$ ที่ index เป็นเลขคู่ให้เป็นค่ายกกำลัง 2 จากนั้นพิมค่า list ออกมา**
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
##### **2.จงปริ้นค่า 1+2+3+...+20 โดยใช้ while และ for**
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
c = 0
while (c==0):
    for i in range(1,21):
        i1.append(i)
        c = 1   
for x in range((len(i1)*2)-1):
    if x%2 != 0:i1.insert(x,'+')
for x1 in range(len(i1)):
    print(i1[x1],end="")
"""
i1 = []
while 1:
    for i in range(1,21):i1.append(i)   
    if i == 20:break
for x in range((len(i1)*2)-1):
    if x%2 != 0:i1.insert(x,'+')
for x1 in range(len(i1)):
    print(i1[x1],end="")
"""
```
$\color[rgb]{0,1,0}Output$
```Txt
1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20
```
##### **3. จงรับค่า $\color[rgb]{1,0,1}input$ เช่น $\color[rgb]{1,0,1}6+3$ มาคำนวณโดยกำหนดให้ใช้ได้เเค่ 1 บรรทัด (EX. $\color[rgb]{1,0,1}input$ = 6+3 $\color[rgb]{1,0,1}output$ = 9)**

```Python
print(eval(input(" ")))
```
$\color[rgb]{0,1,0}Input$
```Text
9+3
```
$\color[rgb]{0,1,0}Output$
```Text
12
```
##### **4. จงเขียนโปรแกรมเพื่อแปลง list เป็น array แล้วเรียงจากมากไปน้อย โดยตัวอย่างการเเสดง $\color[rgb]{1,0,1}input$ เเละ $\color[rgb]{1,0,1}Output$ ดังนี้**
>$\color[rgb]{0,1,1}Input$
>
>[230,450,-270,180,860,100]

>$\color[rgb]{1,0,1}Output$
>
>860 450 230 180 100 -270
```Python
str_input =input() #input
del_str = str_input.strip('[,]') # del [ and ] in string
strlis = del_str.split(',') # Make a list and make , disappear
lis = [int(x) for x in strlis] # Convert values in list from str to int
lis.sort(reverse=True) # Sort descending order
for y in lis:
  print(y,end=" ")
```
##### **5. จงเขียนโปรแกรมเเสดงสีของลูกบอลที่มีอยู่ในถังที่หนึ่งและสอง แต่ไม่มีอยู่ในถังที่สาม (กรณีที่ไม่มีลูกบอลสีใดเลยที่ตรงตามเงื่อนไข ให้ผลลัพธ์ออกเป็น none)**
>$\color[rgb]{0,1,1}Input$
>
>b1=[red,green,blue] b2=[black,green,white] b3=[blue]

>$\color[rgb]{1,0,1}Output$
>
>green

>$\color[rgb]{0,1,1}Input$
>
>b1=[pink,yellow] b2=[brown,pink,green] b3=[orange,pink]

>$\color[rgb]{1,0,1}Output$
>
>none

>$\color[rgb]{0,1,1}Input$
>
>b1=[blue,orange,white,brown] b2=[red,orange,white,brown] b3=[orange,blue,green]

>$\color[rgb]{1,0,1}Output$
>
>white,brown

```Python
x,y,z = input().split()
a = x[4::].split("]")
a1 = a[0].split(",")
b = y[4::].split("]")
b1 = b[0].split(",")
c = z[4::].split("]")
c1 = c[0].split(",")
c2,c3 = [],[]
for xx in a1:
  try:
    c2.append(b1[b1.index(xx)])
  except:
    pass
for yy in c2:
  if yy not in c1:
    c3.append(yy)
for x1 in range((len(c3)*2)-1):
    if x1%2 != 0:c3.insert(x1,',')
for x2 in range(len(c3)):
    print(c3[x2],end="")
if str(c3) == "[]":
  print('none')
```
##### **6. จงเขียนโปรแกรมเเสดง จำนวนถั่วที่สามารถกำออกมาได้มากที่สุด โดยมี$\color[rgb]{1,0,1}]เงื่อนไข$ว่า ขนาดของมือจะเล็กกว่าขนาดของรูบนกล่องเสมอ โดยมีรูปเเบบ $\color[rgb]{1,0,1}Input$ ดังต่อไปนี้**
```Txt
รูปเเบบ Input

- บรรทัดแรก เส้นผ่านศูนย์กลางของรูที่กล่อง

- บรรทัดสอง ขนาดของมือลิง

- บรรทัดสาม จำนวนถั่วภายในกล่อง

- บรรทัดสี่ ขนาดมือที่เพิ่มขึ่นต่อถั่ว 1 ชิ้น

```
```Python
a =  float(input())
b =  float(input())
c =  float(input()) 
d = float(input())
l = 0
while 1:
  l = l+1
  cc = (d*l)+b
  if cc>=a:
    break
print(l)
```
$\color[rgb]{0,1,0}Input$
```Text
6.0
3.5
5
0.5
```
$\color[rgb]{0,1,0}Output$
```Text
5
```
