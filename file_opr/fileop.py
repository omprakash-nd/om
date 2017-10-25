filename = str(raw_input("Enter Filename"))  
data = str(raw_input("Enter data: "))

name = open(filename,"r")
name = open(filename,"w")
name.read(data)
name.write(data)
name.close()
