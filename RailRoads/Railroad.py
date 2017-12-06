from RailCVS import Rails
from collections import defaultdict
import sys


class Railroads():
    def readRailInfo(self, file_name):
        try:
            isSuccess = True
            info = "File format not correct"
            rail = Rails()
            if len(file_name) > 1:
                filename, isfile = rail.checkFile(file_name)
            else:
                isSuccess = False
            if isfile:
                reader, isRead = rail.readFile(filename, isfile)
                if isRead:
                    header, isheader = rail.checkHeading(reader, isRead)
                    if isheader:
                        departure, arrival, cities, isTrainDetails = rail.getTrainInfo(reader, isheader)
                        return departure, arrival, cities, isSuccess
            else:
                print info 
                return isSuccess
                
        except Exception as exception:
            isSuccess = False
            template = "An exception of type readRailInfo function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        
    def getPassenger(self):
        passenger_data = []
        passenger_start = str(raw_input("Enter passener startpoint:"))
        passenger_data.append(passenger_start)
        passenger_end = str(raw_input("Enter passener endpoint:"))
        if passenger_start == passenger_end:
            print "Startpoint and Endpoint is same.."
        else:
            passenger_data.append(passenger_end)
        passenger_time = int(raw_input("Enter time to reach destination:"))
        passenger_data.append(passenger_time)
        return passenger_data

    def checkPassenger(self, cities, passenger_data, isSuccess):
        try:
            isSuccess = True
            passenger = []
            if passenger_data[0] in cities:
                passenger.append(passenger_data[0])
                if passenger_data[1] in cities:
                    passenger.append(passenger_data[1])
                    if passenger_data[2] <= 2400:
                        passenger.append(passenger_data[2])
                    else:
                        wrong_time = "please enter correctime.."
                        isSuccess = False
                else:
                    wrong_point = "Wrong start/end point"
                    isSuccess = False
            else:
                wrong_point = "Wrong start/end point"
                isSuccess = False

            if len(passenger) == 0:
                print wrong_point
            if len(passenger) == 2:
                print wrong_time
                
        except Exception as exception:
            isSuccess = False
            template = "An exception of type getPassengerInfo function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return passenger, isSuccess

    def convertDepatureTime(self, departure, isSuccess):
        try:
            isSuccess = True
            traindepaturelist = []
            for count in departure:
                traindepaturelist.append([int(check) if check.isdigit() else check for check in count])
        except Exception as exception:
            isSuccess = False
            template = "An exception of type convertDepatureTime function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return traindepaturelist, isSuccess
        
    def convertArrivalTime(self, arrival, isSuccess):
        try:
            isSuccess = True
            trainarrivallist = []
            for count in arrival:     
                trainarrivallist.append([int(check) if check.isdigit() else check for check in count])
        except Exception as exception:
            isSuccess = False
            template = "An exception of type convertArrivalTime function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return trainarrivallist, isSuccess

    def checkMatchStation(self, traindepaturelist, trainarrivallist, passenger, isSucess):
        try:
            isSuccess = True
            match_destination = []
            start = []
            end = []
            index = 1
            for count in range(0, len(traindepaturelist)):
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
            template = "An exception of type checkMatchStation function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return start, end, isSuccess

    def checkMatchTime(self, start, end, passenger, isSucess):
        try:
            isSuccess = True
            match_time = []
            not_match_time = []
            match_train = []
            maxTrain = []
            index = 2
            count = 0
            check = ""
            for count in range(0, len(end)):
                if passenger[index] == end[count][index] or passenger[index] > end[count][index]:
                    match_time.append(end[count])
                    time = max(map(lambda key: key[index], match_time))
                else:
                    Notrain = "Sorry.., On Time No trains available"

            for count in range(0, len(match_time)):
                if match_time[count][index] == time:
                    match_train = match_time[count]
                else:
                    check = "No connection"
            maxTrain.append(match_train)
            if len(match_time) == 0:
                print check
            if len(match_time) == 0:
                print Notrain
                
        except Exception as exception:
            isSuccess = False
            template = "An exception of type checkMatchTime function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return maxTrain, isSuccess

    def Display(self, maxTrain, trainarrivallist, traindepaturelist, passenger, isSucess):
        try:
            isSuccess = True
            if len(maxTrain) != 0:
                for count in range(len(trainarrivallist)):
                    if trainarrivallist[count] in maxTrain:
                        if passenger[0] in traindepaturelist[count][1]:
                            print "\nYour Train Number:%r" % (traindepaturelist[count][0]) 
                            print "If You start %r clock from %r" % (traindepaturelist[count][2], traindepaturelist[count][1])
                            print "You will reach %r on %r clock" % (trainarrivallist[count][1], trainarrivallist[count][2])                
        except Exception as exception:
            isSuccess = False
            template = "An exception of type Display function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return isSuccess 

if __name__ == "__main__":
    check = "info's not correct.."
    railroad = Railroads()
    isSuccess = True
    try:
        depts, arrivals, city, result = railroad.readRailInfo(sys.argv[1])
    except Exception as exception:
        isSuccess = False
        print check
        exit()
    if result:
        print """Hello, This application for check your train information.
Once you check Departure and arrival stations name from your input file.\n
User provide Departue,Arrival stations & time like 0000 to 2400\n"""
        info_passenger = railroad.getPassenger()
    else:
        isSuccess = False
        print check
    if result:
        passenger, isPassener = railroad.checkPassenger(city, info_passenger, result)
    else:
        isSuccess = False
        print check
        exit()
    if isPassener:
        departuretime, isDeparture = railroad.convertDepatureTime(depts, isPassener)
    else:
        isSuccess = False
        print check
        exit()
    if isDeparture:
        arrivaltime, isArrival = railroad.convertArrivalTime(arrivals, isDeparture)
    else:
        isSuccess = False
        print check
        exit()
    if isArrival:
        sortStart, sortDest, isMatchJunction = railroad.checkMatchStation(departuretime, arrivaltime, passenger, isArrival)
    else:
        isSuccess = False
        print check
        exit()
    if isMatchJunction:
        sortTime, isMatchTime = railroad.checkMatchTime(sortStart, sortDest, passenger, isMatchJunction)
    else:
        isSuccess = False
        print check
        exit()
    if isMatchTime:
        isSuccess = railroad.Display(sortTime, arrivaltime, departuretime, info_passenger, isMatchTime)
    else:
        print check
        exit()
