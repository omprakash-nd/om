import re

s = open("sample.txt", 'r')
data = s.read()
text = re.sub(r'<!.+-->',r' ',(data))

for tag in re.findall(r'<([^/][^>]*)>', text):
    
    if ' ' in tag:

        for attr in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',tag):
            print (attr[0])
            print( '->'+attr[1]+' >'+attr[2])
    else:
        print tag
