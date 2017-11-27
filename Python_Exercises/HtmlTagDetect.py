import sys
import os,re

class CheckHTML():

    def check_fileformat(self,filename):
        isSuccess = True
        try:
            if '.html' in filename or '.txt' in filename:
                if os.stat(filename).st_size != 0:
                   #print "filename correct format"
                    isSuccess = True
                else:
                    print '%s is empty file' %filename
                    isSuccess = False
            else:
                print'%s does not exist in current directory' %filename
                isSuccess = False
        except IndexError:
            isSuccess = False
            print 'You failed to provide filename as input on the command line!'
        return filename,isSuccess

    def open_file(self,filename,isSuccess):
        try:
            if isSuccess == True:
                current_file = open(filename)
                fileRead = current_file.read()
                self.reading = fileRead
            else:
                isSuccess = False
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return fileRead,isSuccess

    def check_fileAttributes(self,filename,isSuccess):
        if isSuccess == True: 
            try: 
                HtmlTags=[]
                HtmlAttributes=[]
                HtmlAttributeValues=[]
                remove_params = re.sub(r'<!.+-->',r' ',filename)
                self.texts = remove_params
                
                for tags in re.findall(r'<([^/][^>]*)>',self.texts):
                    if ' ' in tags:
                        for attribute in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',tags):
                            HtmlTags.append(attribute[0])
                            HtmlTags =filter(None, HtmlTags)
                            self.htmltags = HtmlTags
                            HtmlAttributes.append(attribute[1])
                            self.htmlAttributes = HtmlAttributes
                            HtmlAttributeValues.append(attribute[2])
                            self.htmlAttributeValues = HtmlAttributeValues
                    else:
                        HtmlTags.append(tags)

            except Exception as exception:
                isSuccess = False
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(exception).__name__, exception.args)
                print message
            return HtmlTags, isSuccess

    def display(self,isSuccess):
        if isSuccess == True:
            try:
                choice = int(raw_input("""
    1 for tags,
    2 for attributes,
    3 for attribute values,
    4 for search attribute value,
    5.exit
        Enter number:"""))
                if choice == 1:
                    for tag in self.htmltags:
                        print tag
                    self.display(isSuccess)

                elif choice == 2:
                    for attrib in self.htmlAttributes:
                        print attrib
                    self.display(isSuccess)

                elif choice == 3:
                    for attrib,values in map(None, self.htmlAttributes,self.htmlAttributeValues):
                        print "%s = %s"%(attrib,values)
                    self.display(isSuccess)

                elif choice == 4:
                    attrib = str(raw_input('enter attribe ='))
                    if attrib in self.htmlAttributes:
                        index_value = self.htmlAttributes.index(attrib)
                        print "Attribute value:",self.htmlAttributeValues[index_value]
                    else:
                        print "Values doesn't match"
                    self.display(isSuccess)

                elif choice == 5:
                    sys.exit()
                else:
                    print "Enter correct number"
                    self.display(isSuccess)
    
            except Exception as exception:
                isSuccess = False
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(exception).__name__, exception.args)
                print message
        return isSuccess
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        html = CheckHTML()
        arg1, arg2 = html.check_fileformat(sys.argv[1])
        if arg2:
            arg3, arg4 = html.open_file(arg1,arg2)
        if arg4:
            arg5,arg6 = html.check_fileAttributes(arg3,arg4)
        if arg6:
            html.display(arg6)