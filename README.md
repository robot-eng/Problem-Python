# Problem-Python

> **Warning** เป็นการเก็บรวมร่วมโจทย์ เเละฟังชันก์ต่างๆใน python เพื่อไม่ให้ลืม ร่วมไปถึงการใช้งาน ทบทวน เเละเพื่อสะดวกต่อการเปิดอ่านได้ง่าย 

##### **1. กำหนดให้ list = [1,2,3,...,25] เขียนโปรเเกรมเปลี่ยนสมาชิกใน list ที่ index เป็นเลขคู่ให้เป็นค่ายกกำลัง 2 จากนั้นพิมค่า list ออกมา**

Output
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

Output
```Txt
1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20
```

##### **3. จงรับค่า input เช่น 6+3 มาคำนวณโดยกำหนดให้ใช้ได้เเค่ 1 บรรทัด (EX. input = 6+3 / output = 9)**

```Python
print(eval(input(" ")))
```
Input
```Text
9+3
```
Output
```Text
12
```

##### **4. จงเขียนโปรแกรมเพื่อแปลง list เป็น array แล้วเรียงจากมากไปน้อย โดยตัวอย่างการเเสดง input เเละ Output ดังนี้**

Input
```
[230,450,-270,180,860,100]
```
Output
```
860 450 230 180 100 -270
```
##### **5. จงเขียนโปรแกรมเเสดงสีของลูกบอลที่มีอยู่ในถังที่หนึ่งและสอง แต่ไม่มีอยู่ในถังที่สาม (กรณีที่ไม่มีลูกบอลสีใดเลยที่ตรงตามเงื่อนไข ให้ผลลัพธ์ออกเป็น none)**

Input
```
b1=[red,green,blue] b2=[black,green,white] b3=[blue]
```
Output
```
green
```
Input
```
b1=[pink,yellow] b2=[brown,pink,green] b3=[orange,pink]
```
Output
```
none
```
Input
```
b1=[blue,orange,white,brown] b2=[red,orange,white,brown] b3=[orange,blue,green]
```
Output
```
white,brown
```

##### **6. จงเขียนโปรแกรมเเสดง จำนวนถั่วที่สามารถกำออกมาได้มากที่สุดโดยมีเงื่อนไขว่า ขนาดของมือจะเล็กกว่าขนาดของรูบนกล่องเสมอ โดยมีรูปเเบบ Input ดังต่อไปนี้**

```Txt
รูปเเบบ Input

- บรรทัดแรก เส้นผ่านศูนย์กลางของรูที่กล่อง

- บรรทัดสอง ขนาดของมือลิง

- บรรทัดสาม จำนวนถั่วภายในกล่อง

- บรรทัดสี่ ขนาดมือที่เพิ่มขึ่นต่อถั่ว 1 ชิ้น

```
Input
```Text
6.0
3.5
5
0.5
```
Output
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
>Input
>
>3
>
>610
>
>580
>
>700

>Output
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
Input
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
Output
```Text
Winner : 2 hr 26 min 5 sec
Loser : 0 hr 42 min 45 sec
Average : 1 hr 33 min 58 sec
```
##### **8. จงนำ input มาแปล โดยการแปลงตัวอักษรภาษาอังกฤษเป็นตัวเลขสามารถแปลได้ดังนี้ A=1 B=2 C=3 D=4 E=5 F=6 G=7 H=8 I=9 J=10 K=11 L=12 M=13 N=14 O=15 P=16 Q=17 R=18 S=19 T=20 U=21 V=22 W=23 X=24 Y=25 Z=26 โดยตัวอย่างดังนี้**
>Input
>
>19 15 18 18 25

>Output
>
>sorry

```Python
x = list(map(int, input().split()))
y = ''.join(chr(i+96) for i in x)
print(y)
```

##### **9.หาคนที่ได้รับของขวัญจากซานต้ามากที่สุด ตัวอย่างดังนี้**
>Input
>
>5
>HH
>HH
>N
>N
>HH

>Output
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

>Input
>
>5
>

>Output

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
>Input
>
>12
>

>Output

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
>Input
>
>63
>173
>

>Output
>
>BMI: 21.05

>Input
>
>50
>170
>

>Output
>
>BMI: 17.3

```Python
x = int(input())
y = int(input())/100
i = (x)/(y**2)
print("BMI: %g"%round(i,2))
```
##### **12.ให้แสดงตัวอักษร ที่เกินมาจาก จำนวน n โดย n คือจำนวนตัวอักษรของข้อความที่สั้นที่สุด ซึ่งรวมถึงช่องว่างภายในข้อความด้วยให้รับค่ามาเป็นข้อความสองชุด**

>Input
>
>Aa Bb...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zz
> 
>CookIE Run

>Output


>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zz = 6

>Input
>
> HelloDevlaB
>
> loveyouto YouDDD

>Output
>
> ouDDD = 5

```Python
#Output Example
a = input()
b = input()
a1 = len(a)
b1 = len(b)
if a1 > b1 :
  c = a[b1::]
  print(c,"=","%d"%(len(c)))
elif a1 < b1 :
  c = b[a1::]
  print(c,"=","%d"%(len(c)))
else:
  print("no surplus")
```
