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
