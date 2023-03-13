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
