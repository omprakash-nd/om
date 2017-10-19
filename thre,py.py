from threading import *
import time
 
def handleClient1():
    while(True):
        print "1 Start : %s" % time.ctime()
        time.sleep(5) # wait 5 seconds
        print "1 End : %s" % time.ctime()
          
 
def handleClient2():
    while(True):
        print "2 Start : %s" % time.ctime()
        time.sleep(5) # wait 5 seconds
        print "2 End : %s" % time.ctime()
        
# create threads
t = Timer(10.0, handleClient1)
t2 = Timer(5.0, handleClient2)
 
# start threads
print "THREAD TIME %s"  % time.ctime()
t.start()
t2.start()
