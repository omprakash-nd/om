import sys
from collections import defaultdict

class RailRoad():
    def GetCities(self):
        cities = []
        ncity = int(raw_input("Enter number of cities "))
        for i in range(ncity):
            i=i+1
            city = str(raw_input("Enter %r cities name:" %i))
            cities.append(city)    
        return cities 

    def TrainDetails(self,cities):
        traindepaturelist = []
        trainarrivallist =[]
        notrain = int(raw_input("Enter number of trains to connected city's:"))
        for train in range(notrain):    
            start_info = str(raw_input("Enter train depature time and depature station:"))
            start = start_info.split() 
            start_list = [int(check) if check.isdigit() else check for check in start]
            traindepaturelist.append(start_list)
            end_info = str(raw_input("Enter train arrival time and arrival station:"))
            end = end_info.split()
            end_list = [int(check) if check.isdigit() else check for check in end]
            trainarrivallist.append(end_list)
        return traindepaturelist,trainarrivallist 

    def PassengerInfo(self,city):
        passenger =[]
        passenger_start = str(raw_input("Enter passener startpoint:"))
        if passenger_start in city:
            passenger_end = str(raw_input("Enter passener endpoint:"))
            if passenger_end in city:
                if passenger_start == passenger_end:
                    print "Startpoint and Endpoint is same.."
                    self.PassengerInfo(city)
                else:
                    passenger_time = int(raw_input("Enter time to reach destination:"))
                    if passenger_time <=24:
                        passenger.append(passenger_start)
                        passenger.append(passenger_end)
                        passenger.append(passenger_time)                
            else:
                    print "Enter correctime.."
            else:
                 print "Wrong End Point"     
        else:
            print "Wrong Start Point"
        return passenger

    def MatchStation(self,traindepaturelist,trainarrivallist,passenger):
        destination = []
        j=1
        for i in range(0,len(trainarrivallist)):
            if trainarrivallist[i][j] == passenger[j]:
                 destination.append(trainarrivallist[i])
                 if len(destination) == 0:
                     print "No Connections"
        return destination

    def MatchTime(self,destination,passenger):
        getDest=[]
        check=""
        Dest=""
        j=0
        for i in range(0,len(destination)):
            if passenger[2] == destination[i][j] or passenger[2] > destination[i][j]:
                getDest.append(destination[i])
                Dest=max(getDest)
            else:
                check = "No connection"
        if len(getDest) <= 1:
            print check
        return Dest

    def Result(self,dest,trainarrivallist,traindepaturelist):
        if len(dest)<=1:
            for i in range(len(trainarrivallist)):
                if trainarrivallist[i] == dest:
                    print "If You start %r clock from %r" %(traindepaturelist[i][0], traindepaturelist[i][1])
                    print "You will reach %r on %r clock"% (trainarrivallist[i][1], trainarrivallist[i][0])
   
if __name__ == '__main__':
    Rail = RailRoad()      
    arg = Rail.GetCities()
    arg1,arg2 = Rail.TrainDetails(arg)
    arg3 = Rail.PassengerInfo(arg)
    arg4 = Rail.MatchStation(arg1,arg2,arg3)
    if len(arg4) != 0:
        arg5=Rail.MatchTime(arg4,arg3)
        Rail.Result(arg5,arg2,arg1)


    
