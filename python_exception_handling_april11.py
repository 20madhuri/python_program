##var = 10/0
##print(var)
##print("welcome")
##Exception ---> ZeroDivisionError, IndexError,ArithmericError

##try:
##    var = 10/0
##    print(var)
##except:
##    print("hai")
##print("welcome")    

##var = "a" + 10
##print(var)

##try:
##    var = "a" + 10
##    print(var)
##except: #default exception block
##    print("sorry")
##print("welcome")

##try:
##    var = 10/0
##    print(var)
##    
##except TypeError:
##    print("sorry try again")
##
##except ZeroDivisionError:
##    print("sorry for the error")
##
##except: #default exception block
##    print("sorry")



##try:   
##    var = 10/0
##    print(var)
##    
##except TypeError as exi:
##    print(exi)
##
##except ZeroDivisionError as hello:
##    print(hello)
##
##except: #default exception block
##    print("sorry")

##try:
##    var = 10/0
##    print(var)
##
##except Exception as ex:
##    print(ex)

##try:
##    var = 101/5
##    print(var)
##
##except Exception as ex:
##    print(ex)
##
##else:
##    print("my else block")
##finally:
##    print("my block of finally")
##

##var = 10
##try:
##    if var>5:
##        raise IndexError()
##
##except IndexError:
##    print("sorry")
##

##var = 10
##try:
##    if var>5:
##        raise IndexError()
##
##except IndexError as ex:
##    print(ex)
##

##var = 10
##try:
##    if var>5:
##        raise IndexError("my raising of error")
##
##except IndexError as ex:
##    print(ex)
##
##

##class Netzwerk_Error(Exception):
##    pass
##var = 10
##try:
##    if var>5:
##        raise Netzwerk_Error()
##
##except Netzwerk_Error:
##    print("sorry")

class Netzwerk_Error(Exception):
    my_error = "user defined exception"
var = 10
try:
    if var>5:
        raise Netzwerk_Error()

except Netzwerk_Error as ex:
    print(ex.my_error)








































