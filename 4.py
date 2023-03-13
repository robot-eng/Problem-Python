str_input =input() #input
del_str = str_input.strip('[,]') # del [ and ] in string
strlis = del_str.split(',') # Make a list and make , disappear
lis = [int(x) for x in strlis] # Convert values in list from str to int
lis.sort(reverse=True) # Sort descending order
for y in lis:
  print(y,end=" ")
