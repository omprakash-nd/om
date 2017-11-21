import sys
from collections import defaultdict

class RailRoad():
    def GetCities(self):
        cities = []
        ncity = int(raw_input("Enter no.of cities "))
        for i in range(ncity):
            i=i+1
            city = str(raw_input("Enter %r cities name:" %i))
            cities.append(city)    
        return cities 

    def TrainDetails(self,cities):
        traindetp = []
        trainarr =[]
        notrain = int(raw_input("Enter no.of trains"))
        for train in range(notrain):
            
            start_info = str(raw_input("enter starttime and depature station:"))
            start = start_info.split()
            changed_list = [int(f) if f.isdigit() else f for f in start]
            traindetp.append(changed_list)

            end_info = str(raw_input("enter reachtime and arrival station:"))
            end = end_info.split()
            changed_list1 = [int(f) if f.isdigit() else f for f in end]
            trainarr.append(changed_list1)

        return traindetp,trainarr 

    def PassengerInfo(self,city):

        passenger =[]

        passenger_start = str(raw_input("enter passener startpoint:"))
        if passenger_start in city:
            passenger.append(passenger_start)
            
            passenger_end = str(raw_input("enter passener endpoint:"))
            if passenger_end in city:
                passenger.append(passenger_end)
                passenger_time = int(raw_input("enter time to reach destination:"))
                if passenger_time <=24:
                    passenger.append(passenger_time)
                    print "Process.."
                else:
                    print "Enter correctime.."
            else:
                 print "Wrong End Point"     
        else:
            print "Wrong Start Point"

        return passenger

    def check(self,traindept,trainarr,passenger):
        dest = []
        start = []
        
        for i in range(0,len(trainarr)):
            j=1
            if passenger[j] == trainarr[i][j]:
                 dest.append(trainarr[i])
            else:
                print "Wrong Destination"
        return dest

    def destination(self,dest,passenger):
        getDest=[]
        res =""
        j=0
        for i in range(0,len(dest)):
            if passenger[2] == dest[i][j]:
                getDest.append(dest[i])        
            elif passenger[2] > dest[i][j]:
                getDest.append(dest[i])
            else:
                res = "No connection"
        Dest=max(getDest)
        if len(getDest) <= 1:
            print res
        return Dest

    def checkingDest(self,getDest,trainarr,traindept):
        for i in range(len(trainarr)):
            if trainarr[i] == getDest:
                print "If You start %r clock from %r" %(traindept[i][0], traindept[i][1])
                print "You will reach %r on %r clock"% (trainarr[i][1], trainarr[i][0])

if __name__ == '__main__':

    Rail = RailRoad()      

    arg = Rail.GetCities()

    arg1,arg2 = Rail.TrainDetails(arg)
    
    arg3 = Rail.PassengerInfo(arg)

    arg4 = Rail.check(arg1,arg2,arg3)

    arg5=Rail.destination(arg4,arg3)
    
    Rail.checkingDest(arg5,arg2,arg1)


    
