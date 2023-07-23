# 1
while 1:
    for i in range(1,21):
        if i <=19:print(i,end="+")
        if i == 20: print(i)
    if i == 20:
        break
        
# 2
i1 = []
dis = ["[","","]","+",","," "] # [0 1 2 3 4 5] 
while 1:
    for i in range(1,21):i1.append(i)   
    if i == 20:break
i2 = str(i1)
i3 = i2.replace(dis[0],dis[1]).replace(dis[4],dis[3]).replace(dis[5],dis[1]).replace(dis[2],dis[1])
print(i3)

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
