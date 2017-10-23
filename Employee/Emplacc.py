import datastore
import time

def verification():
    print "Login"
    print "User Name:"
    uname = raw_input()
    print "Password :"
    password = raw_input()

    if uname == "admin" and password =="admin":
        menu()
    else:
        print "Username or Password wroung.."
        verification()
    

def menu():
    print "Welcome To Employee Account Creation..."
    prompt = int(raw_input("""Press keys \n 1-New Creation 2-View Exisiting Details 3-Delete Account.
"""))

    if(prompt == 1 ):
        acc=Newaccount()
    elif(prompt == 2):
        acc=Exitistacc()
    elif(prompt == 3):
        acc=Deleteacc()
    else:
        print "You have pressed the wrong key, please try again"
        menu()

class Newaccount:
    """Class for a New account"""
    type="Normal"
    def __init__(self):
        self.empname, self.bldgrp, self.dob = datastore.empacc()
        print("Thankyou,You have created %s new account" %self.empname)
        time.sleep(2)
        print "Last Entered %s Details Saved.."
        time.sleep(1)
        self.trant_back()
        
    def empfunctions(self):
        print("\n\nTo access any function below, enter the corresponding key")
        print ("""To: Employee Address -- press A.,
Employee Branch -- press B.
Employee Contact No -- press C.
Valid Period -- press V
exit service -- press E\n
:"""),
        ans = raw_input()

        if ans == 'a' or ans == 'A':

            print "Update Employee Address:"
            self.address()
            
        elif ans == 'b' or ans == 'B':
            print "Update Employee Branch:"
            branch = str(raw_input())
            stream = str(raw_input())
            
        elif ans == 'c' or ans == 'C':
            print "Update Employee Contact Number:"
            mob1 = int(input())
            mob2 = int(input())

        elif ans == 'e' or ans == 'E':
            exit()

        else:
            print "Your Pressed Wroung Key...Please enter correct key.."
            self.empfunctions()
            
    def address(self):
        print "Enter Door No./ Street line:"
        drno = raw_input()
        print "Enter Addressline 1 :"
        addr1 = str(raw_input(""))
        print "Enter Addressline 2 :"
        addr2 = str(raw_input())
        print "Enter City :"
        city = str(raw_input())
        print "Enter State :"
        state = str(raw_input())
        print "Enter Country:"
        country = str(raw_input())
        print "Enter Pincode:"
        pincode = int(raw_input())
        addr = drno + addr1 + addr2
        self.working()
        print "Last Entered %s Details Saved.." %self.empname
        time.sleep(1)
        self.trant_back()

     
    def working(self):
        print("working"),
        time.sleep(1)
        print ("..")
        time.sleep(1)
        print("..")
        time.sleep(1)

    def trant_back(self):
        ans=raw_input("Do you want to do any other updation..? (y/n)\n").lower()
        self.working()
        if ans=='y':
            self.empfunctions()
        elif ans=='n':
            print ("Thank you. Have a good day")
            time.sleep(1)
            print ("Goodbye {}").format(self.empname)
            exit()
        elif ans!='y' and ans!='n':
            print "Unknown key pressed, please choose either 'N' or 'Y'"
            self.trant_back()

verification()
