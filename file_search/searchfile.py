import os

file_name = str(raw_input("Enter File Name:"))

cur_dir = os.getcwd()

while True:
    file_list = os.listdir(cur_dir)
    parent_dir = os.path.dirname(cur_dir)

    if file_name in file_list:
        print "File Exists in: ", cur_dir
        filename = file_name
        print "Operations"
        print """0.Search File
1.Write
2.Read
3.Append
4.create a new file
5.Search Word
Other keys for Exit \n """
        check = int(raw_input("Enter Your Choice"))
        
        if check == 1:
            file_name = filename
            i = str(raw_input("Enter your data:")) 
            data = open(file_name,'w')
            data.write(i)
            print "Your data Saved in %r" % file_name
        
        elif check == 2:
            file_name = filename
            data = open(file_name,'r')
            for line in data:
                print line
                sample = line.split(' ') 
                
            data.close()
           
        elif check == 3:
            file_name = filename
            i = str(raw_input("Enter your data:")) 
            data = open(file_name,'a')
            data.write(i)
            data = open(file_name,'r')
            for line in data:
                print line
            data.close()
        
        elif check == 4:
            name = str(raw_input("Enter File name:"))
            data = open(name.strip()+".txt","w")
            print "file created.."
        
        elif check == 5:
            file_name = filename
            name = str(raw_input("Enter the word you search in file.."))
            for word in sample:
                if word == name: 
                    print "True"
                else:
                    print "false"
               
        else:
            print """Your Pressed Wroung Key..!!
Bye..Bye.."""
            exit()

    else:
        if cur_dir == parent_dir: #if dir is root dir
            print "File not found"
            break
        else:
            cur_dir = parent_dir
