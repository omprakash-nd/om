import os

filename = str(raw_input("Enter Filename"))  
data = str(raw_input("Enter data: "))

name = open(filename,"r")
name.read()
name = open(filename,"w")
name.write(data)
name.close()
