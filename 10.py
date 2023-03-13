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
