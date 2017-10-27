import os
import datetime
import MySQLdb

class blood:
    

    def donorinfo(self):
        name = str(raw_input("Enter Name:"))
        age = int(raw_input("Enter Age:"))
        contact = int(raw_input("Contact Number:"))
        city = str(raw_input("Enter City:"))
        state = str(raw_input("Enter State:"))

    def blddetails(self):
        donorbld = str(raw_input("Enter Blood Type:"))
        lastyr = int(raw_input("Enter Last Dontated Year(like 2001):"))
        lastmn = int(raw_input("Enter Last Dontated Month(like 04):"))

    def check(self):
        now = datetime.datetime.now()
        curyear=now.year
        curmonth=now.month

        year = curyear - lastyr
        month = curmonth - lastmonth

        if year == 0 and month <=3:

            print "You last donated blood year %d and month %d "lastyr,lastmn
            print "Next your Donsted month: "lastmn+3

        elif year == 0 and month >=3:
            print "Please Donate your blood.."

    def search(self):
        uname = str(raw_input("Enter blood needed person:"))
        bldtype = str(raw_input("Enter Blood Type:(O+,O-,A+,A-,B+,B-,AB+,AB-)"))

bld = blood()

bld.donorinfo()
bld.blddetails()
bld.search()

        



                     
