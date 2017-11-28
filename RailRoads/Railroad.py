import sys,csv
from collections import defaultdict

class Railroads():
    def openFile(self,filename):
        try:
            isSuccess = True
            if filename.endswith('.csv'):
                file  = open(filename)
                reader = csv.reader(file)
            else:
                isSuccess = False
                print "File format not correct"

        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return reader,isSuccess

    def readFile(self,data): 
        try:
            isSuccess = True
            depture =[]
            arrival = []
            cities = []
            for count,row in enumerate(data):
                if count > 0:
                    dept_det=[row[0],row[1]] 
                    depture.append(dept_det)
                    arr_det=[row[2],row[3]]
                    arrival.append(arr_det)
                    city = [row[0],row[2]]
                    cities.append(city)
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return depture,arrival,cities,isSuccess        

    def getPassengerInfo(self,cities,isSuccess):
        try:
            isSuccess = True
            passenger =[]
            passenger_start = str(raw_input("Enter passener startpoint:"))
            if str(passenger_start == cities):
                passenger_end = str(raw_input("Enter passener endpoint:"))
                if str(passenger_end == cities):
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
            for count in depture:
                traindepaturelist.append([int(check) if check.isdigit() else check for check in count])
            for count in arrival:     
                trainarrivallist.append([int(check) if check.isdigit() else check for check in count])
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
            index=1
            for count in range(0,len(trainarrivallist)):
                if trainarrivallist[count][0] == passenger[index]:
                     destination.append(trainarrivallist[count])

            for count in range(0,len(traindepaturelist)):
                 if traindepaturelist[count][0] == passenger[0]:
                     start.append(traindepaturelist[count])

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
            index=1
            for count in range(0,len(destination)):
                if passenger[2] == destination[count][index] or passenger[2] > destination[count][index]:
                    getDest.append(destination[count])
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

    def Display(self,dest,trainarrivallist,traindepaturelist,passenger,isSucess):
        try:
            isSuccess = True
            if len(dest)!=0:
                for count in range(len(trainarrivallist)):
                    if trainarrivallist[count] == dest:
                        if passenger[0] == traindepaturelist[count][0]:
                            print "If You start %r clock from %r" %(traindepaturelist[count][1], traindepaturelist[count][0])
                            print "You will reach %r on %r clock"% (trainarrivallist[count][0], trainarrivallist[count][1])
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return isSuccess

if __name__ == '__main__':
    if len(sys.argv) > 1:
        Rail = Railroads()
        TrainData,Result = Rail.openFile(sys.argv[1])
        if Result:
            Depature,Arrival,City,Result = Rail.readFile(TrainData)
        if Result:
            Passenger,Result=Rail.getPassengerInfo(City,Result)    
        if Result:
            TrainDept,TrainArrival,Result=Rail.getTrainDetails(Depature,Arrival,Result)
        if Result:
            Station,Result=Rail.MatchStation(TrainDept,TrainArrival,Passenger,Result)
        if Result:
            Destination,Result=Rail.MatchTime(Station,Passenger,Result)
        if Result:
            Result=Rail.Display(Destination,TrainArrival,TrainDept,Passenger,Result)
