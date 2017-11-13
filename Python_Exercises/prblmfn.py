from sys import argv
import os,re

#script, input_file = argv

class CheckHTML():

    def get_FileName(self, filename):
        try:
            if '.html' in filename or '.txt' in filename:
                print os.stat(filename).st_size
                if os.stat(filename).st_size != 0:
                    current_file = open(filename)
                    self.file_name = filename
                    print (filename)
                    fileRead = current_file.read()
                    self.reading = fileRead
                else:
                    print "%s is empty file" %self.file_name
            else:
                print'%s does not exist in current directory' %self.file_name           
        except IndexError:
            print 'You failed to provide filename as input on the command line!'
        return filename

    def is_prime(number):
        """Return True if *number* is prime."""
        for element in range(number):
            if number % element == 0:
                return False
        
        return True

    def test(self):
        self.message = 'Hello world'

    def check_Tags(self):
        try:
            self.HtmlTags=[]
            self.HtmlAttributes=[]
            self.HtmlAttributeValues=[]
            remove_params = re.sub(r'<!.+-->',r' ',self.reading)
            self.texts = remove_params
        except :
           pass
        return remove_params 

    def check_Attributes(self):
        try:
            for tags in re.findall(r'<([^/][^>]*)>',self.texts):
                if ' ' in tags:
                    for attribute in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',tags):
                        self.HtmlTags.append(attribute[0])
                        self.HtmlAttributes.append(attribute[1])
                        self.HtmlAttributeValues.append(attribute[2])
                    self.display()
                else:
                    self.HtmlTags.append(tags)
            self.HtmlTags =filter(None, self.HtmlTags)   
        except:
            pass
        return tags
    
    def display(self):
        isSuccess = True
        try:
            choice = int(raw_input("""
1 for tags,
2 for attributes,
3 for attribute values,
4 for search attribute value,
5.exit
Enter number:"""))
            if choice == 1:
                for tagg in self.HtmlTags:
                    print tagg
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
                sys.exit(0)
            else:
                print "Enter correct number"
                self.display() 
        except:
            isSuccess = False
            print 'Your process error occured..'
            sys.exit(0)
        return isSuccess


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(str(sys.argv[1]))

