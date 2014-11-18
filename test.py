def average(x, y, z):
 avg = float(x + y + z)/3
 if avg<=5:
  q=0
 else:
  q=1
 print "elment " + str(i) + " = " + str(q)

Number = [1,4,6,3,6,23,34,5,1,3]
i,l = 0,len(Number)
while (i<l):
 if i==0:
  average(Number[i], Number[i+1], Number[i+2])
 elif i==l-1:
  average(Number[i], Number[i-1], Number[i-2])
 else:
  average(Number[i], Number[i-1], Number[i+1])
 i=i+1

