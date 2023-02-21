# Code-Python

> **Warning**
>เป็นการเก็บรวมร่วมโจทย์ เเละฟังชันก์ต่างๆใน python เพื่อไม่ให้ลืม ร่วมไปถึงการใช้งาน เเละทบทวน+เพื่อเปิดอ่านได้ง่าย 

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

##### **6. จงเขียนโปรแกรมเเสดง จำนวนถั่วที่สามารถกำออกมาได้มากที่สุด โดยมี $\color[rgb]{1,0,1}เงื่อนไข$ ว่า ขนาดของมือจะเล็กกว่าขนาดของรูบนกล่องเสมอ โดยมีรูปเเบบ $\color[rgb]{1,0,1}Input$ ดังต่อไปนี้**

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

##### **7. จงเขียนโปรแกรมหาว่า ผู้ชนะและผู้แพ้ใช้เวลาในการนับแกะไปคนละกี่ชั่วโมง กี่นาที กี่วินาที และเวลาที่ทุกคนในกลุ่มใช้ในการนับแกะเฉลี่ยกันเท่ากับกี่ชั่วโมง กี่นาที กี่วินาที**

```Txt
รูปเเบบ Input

- บรรทัดที่ 1 - เวลาที่ใช้ในการนับแกะของผู้ชนะ

- บรรทัดที่ 2 - เวลาที่ใช้ในการนับแกะของผู้แพ้

- บรรทัดที่ 3 - เวลาเฉลี่ยที่ใช้ในการนับแกะของทุกคน
```
>$\color[rgb]{0,1,1}Input$
>
>3
>
>610
>
>580
>
>700

>$\color[rgb]{1,0,1}Output$
>
>Winner : 0 hr 10 min 10 sec
>
>Loser : 0 hr 9 min 40 sec
>
>Average : 0 hr 10 min 30 sec
```Python
lst = [ ] 
n = int(input("")) 
for i in range(0, n):
  ele = int(input()) 
  lst.append(ele) 
#----------------------Average
def Average(lst):
    return sum(lst) / len(lst)  
average = int(Average(lst))
#---------------------- min 
mi = min(lst)
#---------------------- max
ma = max(lst)
#--------------------
import datetime
#----------------------
time_Average  = str(datetime.timedelta(seconds=average))
time_Average  = time_Average.split(':')
del_time_Average = time_Average[1]
del_time_Average1 = time_Average[2]
if del_time_Average[0] == '0':
  time_Average[1] = del_time_Average[-1]
if del_time_Average1[0] == '0':
  time_Average[2] = del_time_Average1[-1]
#----------------------
#print(time_Average)
#----------------------
time_min  = str(datetime.timedelta(seconds=mi))
time_min  = time_min.split(':')
del_time_min = time_min[1]
del_time_min1 = time_min[2]
if del_time_min[0] == '0':
  time_min[1] = del_time_min[-1]
if del_time_min1[0] == '0':
  time_min[2] = del_time_min1[-1]
#----------------------
#print(time_min)
#----------------------
time_max  = str(datetime.timedelta(seconds=ma))
time_max  = time_max.split(':')
del_time_max = time_max[1]
del_time_max1 = time_max[2]
if del_time_max[0] == '0':
  time_max[1] = del_time_max[-1]
if del_time_max1[0] == '0':
  time_max[2] = del_time_max1[-1]
#----------------------
#print(time_max)
#----------------------
print("Winner : %s"%time_max[0],"hr",time_max[1],"min",time_max[2],"sec")
print("Loser : %s"%time_min[0],"hr",time_min[1],"min",time_min[2],"sec")
print("Average : %s"%time_Average[0],"hr",time_Average[1],"min",time_Average[2],"sec")
```
$\color[rgb]{0,1,0}Input$
```Text
7
7690
5683
5679
2565
8765
5633
3451
```
$\color[rgb]{0,1,0}Output$
```Text
Winner : 2 hr 26 min 5 sec
Loser : 0 hr 42 min 45 sec
Average : 1 hr 33 min 58 sec
```
##### **8. จงนำ input มาแปล โดยการแปลงตัวอักษรภาษาอังกฤษเป็นตัวเลขสามารถแปลได้ดังนี้ A=1 B=2 C=3 D=4 E=5 F=6 G=7 H=8 I=9 J=10 K=11 L=12 M=13 N=14 O=15 P=16 Q=17 R=18 S=19 T=20 U=21 V=22 W=23 X=24 Y=25 Z=26 โดยตัวอย่างดังนี้**
>$\color[rgb]{0,1,1}Input$
>
>19 15 18 18 25

>$\color[rgb]{1,0,1}Output$
>
>sorry

```Python
x = list(map(int, input().split()))
y = ''.join(chr(i+96) for i in x)
print(y)
```

##### **9.หาคนที่ได้รับของขวัญจากซานต้ามากที่สุด ตัวอย่างดังนี้**
>$\color[rgb]{0,1,1}Input$
>
>5
>HH
>HH
>N
>N
>HH

>$\color[rgb]{1,0,1}Output$
>
>HH

```Python
#1
number = input()
dictionary = dict()
max_gifts = 0
max_person = None

for i in range(int(number)):
     name = input()
     if name in dictionary:
          dictionary[name] += 1
     else:
          dictionary[name] = 1
          
     if dictionary[name] > max_gifts:
          max_gifts = dictionary[name]
          max_person = name
          
print(max_person)

#2
from collections import defaultdict
number = input()
dictionary = defaultdict(lambda: 0)
max_gifts = 0
max_person = None

for i in range(int(number)):
     name = input()
     dictionary[name] += 1
     
     if dictionary[name] > max_gifts:
          max_gifts = dictionary[name]
          max_person = name
          
print(max_person)
```

##### **10.สร้างนาฬิกาทรายรูปแบบ Star Pattern เเละสร้างกรอบ รูปเเบบ shape ดังตัวอย่างต่อไปนี้**

>$\color[rgb]{0,1,1}Input$
>
>5
>

>$\color[rgb]{1,0,1}Output$

```
* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *
  #####
  #   #
  #   #
  #   #
  #####
```
>$\color[rgb]{0,1,1}Input$
>
>12
>

>$\color[rgb]{1,0,1}Output$

```
* * * * * * * * * * * *
 * * * * * * * * * * *
  * * * * * * * * * *
   * * * * * * * * *
    * * * * * * * *
     * * * * * * *
      * * * * * *
       * * * * *
        * * * *
         * * *
          * *
           *
           *
          * *
         * * *
        * * * *
       * * * * *
      * * * * * *
     * * * * * * *
    * * * * * * * *
   * * * * * * * * *
  * * * * * * * * * *
 * * * * * * * * * * *
* * * * * * * * * * * *
      ############
      #          #
      #          #
      #          #
      #          #
      #          #
      #          #
      #          #
      #          #
      #          #
      #          #
      ############
```
> **Note** เลขคู่เหลื่อมล้ำได้ดังตัวอย่าง input 12
```Python
n=int(input())
for j in range(n, 0 , -1): 
  print(" "*(n-j)+"* "*(j))
for i in range(n): 
  print(" "*(n-1-i)+"* "*(i+1))
if n != 1:
  print(" "*int((n/2))+n*"#")
  for k in range(n-2):
    print(" "*int((n/2))+"#"+(n-2)*" "+"#")
  print(" "*int((n/2))+n*"#")
if n ==1:
  print(" "*int((n/2))+"#")
```

##### **11.คำนวณ BMI โดย ให้รับ Input 2 ตัวแปรดังนี้ 1.ค่าน้ำหนัก ในหน่วยกิโลกรัม 2.ค่าส่วนสูง ในหน่วยเซนติเมตร ดังตัวอย่างนี้**
>$\color[rgb]{0,1,1}Input$
>
>63
>173
>

>$\color[rgb]{1,0,1}Output$
>
>BMI: 21.05

>$\color[rgb]{0,1,1}Input$
>
>50
>170
>

>$\color[rgb]{1,0,1}Output$
>
>BMI: 17.3

```Python
x = int(input())
y = int(input())/100
i = (x)/(y**2)
print("BMI: %g"%round(i,2))
```
