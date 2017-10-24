nameList=["Nagarani","Prabu","Om"]
message="""I just tried how to merge email And successfully merge"""

for name in nameList:

    names = open("names.txt","w")
    names.write(name)
    names = open("names.txt","r")
    
    mail= "Dear" + " "+name +" "+ message
    mailFile = open(name.strip()+".txt","w")
    mailFile.write(mail)
    mailFile.close()
    print mail

