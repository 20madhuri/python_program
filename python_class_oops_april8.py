##class My_Class(object):
##
##    def __init__(self):
##        print("hello")
##
##    def fun(self):
##        print("welcome to python")
##    def fun(self):
##        print("my second function")
##
##my = My_Class()
##my.fun()


##class My_Class(object):
##
##    def __int__(self):
##        print("hello")
##
##    def fun(self):
##        print("welcome to python")
##    def new(self):
##        print("my second function")
##
##my = My_Class()
##my.fun()
##my.new()
#Access specifier ---Private,public(in python public isnt available)


##class My_Class:
##
##    def __init__(self,name,age):
##
##        self.name = name
##        self.age = age
##
##    def one(self):
##        print("one",self.name)
##
##class Second_Class(My_Class): #single inheritance
##
##    def two(self):
##
##        print("two",self.name,self.age)
##my = Second_Class("appu",46)
##my.one()
##my.two()
##

##class My_Class:
##
##    def __init__(self,name,age):
##
##        self.name = name
##        self.age = age
##
##    def two(self):
##        print("one",self.name)
##
##class Second_Class(My_Class): #single inheritance
##
##    def two(self):
##
##        print("two",self.name,self.age)
##        
##my = Second_Class("appu",46)
##my.two()
##my_parent = My_Class("appu",44)
##my.two()

#algorithm(interview qn)

##class A:
##    def fun(self):
##        print("A")
##
##class B(A):
##    def fun(self):
##        print("B")
##
##class C(A):
##    def fun(self):
##        print("c")
##
##class D(C,B):
##    pass
###def fun(self):
###print("d")
##
##d = D()
##d.fun()

#Method Resolution order
#near by search


























        
