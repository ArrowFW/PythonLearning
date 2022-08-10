bread= int(input("Enter Your Number "))
count = 0
while bread>0:
    print(bread%10, end='')
    bread = bread//10
