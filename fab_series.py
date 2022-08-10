#f= -1
#s= 1
#count = 1

#while count<=8:
#    t = f+s
#    f = s
#    s = t
#    count+=1
#    print(t)


f = -1
s = 1
count = 1
while count<=8:
    print(f+s)
    s = f+s
    f = s-f
    count+=1
