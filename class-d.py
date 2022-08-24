class Parent:
    i=100 #class variable
    def __init__(self):
        self.j=50 #instance variable


class Child(Parent):
    def m1(self):
        print(self.i)
        print(self.j)
        print("using super",super().i)
        #print("using super",super().j)

c=Child()
c.m1()
