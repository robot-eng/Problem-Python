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
