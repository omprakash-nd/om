import sys,csv
from collections import defaultdict

class RailRoad():
    def readFile(self):
        try:
            isSuccess = True
            file  = open('input.csv', "rb")
            reader = csv.reader(file)

            depture =[]
            arrival = []
            for idx,row in enumerate(reader):
                if idx>0:
                    dept_det=[row[0],row[1]]
                    depture.append(dept_det)

                    arr_det=[row[2],row[3]]
                    arrival.append(arr_det)
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return depture,arrival,isSuccess

    def getPassengerInfo(self,isSuccess):
        try:
            isSuccess = True
            passenger =[]
            passenger_start = str(raw_input("Enter passener startpoint:"))
            if str(passenger_start):
                passenger_end = str(raw_input("Enter passener endpoint:"))
                if str(passenger_end):
                    if passenger_start == passenger_end:
                        print "Startpoint and Endpoint is same.."
                    else:
                        passenger_time = int(raw_input("Enter time to reach destination:\n"))
                        if passenger_time <=2400:
                            passenger.append(passenger_start)
                            passenger.append(passenger_end)
                            passenger.append(passenger_time)                
                        else:
                            print "Enter correctime.."
                            isSuccess = False
                else:
                     print "Wrong End Point"
                     isSuccess = False
            else:
                print "Wrong Start Point"
                isSuccess = False
            
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return passenger,isSuccess

    def getTrainDetails(self,depture,arrival,isSucess):
        try:
            isSuccess = True
            traindepaturelist = []
            trainarrivallist =[]
            for i in depture:
                traindepaturelist.append([int(check) if check.isdigit() else check for check in i])
            for i in arrival:     
                trainarrivallist.append([int(check) if check.isdigit() else check for check in i])
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return traindepaturelist,trainarrivallist,isSuccess

    def MatchStation(self,traindepaturelist,trainarrivallist,passenger,isSucess):
        try:
            isSuccess = True
            destination = []
            start = []
            j=1
            for i in range(0,len(trainarrivallist)):
                if trainarrivallist[i][0] == passenger[j]:
                     destination.append(trainarrivallist[i])

            for i in range(0,len(traindepaturelist)):
                 if traindepaturelist[i][0] == passenger[0]:
                     start.append(traindepaturelist[i])

            if len(destination) == 0 or len(start) == 0:
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
            j=1
            for i in range(0,len(destination)):
                if passenger[2] == destination[i][j] or passenger[2] > destination[i][j]:
                    getDest.append(destination[i])
                    Dest=max(getDest)
                else:
                    check = "No connection"
            if len(getDest) <= 1:
                print check    
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
    Depature,Arrival,Result = Rail.readFile()
    if Result:
        Passenger,Result=Rail.getPassengerInfo(Result)    
    if Result:
        TrainDept,TrainArrival,Result=Rail.getTrainDetails(Depature,Arrival,Result)
    if Result:
        Station,Result=Rail.MatchStation(TrainDept,TrainArrival,Passenger,Result)
    if Result:
        Destination,Result=Rail.MatchTime(Station,Passenger,Result)
    if Result:
        Result=Rail.Display(Destination,TrainArrival,TrainDept,Result)
