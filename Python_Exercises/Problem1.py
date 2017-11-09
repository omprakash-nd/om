from sys import argv
import os,re

script, input_file = argv

class checkHTML:

    def input_check(self,input_file):
        isSuccess = False
        try:
            filename = input_file
            self.get_FileName(filename)
        except IndexError:
            print 'You failed to provide filename as input on the command line!'
            isSuccess = True
            return isSuccess
    
    def get_FileName(self,fname):
        isSuccess = False
        try:
            file_name = fname
            if '.html' in file_name or '.txt' in file_name:
                current_file = open(file_name)
                if os.stat(file_name).st_size != 0:
                    self.fileRead = current_file.read()
                    self.check_Tags()
                else:
                    print "%s is empty file" %file_name
            else:
                print'%s does not exist in current directory' %file_name
            isSuccess = True            
        except (RuntimeError, TypeError, NameError):
            print 'You failed to provide filename as input on the command line!'
            isSuccess = True
            return isSuccess

    def check_Tags(self):
        isSuccess = False
        try:
            self.HtmlTags=[]
            self.HtmlAttributes=[]
            self.HtmlAttributeValues=[]
            texts = re.sub(r'<!.+-->',r' ',(self.fileRead))
            self.check_Attributes()
            #print texts
            return texts
        except (RuntimeError, TypeError, NameError):
            isSuccess = True
            return isSuccess

    def check_Attributes(self, ):
        isSuccess = False  
        try:
            text = self.check_Tags()
            #print text
            for tags in re.findall(r'<([^/][^>]*)>',text):
                if ' ' in tags:
                    for attribute in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',tags):
                        self.HtmlTags.append(attribute[0])
                        #print attribute[0]
                        self.HtmlAttributes.append(attribute[1])
                        self.HtmlAttributeValues.append(attribute[2])
                    self.display()
                else:
                    self.HtmlTags.append(tags)        
            self.HtmlTags =filter(None, self.HtmlTags)
            isSuccess = True
            return tags
        except(RuntimeError, TypeError, NameError):
            pass
            isSuccess = False  
            return isSuccess
            
    def display(self):
        isSuccess = False
        try:
            choice = int(raw_input('1 for tags , 2 for attributes , 3 for attribute values 4 for search attribute value 5.exit \n Enter number:'))
            if choice == 1:
                for tag in self.HtmlTags:
                    print tag
                self.display()
                    
            elif choice == 2:
                for attrib in self.HtmlAttributes:
                    print attrib
                self.display()
                   
            elif choice == 3:
                for attrib,values in map(None,self.HtmlAttributes,self.HtmlAttributeValues):
                    print "%s = %s"%(attrib,values)
                self.display()
                
            elif choice == 4:
                attrib=str(raw_input('enter attribe ='))
                if attrib in self.HtmlAttributes:
                    index_value=self.HtmlAttributes.index(attrib)
                    print "Attribute value:",self.HtmlAttributeValues[index_value]
                else:
                    print "Values doesn't match"
                    self.display()
            elif choice == 5:
                exit()
                
            else:
                print "Enter correct number"
                self.display()
                isSuccess = True  
        except (RuntimeError, TypeError, NameError):
            pass 
            return isSuccess    

html = checkHTML()
html.input_check(input_file)  
