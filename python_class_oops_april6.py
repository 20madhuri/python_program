#Python is unstructured programming
#python can be made as structured programming if it follows "class" principles
#class is collection of object
#object is real world enitity
#class is kind of template or wrapper to hold things
#object is anything which  takes memory
#class is mainly to give the property of inheritance or extensibility

##var = "appu"
##print(var)
##
##def fun():
##    print("welcome")
##
##fun()    

##class My_Class:
##
##    var = "appu"
##
##    def fun():
##        print("welcome")
##
##print(My_Class.var)
##My_Class.fun()

##class My_Class:
##
##    var = "appu"
##
##    def fun():
##       print("welcome")
##My = My_Class
##print(My.var)
##My.fun()
#My is called object reference of the "My_Class"
#class without constructor

##class My_Class:
##
##    def new(name):
##        print("hello")
##
##    def fun(name,age):
##        print("welcome")
##My = My_Class
##My.fun("appu",46)
##My.new("appu")
##
class My_Class:

    def __init__(sonu,name,age):

        sonu.name = name
        sonu.age = age

    def new(sonu):
        print(sonu.name)

    def fun(self):
        print(sonu.name, sonu.age)
My = My_Class("sonu",46)
#My_Class is called as constructor class
#My is called as object reference with single instant memory(single instant memory)
#My_Class() will have one hidden object inside
#whenever you create constructor, an attribute called __init__ is created automatically
#we can use that __init__if we need to initialize the data inside the class
#attribute or magic method or dunder method is anything that contain double underscore on either side
#self is similar to My
#My is the object reference for external class
#self is the object reference for internal class
My.fun()
My.new()
































