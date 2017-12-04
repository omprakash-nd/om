from RailCVS import Rails
from collections import defaultdict
import sys

class Railroads():
    def readRailInfo(self):
        try:
            isSuccess= True
            print """Hello, This application for check your train information.
Once you check Departure and arrival stations name from your input file.\n
User provide Departue,Arrival stations & time like 0000 to 2400\n"""
            rail = Rails()
            if len(sys.argv)>1:
                filename, isfile = rail.checkFile(sys.argv[1])
                if isfile:
                    reader,isRead = rail.readFile(filename,isfile)
                    if isRead:
                        header,isheader=rail.checkHeading(reader,isRead)
                        if isheader:
                            departure,arrival,cities,isTrainDetails = rail.getTrainInfo(reader,isheader)
            else:
                print "You failed to provide filename as input on the command line!"
                isSuccess= False
                exit()
        except Exception as exception:
            isSuccess= False
            template = "An exception of type readRailInfo Depature{0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return departure,arrival,cities,isSuccess

    def getPassengerInfo(self,cities,isSuccess):
        try:
            isSuccess = True
            passenger =[]
            passenger_start = str(raw_input("Enter passener startpoint:"))
            if passenger_start in cities:
                passenger_end = str(raw_input("Enter passener endpoint:"))
                if passenger_end in cities:
                    if passenger_start == passenger_end:
                        print "Startpoint and Endpoint is same.."
                    else:
                        passenger_time = int(raw_input("Enter time to reach destination:"))
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
            template = "An exception of type getPassengerInfo{0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return passenger,isSuccess

    def convertDepatureTime(self,departure,isSuccess):
        try:
            isSuccess = True
            traindepaturelist = []
            for count in departure:
                traindepaturelist.append([int(check) if check.isdigit() else check for check in count])
        except Exception as exception:
            isSuccess = False
            template = "An exception of type convertDepatureTime{0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return traindepaturelist,isSuccess
        
    def convertArrivalTime(self,arrival,isSuccess):
        try:
            isSuccess = True
            trainarrivallist =[]
            for count in arrival:     
                trainarrivallist.append([int(check) if check.isdigit() else check for check in count])
        except Exception as exception:
            isSuccess = False
            template = "An exception of type convertArrivalTime{0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return trainarrivallist,isSuccess

    def checkMatchStation(self,traindepaturelist,trainarrivallist,passenger,isSucess):
        try:
            isSuccess = True
            match_destination = []
            start = []
            end=[]
            index=1
            for count in range(0,len(traindepaturelist)):
                 if traindepaturelist[count][index] == passenger[0]:
                     start.append(traindepaturelist[count])
                     match_destination.append(trainarrivallist[count])
                     
            for count in range(len(match_destination)):
                if match_destination[count][index] == passenger[index]:
                     end.append(match_destination[count])
            if len(match_destination) == 0 or len(start) == 0:
                print "No Connection"
        except Exception as exception:
            isSuccess = False
            template = "An exception of type checkMatchStation{0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return start,end,isSuccess

    def checkMatchTime(self,start,end,passenger,isSucess):
        try:
            isSuccess = True
            match_time=[]
            not_match_time=[]
            match_train=[]
            maxTrain = []
            index=2
            count=0
            check=""
            for count in range(0,len(end)):
                if passenger[index] == end[count][index] or passenger[index] > end[count][index]:
                    match_time.append(end[count])
                    time=max(map(lambda x: x[index], match_time))
                else:
                    Notrain="On Time No trains available"

            for count in range(0,len(match_time)):
                if match_time[count][index] == time:
                     match_train= match_time[count]
                else:
                    check = "No connection"
                    
            maxTrain.append(match_train)
            if len(match_time) <= 1:
                print check
            if len(match_time)<=1:
                print Notrain
        except Exception as exception:
            isSuccess = False
            template = "An exception of type checkMatchTime{0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return maxTrain,isSuccess

    def Display(self,maxTrain,trainarrivallist,traindepaturelist,passenger,isSucess):
        try:
            isSuccess = True
            if len(maxTrain)!=0:
                for count in range(len(trainarrivallist)):
                    if trainarrivallist[count] in maxTrain:
                        if passenger[0] in traindepaturelist[count][1]:
                            print "Your Train Number:%r" %(traindepaturelist[count][0]) 
                            print "If You start %r clock from %r" %(traindepaturelist[count][2], traindepaturelist[count][1])
                            print "You will reach %r on %r clock" %(trainarrivallist[count][1], trainarrivallist[count][2])                
        except Exception as exception:
            isSuccess = False
            template = "An exception of type Display{0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return isSuccess 

if __name__ == "__main__":
    check="info's not correct.."
    railroad =Railroads()
    isSuccess = True
    depts,arrivals,city,result=railroad.readRailInfo()
    if result:
        info_passenger,isPassenerInfo =railroad.getPassengerInfo(city,result)
    else:
        isSuccess = False
        print check
        exit()
    if isPassenerInfo:
        departuretime,isDeparture=railroad.convertDepatureTime(depts,isPassenerInfo)
    else:
        isSuccess = False
        print check
        exit()
    if isDeparture:
        arrivaltime,isArrival=railroad.convertArrivalTime(arrivals,isDeparture)
    else:
        isSuccess = False
        print check
        exit()
    if isArrival:
        sortStart,sortDest,isMatchJunction=railroad.checkMatchStation(departuretime,arrivaltime,info_passenger,isArrival)
    else:
        isSuccess = False
        print check
        exit()
    if isMatchJunction:
        sortTime,isMatchTime = railroad.checkMatchTime(sortStart,sortDest,info_passenger,isMatchJunction)
    else:
        isSuccess = False
        print check
        exit()
    if isMatchTime:
        isSuccess=railroad.Display(sortTime,arrivaltime,departuretime,info_passenger,isMatchTime)
    else:
        print check
        exit()
