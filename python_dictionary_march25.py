##var = {}
##print(var)
##print(type(var))

##var = {"appu",46}
##print(var)
##print(type(var))

##var = {"name":"appu","age":46}
##print(var)
##print(type(var))

##var = {"name":"appu","age":46}
##print(var[0]) #no index based direct data retrieval in dictionary

#in dictionary datas are manipulated or used via key
#dictionary is called key value pair
#because each data we use needs to be stored with specific key
#storing data with key is generally called as "Hashing" or HashTable"

##var = {"name":"appu","age":46}
##print(var["age"])

##var ={"name":"appu","age":46}
##var["name"] = "yuva"
##print(var)

#dictionary is mutable type

##var = {"name":"appu","age":46,"name":"james"}
##print(var)

#keys are unique
#dictionary is called as "un ordered collection"

##var = {"name":"appu",9:33,98.9:"james",("a","B"):"sid",True:"yuvaratna"}
##var["name"] = "puneeth"
##print(var)


##var = {"name":"appu"}
##var["country"] = "india"
##print(var)

##var = {"name":"kohli","team":"rcb"}
##output = var["team"]
##print(output)

##var = {"name":"kohli","team":"rcb"}
##var1 = {"age":29}
##output = var + var1
##print(output)

##var = {"name":"kohli","team":"rcb"}
##var1 = {"age":29}
##var2 = {"lan":"eng"}
##output = {**var,**var1,**var2}
##print(output)


##var = {"name":["virat","dhoni"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##print(var)

##var = {"name":["virat","dhoni"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var["team"][1]
##print(output)

##var = {"name":["virat","dhoni"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##var["name"] [1] = "rohit"
##print(var)

##var = {"name":["virat","dhoni"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var["country"]
##print(output)
##print("welcome")




##var = {"name":["virat","dhoni"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var.get("country")
##print(output)
##print("welcome")

##var = {"name":["virat","dhoni"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var.get("country","sorry key not found")
##print(output)
##print("welcome")

#dictionary is mutable u can make changes

























