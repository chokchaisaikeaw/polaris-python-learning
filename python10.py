print ('this is a program to calculate y = ||x|-1|')
print ('please input a number:')
temp = float (input ())
if temp >= 1:
    print (temp-1)
elif temp <1 and temp>0:
    print (1-temp)
elif temp <=0 and temp >=-1:
    print (temp+1)
else:
    print (-temp-1)
