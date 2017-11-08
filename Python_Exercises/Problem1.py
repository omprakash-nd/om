from sys import argv
import os,re

script,filename =argv

class checkHTML:
            
    def get(self):
        if '.html' in filename or '.txt' in filename:
            txt = open(filename)
            if os.stat(filename).st_size != 0:
                self.data = txt.read()      
            else:
                print "%s is empty file" %filename
        else:
            print ' %s does not exist in current directory' %filename

    def form(self):
        self.tags=[]
        self.attrb=[]
        self.attrval=[]
        text = re.sub(r'<!.+-->',r' ',(self.data))
        for tag in re.findall(r'<([^/][^>]*)>', text):
            if ' ' in tag:
                for attr in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',tag):
                    self.tags.append(attr[0])
                    self.attrb.append(attr[1])
                    self.attrval.append(attr[2])
            else:
                self.tags.append(tag)        
        self.tags =filter(None, self.tags)        
        
    def display(self):
        try:
            choice = int(raw_input('1 for tags , 2 for attributes , 3 for attribute values 4\n Enter number:'))
            if choice==1:
                for i in self.tags:
                    print i
                self.display()
                    
            elif choice==2:
                for i in self.attrb:
                    print i
                self.display()
                   
            elif choice==3:
                for i in self.attrval:
                    print i
                self.display()
                
            elif choice == 4:
                att=str(raw_input('enter attribe ='))
                if att in self.attrb:
                    i=self.attrb.index(att)
                    print i
                    print self.attrval[i]
                else:
                    print "Values doesn't match"
                    self.display()
                
            else:
                print "Enter correct number"
                self.display()
        except:
            print "Errors Occured.. Tryagain.", 
            

    def check():
        ans=raw_input("Do you want to do continue..(y/n)\n").lower()
        if ans=='y':
            self.display()
        elif ans=='n':
            print ("Thank you for using PostBank we value you. Have a good day")
            time.sleep(1)
            exit()
        elif ans!='y' and ans!='n':
            print "Unknown key pressed, please choose either 'N' or 'Y'"
            self.check()

            
html = checkHTML()
html.get()
html.form()
html.display()
