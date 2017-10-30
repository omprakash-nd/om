import os
import datetime
import MySQLdb

class blood:
  
    def donorinfo(self):
        try:
            self.name = str(raw_input("Enter Name:"))
            self.age = int(raw_input("Enter Age:"))
            self.contact = int(raw_input("Contact Number:"))
            if self.contact < 9 or self.contact > 11:
                self.city = str(raw_input("Enter City:"))
                self.state = str(raw_input("Enter State:"))
            else:
                print "enter correct contact number"
                self.donorinfo()
        except:
            print "Errors Occoured.. Try Again.."
                
    def blddetails(self):
        bldtypes =['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
        try:
            self.donorbld = str(raw_input("Enter Blood Type:(O+,O-,A+,A-,B+,B-,AB+,AB-)"))
            if self.donorbld in bldtypes:
                print "Blood type saved.."
            else:
                print "Enter Correct Blood type.."
                self.blddetails()
                
            lastyr = int(raw_input("Enter Last Dontated Year(like 2001):"))
            lastmn = int(raw_input("Enter Last Dontated Month(like 04):"))
            now = datetime.datetime.now()
            curyear=now.year
            curmonth=now.month
            year = curyear - lastyr
            month = curmonth - lastmn
            
            if year == 0 and month <=3:
                print "You last donated blood year %d and month %d " %lastyr %lastmn
                print "Next your Donoted month: "%lastmn+3
                print "Thank You..."
                time.sleep(2)
                exit()  
            elif year == 0 and month >=3:
                print "Please Eligible for Donate your blood.."

            else:
                print "Enter correct date.."
                blddetails()
        except:
            print "Errors Occoured.. Try Again.."
            

    def search(self):
        uname = str(raw_input("Enter name for **Blood needed person:"))
        bldtype = str(raw_input("Enter needed person **Blood Type:(O+,O-,A+,A-,B+,B-,AB+,AB-)"))
        atype =['A+','A-','B+','B-']
        otype =['O+','O-','A+','A-','B+','B-','AB+','AB-']
        abtype=['AB+','AB-']

        if self.donorbld == 'A+' or 'A-' or 'B+' or 'B-':
            if bldtype in atype:
                print "Your Blood and Donor Blood Matched.."
            else:
                print "Your Blood and Donor Blood Not Matched.."
                
        elif self.donorbld == 'O+' or 'O-':
            if bldtype in otype:
                print "Your Blood and Donor Blood Matched.."
            else:
                print "Your Blood and Donor Blood Not Matched.."
            
        elif self.donorbld == 'AB+' or 'AB-':
            if bldtype in abtype:
                print "Your Blood and Donor Blood Matched.."
            else:
                print "Your Blood and Donor Blood Not Matched.."
            
        else:
            print "Blood type not match.."
            exit()


    def dbcreate(self):
        
        db = MySQLdb.connect(host="localhost",
                             user="root",
                             password="root",
                             db="test")
        cur = db.cursor()
        
        cur.execute("INSERT INTO blddonorinfo(name,age,contact,city,state) VALUES (self.name,self.age,self.contact,self.city,self.state)")      
        cur.execute("SELECT * FROM examples")

        for row in cur.fetchall() :
            print row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", row[5]

bld = blood()

bld.donorinfo()
bld.blddetails()
bld.search()
bld.dbcreate()

        



                     
