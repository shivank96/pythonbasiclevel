from array import *
# import array as arr
vals = array('i',[10,20,30,40])
vals1 = array(vals.typecode,[a+1 for a in vals])
for i in vals:
    print(i)
i=0
while(i<len(vals1)):
    print(vals1[i])
    i+=1



