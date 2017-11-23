import sys
from collections import defaultdict

class RailRoad():
    
    def GetCities(self):
        try:
            isSuccess = True
            cities = []
            ncity = int(raw_input("Enter number of cities "))
            for i in range(ncity):
                i=i+1
                city = str(raw_input("Enter %r cities name:" %i))
                cities.append(city)
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return cities, isSuccess

    def getTrainCount(self,isSucess):
        try:
            isSuccess = True
            num_train = int(raw_input("Enter number of trains to connected city's:"))
            if num_train <=0:
                print "Train count is not in zero"
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return num_train,isSuccess

    def getTrainDetails(self,num_train,cities,isSucess):
        try:
            isSuccess = True
            traindepaturelist = []
            trainarrivallist =[]
            for train in range(num_train):    
                start_info = str(raw_input("Enter train depature time and depature station:"))
                start = start_info.split() 
                start_list = [int(check) if check.isdigit() else check for check in start]
                traindepaturelist.append(start_list)

                end_info = str(raw_input("Enter train arrival time and arrival station:"))
                end = end_info.split()
                end_list = [int(check) if check.isdigit() else check for check in end]
                trainarrivallist.append(end_list)
                
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return traindepaturelist,trainarrivallist,isSuccess

    def getPassengerInfo(self,cities,isSucess):
        try:
            isSuccess = True
            passenger =[]
            
            passenger_start = str(raw_input("Enter passener startpoint:"))
            if passenger_start in cities:
                passenger_end = str(raw_input("Enter passener endpoint:"))
                if passenger_end in cities:
                    if passenger_start == passenger_end:
                        print "Startpoint and Endpoint is same.."
                        self.PassengerInfo(cities)
                    else:
                        passenger_time = int(raw_input("Enter time to reach destination:\n"))
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
            
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return passenger,isSuccess

    def MatchStation(self,traindepaturelist,trainarrivallist,passenger,isSucess):
        try:
            isSuccess = True
            destination = []
            j=1
            for i in range(0,len(trainarrivallist)):
                if trainarrivallist[i][j] == passenger[j]:
                     destination.append(trainarrivallist[i])
                     if len(destination) == 0:
                         print "No Connections"
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return destination,isSuccess

    def MatchTime(self,destination,passenger,isSucess):
        try:
            isSuccess = True
            getDest=[]
            check=""
            Dest =""
            j=0
            for i in range(0,len(destination)):
                if passenger[2] == destination[i][j] or passenger[2] > destination[i][j]:
                    getDest.append(destination[i])
                    Dest=max(getDest)
                else:
                    check = "No connection"
            if len(getDest) <= 1:
                print check
            print Dest
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return Dest,isSuccess

    def Display(self,dest,trainarrivallist,traindepaturelist,isSucess):
        try:
            isSuccess = True
            if len(dest)!=0:
                for i in range(len(trainarrivallist)):
                    if trainarrivallist[i] == dest:
                        print "If You start %r clock from %r" %(traindepaturelist[i][0], traindepaturelist[i][1])
                        print "You will reach %r on %r clock"% (trainarrivallist[i][1], trainarrivallist[i][0])
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return isSuccess

if __name__ == '__main__':
    Rail = RailRoad()
    arg1,arg = Rail.GetCities()
    if arg:
        arg2,arg=Rail.getTrainCount(arg)
    if arg:
        arg3,arg4,arg=Rail.getTrainDetails(arg2,arg1,arg)
    if arg:
        arg5,arg=Rail.getPassengerInfo(arg1,arg)
    if arg:
        arg6,arg=Rail.MatchStation(arg3,arg4,arg5,arg)
    if arg:
        arg7,arg=Rail.MatchTime(arg6,arg5,arg)
    if arg:
        arg=Rail.Display(arg7,arg4,arg3,arg)
