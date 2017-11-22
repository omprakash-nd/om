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
        notrain = int(raw_input("Enter number of trains to connected city's"))

        for train in range(notrain):    

            start_info = str(raw_input("enter train depature time and depature station:"))
            start = start_info.split()
            
            start_list = [int(check) if check.isdigit() else check for check in start]
            traindepaturelist.append(start_list)

            end_info = str(raw_input("enter train arrival time and arrival station:"))
            end = end_info.split()

            end_list = [int(check) if check.isdigit() else check for check in end]
            trainarrivallist.append(end_list)
        return traindepaturelist,trainarrivallist 

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
                else:
                    print "Enter correctime.."
            else:
                 print "Wrong End Point"     
        else:
            print "Wrong Start Point"
        return passenger

    def MatchStation(self,traindepaturelist,trainarrivallist,passenger):
        destination = []
        for i in range(0,len(trainarrivallist)):
            j=1
            if passenger[j] == trainarrivallist[i][j]:
                 destination.append(trainarrivallist[i])
            else:
                print "Wrong Destination"
        return destination

    def MatchTime(self,destination,passenger):
        getDest=[]
        check =""
        j=0
        for i in range(0,len(destination)):
            if passenger[2] == destination[i][j]:
                getDest.append(destination[i])        
            elif passenger[2] > destination[i][j]:
                getDest.append(destination[i])
            else:
                check = "No connection"
        Dest=max(getDest)
        if len(getDest) <= 1:
            print check
        return Dest

    def Result(self,dest,trainarrivallist,traindepaturelist):
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

    arg5=Rail.MatchTime(arg4,arg3)
    
    Rail.Result(arg5,arg2,arg1)


    
