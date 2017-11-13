import sys
import os,re

class CheckHTML():

    def get_FileName(self,filename):
        try:
            if '.html' in filename or '.txt' in filename:
                if os.stat(filename).st_size != 0:
                    current_file = open(filename)
                    self.file_name = filename
                    fileRead = current_file.read()
                    self.reading = fileRead
                else:
                    print '%s is empty file' %filename
            else:
                print'%s does not exist in current directory' %filename
        except IndexError:
            print 'You failed to provide filename as input on the command line!'
        return filename

    def check_Attributes(self):
        try:
            remove_params = re.sub(r'<!.+-->',r' ',self.reading)
            self.texts = remove_params
            
            for tags in re.findall(r'<([^/][^>]*)>',self.texts):
                if ' ' in tags:
                    for attribute in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',tags):
                        HtmlTags.append(attribute[0])
                        self.htmltags = HtmlTags
                        HtmlAttributes.append(attribute[1])
                        self.htmlAttributes = HtmlAttributes
                        HtmlAttributeValues.append(attribute[2])
                        self.htmlAttributeValues = HtmlAttributeValues
                else:
                    HtmlTags.append(tags)
            HtmlTags =filter(None, HtmlTags)

        except:
            pass
        return HtmlTags

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
                for tagg in self.htmltags:
                    print tagg
                self.display()

            elif choice == 2:
                for attrib in self.htmlAttributes:
                    print attrib
                self.display()

            elif choice == 3:
                for attrib,values in map(None, self.htmlAttributes,self.htmlAttributeValues):
                    print "%s = %s"%(attrib,values)
                self.display()

            elif choice == 4:
                attrib = str(raw_input('enter attribe ='))
                if attrib in self.htmlAttributes:
                    index_value = self.htmlAttributes.index(attrib)
                    print "Attribute value:",self.htmlAttributeValues[index_value]
                else:
                    print "Values doesn't match"
                self.display()
            elif choice == 5:
                sys.exit()
            else:
                print "Enter correct number"
                self.display()
        except Exception as exception:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
            isSuccess = False
            pass
        return isSuccess
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        html = CheckHTML()
        html.get_FileName(sys.argv[1])
        html.check_Attributes()
        html.display()

