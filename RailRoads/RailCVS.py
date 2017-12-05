import csv
class Rails():
    def checkFile(self,filename):
        try:
            isSuccess = True
            if filename.endswith('.csv'):
                isSuccess = True
            else:
                isSuccess = False
                print "File format not correct"
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return filename,isSuccess

    def readFile(self,filename,isSuccess):
        try:
            isSuccess = True
            file_name  = open(filename)
            reader = csv.reader(file_name)
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return reader,isSuccess

    def checkHeading(self,reader,isSuccess):
        try:
            isSuccess = True
            data_format = ['Trainno', 'Depature', 'DepatureTime', 'Arrival', 'ArrivalTime']
            for row in reader:
              header = row
              break
            if data_format == header:
                isSuccess = True
            else:
                print "In file data alignment is not correct."
                isSuccess = False
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return header,isSuccess

    def getTrainInfo(self,reader,isSuccess):
        try:
            isSuccess = True
            list_departure = []
            list_arrival = []
            list_dept_cities = []
            list_arrive_cities=[]
            
            for count,row in enumerate(reader):
                if count > 0:
                    dept_detail=[row[0],row[1],row[2]]
                    list_departure.append(dept_detail)
                    
                    arrive_detail=[row[0],row[3],row[4]]
                    list_arrival.append(arrive_detail)

                    dept_city = row[1]
                    list_dept_cities.append(dept_city)

                    arrive_city= row[3]
                    list_arrive_cities.append(arrive_city)

            joinedList = list_dept_cities + list_arrive_cities
            city = list(set(joinedList))         
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return list_departure,list_arrival,city,isSuccess
