##print("hello")
##print("welcome to my programmimg")

##def My_Fun(): #function definition without argument or signature or parameter


##print("hello")
##print("welcome to my programming")

##My_Fun() #Function calling

##def My_Fun(name): #function definition with argument or signature or parameter
##
##    print("hello",name)
##    print("welcome to programming")
##
##My_Fun("papa") #function calling
##My_Fun("appu")
##My_Fun(4)

##def My_Fun(name,country): #function definition with argument or signature or parameter
##
##      if isinstance(name,str) and isinstance(country,str):
##          print("hello",name,"from",country)
##          print("welcome to my programming")
##My_Fun("appu","India") #function calling
##My_Fun("papa","banglore")
##My_Fun("manju",4)


##def My_Fun(name,country): #function definition with argument or signature or parameter
##
##    if isinstance(name,str):
##       if isinstance(country,str):
##         print("hello",name,"from",country)
##         print("welcome to my programming")
##My_Fun("appu","India") #function calling
##My_Fun("papa","banglore")

##def My_Fun(name,country): #function definition with argument or signature or parameter
##
##    if isinstance(name,str):
##       if isinstance(country,str):
##         print("hello",name,"from",country)
##         print("welcome to my programming")
##         
##My_Fun(country = "india", name = "appu") #function calling
##My_Fun("papa","banglore")

##def My_Fun(name,country="india"): #function definition with default argument or signature or parameter
##
##    if isinstance(name,str):
##       if isinstance(country,str):
##         print("hello",name,"from",country)
##         print("welcome to my programming")
##         
###function calling
##My_Fun("appu")
##My_Fun("abd","south africa")

##def My_Fun(name,country=None): #function definition with default argument or signature or parameter
##
##    
##         print("hello",name,"from",country)
##         print("welcome to my programming")
##         
###function calling
##My_Fun("appu")
##My_Fun("abd","south africa")

##def My_Fun(name="virat",country=None): #function definition with default argument or signature or parameter
##
##    
##         print("hello",name,"from",country)
##         print("welcome to my programming")
##
##My_Fun()        
##My_Fun("appu")
##My_Fun("abd","south africa")

##def My_Fun(name="virat",country): #function definition with default argument or signature or parameter
##
##    
##         print("hello",name,"from",country)
##         print("welcome to my programming")
##
##My_Fun()        


#april5

##def Student_Passed(*names):
##
##    print(names)
##Student_Passed("dhoni")
##Student_Passed("kohli","sachin")
##

#*args means it can take any number of arguments
#output will be in the form of tuple

##def Student_Passed(**names):
##
##    print(names)
##
##Student_Passed(name = "dhoni")
##Student_Passed(name = "kohli",age = 33)

#**args means data with keys
#output will be in the form of dictionary

##def Student_Mark(eng,math,student_name):
##
##    total = eng + math
##    return
##print(Student_Mark(40,50,"dhoni"))

##def Student_Mark(eng,math,student_name):
##
##    total = eng + math
##    return
##    print("welcome")
##
##output = Student_Mark(40,50,"dhoni")
##print(output)

##def Student_Mark(eng,math,student_name):
##
##    total = eng + math
##    return total
##    print("welcome")
##
##output = Student_Mark(40,50,"dhoni")
##print(output)

##def Student_Mark(eng,math,student_name):
##
##    total = eng + math
##    return total,student_name
##    print("welcome")
##
##output = Student_Mark(40,50,"dhoni")
##print(output)




##def Student_Mark(eng,math,student_name):
##
##    total = eng + math
##    return total,student_name
##    print("welcome")
##
##output,output1 = Student_Mark(40,50,"dhoni")
##print(output)
##print(output1)


#scoping

##var = 100 #outside variable (global)
##def fun():
##    var = 10 #local variable
##    print(var)
##print(var)
##fun()
##print(var)

##var = 100 #outside variable(global)
##def fun():
##    global var
##    var = 10 #local variable
##    print(var)
##print(var)
##fun()
##print(var)

##def fun():
##
##    print("hello")
##    fun()
##fun()

##counter = 0
##def fun():
##    global counter
##    print("hai",counter)
##    counter = counter + 1
##    fun()
##fun()    

##counter = 0
##def  fun():
##    global counter
##    print("hello",counter)
##    counter = counter + 1
##    if counter == 101:
##        return
##    fun()
##fun()    

##counter = 0
##def fun():
##    global counter
##    print("hello",counter)
##    counter = counter + 1
##    while counter < 101:
##        fun()
##fun()        

##counter = 0
##def fun():
##    global counter
##    print("hello",counter)
##    counter = counter + 1
##    if counter < 101:
##        fun()
##fun()        
##        












