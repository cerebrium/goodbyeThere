##### functions file #####
## make sure to import anything you plan to use
import datetime
import math
import pandas as pd
import numpy as np
import glob
from collections import defaultdict
from collections import Counter
import math
import csv
import collections, functools, operator
import re

## declare a function - this one is going to return an array containing the difference between log in and log out times
def timeDifference(logIn, logOut):
    date = datetime.date(1, 1, 1)  # null time value to compare our log in and log out times to

    dateTimeLogIn = datetime.datetime.strptime(str(logIn), '%H:%M:%S') # lots here... but combining null time and our elements log in time
    dateTimeLogOut = datetime.datetime.strptime(str(logOut), '%H:%M:%S')  # same but log out, and now we can actually subrat them

    differenceValue = dateTimeLogIn - dateTimeLogOut

    differenceValue = str(abs(differenceValue))  # if you look at the console it says 8:00:00.... which is fine, but comment this out then look what postman gives you
    myString = differenceValue.split()

    return myString

def statistics(datesList):
        #----- Below are the statistics we will need
    myDatesArray = []

    for ele in datesList:
        myTransientObjectDates = {}
        myTransientObjectDates['driver_id'] = str(ele.driver_id)
        myTransientObjectDates['date_id'] = ele.date_id
        myTransientObjectDates['name'] = ele.name
        myTransientObjectDates['inOff'] = ele.inOff
        myTransientObjectDates['route'] = ele.route
        myTransientObjectDates['logIn_time'] = ele.logIn_time
        myTransientObjectDates['logOut_time'] = ele.logOut_time
        myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
        myTransientObjectDates['location'] = ele.location
        myTransientObjectDates['date'] = ele.date
        myTransientObjectDates['parcel'] = ele.parcel
        # myTransientObjectDates['LWP'] = ele.LWP
        # myTransientObjectDates['LVP'] = ele.LVP
        # myTransientObjectDates['CRT'] = ele.CRT
        # myTransientObjectDates['RL'] = ele.RL
        # myTransientObjectDates['fuel'] = str(ele.fuel)
        myTransientObjectDates['support'] = str(ele.support)
        # myTransientObjectDates['vans'] = str(ele.vans)
        myTransientObjectDates['deductions'] = str(ele.deductions) # here
        # myTransientObjectDates['training'] = ele.CRT + ele.RL # and here

        myDatesArray.append(myTransientObjectDates)




    # get data
    df = pd.DataFrame(data=myDatesArray)    #turns the current data in the backend into panda dataframe 
    data = df
    # print('dataframe: ', data)

    # csv file manually.... cant have spaces in names or will cause errors elsewhere
    data.dropna(subset=['route'], axis = 'rows', how ='all', inplace = True) 
    data.fillna(0,inplace = True)
    #add week column
    #data["week"] = "18"
    #data.to_csv("data.csv", index=False)
    #print(data)

    #count the number of ALL routes
    #data['IN'] = data['IN'].astype(float)
    # numOfRoutes = data['inOff'].value_counts()[1]
    # #count number of LVP and LWP respectively
    # numOfLVP = int(data['LVP'].sum())
    # numOfLWP = int(data['LWP'].sum())
    # numOfParcels = int(data['parcel'].sum())


    # #here I just print out the results
    # names = ['Routes: ', 'LVP: ', 'LWP: ', 'Parcels:']

    

    # numOfRoutes = data['inOff'].value_counts()[1]  
    # # print('routes: ', numOfRoutes)

    # # this is how I would do this.... I am sure pandas has a way, but i dont know it
    # numOfMFNRoutesOne = data['route'].value_counts()
    
    # # set a counter variable
    # numOfMFNRoutes = 0

    # # set a loop variable
    # x = 0

    # # loop through each item in the data set you made
    # while x < len(numOfMFNRoutesOne):

    #     # display the information in the terminal
    #     print (
    #         'Route found: ', numOfMFNRoutesOne.index[x] , ' : ',  numOfMFNRoutesOne[numOfMFNRoutesOne.index[x]]
    #     )

    #     # make a conitional statment that if it finds what you are looking for it will increment the counter variable above
    #     if numOfMFNRoutesOne.index[x] == 'MFN':
    #         numOfMFNRoutes = numOfMFNRoutes + 1

    #     # increment the loop    
    #     x = x + 1

    # # numOfMFNRoutes = data['route'].value_counts()['MFN']
    # # print('mfn: ', numOfMFNRoutes)
    
    # numOfFUllRoutes = numOfRoutes - numOfMFNRoutes
    # # print('full: ', numOfFUllRoutes)


    # #count number of LVP and LWP respectively
    # # numOfLVP = int(data['LVP'].sum())
    # # numOfLWP = int(data['LWP'].sum())
    # numOfParcels = int(data['parcel'].sum())


    # #here I just print out the results
    # names = ['Routes: ',"FULL: ", 'MFN: ', 'LVP: ', 'LWP: ','Parcels: ']

    # #print(names)
    # values = [str(numOfRoutes),str(numOfFUllRoutes),str(numOfMFNRoutes),
    #       str(numOfLVP),str(numOfLWP),str(numOfParcels)]

    
    # #print(values)
    # myNum = len(values)

    # for i in names:
    #     n1 = names[0] + f" " + values[0] 
    #     n2 = names[1] + f" " + values[1]
    #     n3 = names[2] + f" " + values[2]
    #     n4 = names[3] + f" " + values[3]
    #     n5 = names[4] + f" " + values[4]
    #     n6 = names[5] + f" " + values[5]
    #     text = f"Statistics for today:"
    # print(text,n1,n2,n3,n4,n5,n6)
    # return [text,n1,n2,n3,n4,n5,n6]

def returnOrderdData(driversList, datesList, imagesList, vehicles, deductions, support):

    #### add an array of registrations for the vehicles that are owned by the company
    #### add array containing the status of the drivers

    myImagesArray = []
    myDriverArray = []
    myDatesArray = []
    myVehiclesArray = []
    myDeductionArray = []
    mySupportArray = []

    for ele in deductions:
        myTransientDeduction = {}
        myTransientDeduction['deduction_id'] = ele.deduction_id
        myTransientDeduction['date_id'] = str(ele.date_id)
        myTransientDeduction['name'] = ele.name
        myTransientDeduction['amount'] = str(ele.amount)

        myDeductionArray.append(myTransientDeduction)

    for ele in support:
        myTransientSupport = {}
        myTransientSupport['support_id'] = ele.support_id
        myTransientSupport['date_id'] = str(ele.date_id)
        myTransientSupport['name'] = ele.name
        myTransientSupport['amount'] = str(ele.amount)

        mySupportArray.append(myTransientSupport)

    for ele in imagesList:
        myTransientImage = {}
        myTransientImage['driver_id'] = str(ele.driver_id)
        myTransientImage['vehicle_id'] = str(ele.vehicle_id)
        myTransientImage['image_id'] = ele.image_id
        myTransientImage['name'] = ele.name
        myTransientImage['countryOfIssue'] = ele.countryOfIssue
        myTransientImage['expiryDate'] = ele.expiryDate
        myTransientImage['dueDate'] = ele.dueDate
        myTransientImage['datePassed'] = ele.datePassed
        myTransientImage['photo'] = ele.photo
        myTransientImage['managerApprovedName'] = ele.managerApprovedName
        myTransientImage['managerApprovedDate'] = ele.managerApprovedDate
        myTransientImage['imagesLink'] = ele.imagesLink
        myTransientImage['verified'] = ele.verified
        myTransientImage['driverSigned'] = ele.driverSigned
        myTransientImage['points'] = ele.points
        myTransientImage['nextDVLAScreenshot'] = ele.nextDVLAScreenshot
        

        myImagesArray.append(myTransientImage)

    for ele in vehicles:
        myTransientVehicle = {}
        myTransientVehicle['vehicle_id'] = ele.vehicle_id
        myTransientVehicle['registration'] = ele.registration
        myTransientVehicle['make'] = ele.make
        myTransientVehicle['model'] = ele.model
        myTransientVehicle['year'] = ele.year
        myTransientVehicle['companyOwned'] = ele.companyOwned
        myTransientVehicle['vtype'] = ele.vtype
        myTransientVehicle['quotePrice'] = str(ele.quotePrice)
        myTransientVehicle['invoice'] = str(ele.invoice)

        myVehiclesArray.append(myTransientVehicle)

        # images version
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['vehicle_id'] == ele.registration:
                imagesArray.append(imgObject)

        myTransientVehicle['imgArray'] = imagesArray  

    for ele in datesList:
        myTransientObjectDates = {}

        myTransientObjectDates['date_id'] = ele.date_id
        myTransientObjectDates['name'] = ele.name
        myTransientObjectDates['inOff'] = ele.inOff
        myTransientObjectDates['route'] = ele.route
        myTransientObjectDates['routeNumber'] = ele.routeNumber
        myTransientObjectDates['logOut_time'] = ele.logOut_time
        myTransientObjectDates['logIn_time'] = ele.logIn_time
        myTransientObjectDates['location'] = ele.location
        myTransientObjectDates['date'] = ele.date
        myTransientObjectDates['driver_id'] = str(ele.driver_id)
        myTransientObjectDates['mileage'] = ele.mileage
        myTransientObjectDates['start_mileage'] = ele.start_mileage
        myTransientObjectDates['finish_mileage'] = ele.finish_mileage
        myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
        myTransientObjectDates['parcel'] = ele.parcel
        myTransientObjectDates['parcelNotDelivered'] = ele.parcelNotDelivered
        myTransientObjectDates['TORH'] = ele.TORH
    
        myDeductionSum = 0
        mySupportSum = 0
        total = 0
        deductionList = []
        supportList = []

        for element in myDeductionArray: 
            if element['date_id'] == str(ele.date_id):
                myDeductionSum += float(element['amount'][3::])
                deductionList.append(element)
                
        myTransientObjectDates['deductionSum'] = 'GB£{}'.format(myDeductionSum) 
        myTransientObjectDates['deductionList'] = deductionList 

        for element in mySupportArray: 
            if element['date_id'] == str(ele.date_id):
                mySupportSum += float(element['amount'][3::])
                supportList.append(element)

        total = mySupportSum - myDeductionSum        

        myTransientObjectDates['supportSum'] ='GB£{}'.format(mySupportSum) 
        myTransientObjectDates['supportList'] = supportList 

        myTransientObjectDates['total'] = total

        myDatesArray.append(myTransientObjectDates)

    ## array for checking urls
    urlArray = []


    ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        datesArray = []
        myTransientObjectDriver['driver_id'] = str(ele.driver_id)
        myTransientObjectDriver['deleteButton'] = ele.deleteButton
        myTransientObjectDriver['vanOwner'] = ele.vanOwner
        myTransientObjectDriver['vehicle_name'] = ele.driver_id
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime
        myTransientObjectDriver['registration'] = ele.registration
        myTransientObjectDriver['vtype'] = ele.vtype
        myTransientObjectDriver['complianceCheck'] = ele.complianceCheck
            
        ## iterate through numbers
        if ele.SigningUrlNumber:
            if ele.Signed:
                urlArray.append(ele.SigningUrlNumber)

        ## iterate through each date in datesList
        if len(ele.datesList) > 0:
            for item in ele.datesList:
                datesArray.append(item)
            myTransientObjectDriver['datesList'] = datesArray
        else:
            myTransientObjectDriver['datesList'] = [] 

        ################################## important part to look at ..... here i am going to add a 'field' that is not being saved, but will be returned to the front end... very 
        #### useful because this is going to put all the matching appointments into an array attached to the driver object they belong to ... something ive been doing on the front end

        ### step one .... I have mapped all the date data into an array now... which I will be formatting from now on, dont want to touch the actual data class
        # # if it can be avoided.
        datesObjectArray = []
        for dateObject in myDatesArray:
            if dateObject['driver_id'] == str(ele.driver_id):
                datesObjectArray.append(dateObject)

        myTransientObjectDriver['datesArray'] = datesObjectArray    

        # images version
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['driver_id'] == ele.name:
                imagesArray.append(imgObject)

        myTransientObjectDriver['imgArray'] = imagesArray  

        # # vehicles version
        # vehiclesArray = []
        # for vehicleObject in myVehiclesArray:
        #     if vehicleObject['driver_id'] == ele.name:
        #         vehiclesArray.append(vehicleObject)

        # myTransientObjectDriver['vehicleArray'] = vehiclesArray  

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   

    myFinalObject = {
        'drivers': myDriverArray,
        'dates': myDatesArray,
        'images': myImagesArray,
        'vehicles': myVehiclesArray,
    }   
    

    return myFinalObject

def returnVanOrderedData(vanList, scheduledDatesVan, imagesList, driversList, selectedDate=None):
    myVehiclesArray = []
    myImagesArray = []
    myVanDateArray = []
    myDriverArray = []     
    myWeekArray = []

    for ele in imagesList:
        myTransientImage = {}
        myTransientImage['driver_id'] = str(ele.driver_id)
        myTransientImage['vehicle_id'] = str(ele.vehicle_id)
        myTransientImage['image_id'] = ele.image_id
        myTransientImage['name'] = ele.name
        myTransientImage['countryOfIssue'] = ele.countryOfIssue
        myTransientImage['expiryDate'] = ele.expiryDate
        myTransientImage['dueDate'] = ele.dueDate
        myTransientImage['datePassed'] = ele.datePassed
        myTransientImage['photo'] = ele.photo
        myTransientImage['managerApprovedName'] = ele.managerApprovedName
        myTransientImage['managerApprovedDate'] = ele.managerApprovedDate
        myTransientImage['imagesLink'] = ele.imagesLink
        myTransientImage['verified'] = ele.verified
        myTransientImage['driverSigned'] = ele.driverSigned
        myTransientImage['points'] = ele.points
        myTransientImage['nextDVLAScreenshot'] = ele.nextDVLAScreenshot
        
        myImagesArray.append(myTransientImage)

    for ele in scheduledDatesVan:
        myTransientVehicleDate = {}
        myTransientVehicleDate['vehicleDate_id'] = str(ele.vehicleDate_id)
        myTransientVehicleDate['vehicle_id'] = str(ele.vehicle_id)
        myTransientVehicleDate['driver_id'] = str(ele.driver_id)
        myTransientVehicleDate['date'] = ele.date

        myVanDateArray.append(myTransientVehicleDate)

    for ele in vanList:
        myTransientVehicle = {}
        myTransientVehicle['vehicle_id'] = ele.vehicle_id
        myTransientVehicle['registration'] = ele.registration
        myTransientVehicle['make'] = ele.make
        myTransientVehicle['model'] = ele.model
        myTransientVehicle['year'] = ele.year
        myTransientVehicle['companyOwned'] = ele.companyOwned
        myTransientVehicle['vtype'] = ele.vtype
        myTransientVehicle['quotePrice'] = str(ele.quotePrice)
        myTransientVehicle['invoice'] = str(ele.invoice)


        # images version
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['vehicle_id'] == ele.registration:
                imagesArray.append(imgObject)

        myTransientVehicle['imgArray'] = imagesArray  

        # dates version
        datesArray = []
        for dateObject in myVanDateArray:
            if dateObject['vehicle_id'] == ele.registration:
                datesArray.append(dateObject) 

        myTransientVehicle['datesArray'] = datesArray

        myVehiclesArray.append(myTransientVehicle)

       ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        myTransientObjectDriver['driver_id'] = str(ele.driver_id)
        myTransientObjectDriver['vehicle_name'] = ele.vehicle_name
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime 

         # dates version
        datesArray = []
        for dateObject in myVanDateArray:
            if dateObject['driver_id'] == str(ele.driver_id):
                datesArray.append(dateObject) 

        myTransientObjectDriver['vanDatesArray'] = datesArray

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   


        # find out today
    
    if selectedDate == None:
        print('hurray')
    else:
        # from the postman requests
        # myString = str(selectedDate).replace('%20', ' ').replace('date=', '').replace("b'", "").replace("'", "")

        # from the backend
        myString = str(selectedDate).replace("'b'", '').replace('{"date":"', '').replace('"', '').replace("b'", '').replace("}'", '')
        weekBeforeSunday = datetime.datetime.strptime(myString, '%a %b %d %Y').date()
        mostRecentSunday = weekBeforeSunday + datetime.timedelta(days=7)   

        for ele in myVanDateArray:
            if weekBeforeSunday <= datetime.datetime.strptime(ele['date'], '%a %b %d %Y').date() < mostRecentSunday:
                myWeekArray.append(ele)  


    myFinalObject = {
        'vehicles': myVehiclesArray,
        'drivers' : myDriverArray,
        'modifiedvehicles' : myWeekArray
    }   

    return myFinalObject

def invoice(driversList, datesList, vehiclesList, deductions, support, selectedDate=None):


    #### add an array of registrations for the vehicles that are owned by the company
    #### add array containing the status of the drivers

    myImagesArray = []
    myDriverArray = []
    myDatesArray = []
    myVehiclesArray = []
    myDeductionArray = []
    mySupportArray = []

    for ele in deductions:
        myTransientDeduction = {}
        myTransientDeduction['deduction_id'] = ele.deduction_id
        myTransientDeduction['date_id'] = str(ele.date_id)
        myTransientDeduction['name'] = ele.name
        myTransientDeduction['amount'] = str(ele.amount)

        myDeductionArray.append(myTransientDeduction)

    for ele in support:
        myTransientSupport = {}
        myTransientSupport['support_id'] = ele.support_id
        myTransientSupport['date_id'] = str(ele.date_id)
        myTransientSupport['name'] = ele.name
        myTransientSupport['amount'] = str(ele.amount)

        mySupportArray.append(myTransientSupport)

    for ele in vehiclesList:
        myTransientVehicle = {}
        myTransientVehicle['vehicle_id'] = ele.vehicle_id
        myTransientVehicle['registration'] = ele.registration
        myTransientVehicle['make'] = ele.make
        myTransientVehicle['model'] = ele.model
        myTransientVehicle['year'] = ele.year
        myTransientVehicle['companyOwned'] = ele.companyOwned
        myTransientVehicle['vtype'] = ele.vtype
        myTransientVehicle['quotePrice'] = str(ele.quotePrice)
        myTransientVehicle['invoice'] = str(ele.invoice)

        myVehiclesArray.append(myTransientVehicle)

        # images version
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['vehicle_id'] == ele.registration:
                print(imgObject)
                imagesArray.append(imgObject)

        myTransientVehicle['imgArray'] = imagesArray  

    for ele in datesList:
        myTransientObjectDates = {}

        myTransientObjectDates['date_id'] = ele.date_id
        myTransientObjectDates['name'] = ele.name
        myTransientObjectDates['inOff'] = ele.inOff
        myTransientObjectDates['route'] = ele.route
        myTransientObjectDates['routeNumber'] = ele.routeNumber
        myTransientObjectDates['logOut_time'] = ele.logOut_time
        myTransientObjectDates['logIn_time'] = ele.logIn_time
        myTransientObjectDates['location'] = ele.location
        myTransientObjectDates['date'] = ele.date
        myTransientObjectDates['driver_id'] = str(ele.driver_id)
        myTransientObjectDates['mileage'] = ele.mileage
        myTransientObjectDates['start_mileage'] = ele.start_mileage
        myTransientObjectDates['finish_mileage'] = ele.finish_mileage
        myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
        myTransientObjectDates['parcel'] = ele.parcel
        myTransientObjectDates['parcelNotDelivered'] = ele.parcelNotDelivered
        myTransientObjectDates['TORH'] = ele.TORH
    
        myDeductionSum = 0
        mySupportSum = 0
        total = 0
        deductionList = []
        supportList = []

        for element in myDeductionArray: 
            if element['date_id'] == str(ele.date_id):
                myDeductionSum += float(element['amount'][3::])
                deductionList.append(element)
                
        myTransientObjectDates['deductionSum'] = 'GB£{}'.format(myDeductionSum) 
        myTransientObjectDates['deductionList'] = deductionList 

        for element in mySupportArray: 
            if element['date_id'] == str(ele.date_id):
                mySupportSum += float(element['amount'][3::])
                supportList.append(element)

        total = mySupportSum - myDeductionSum        

        myTransientObjectDates['supportSum'] ='GB£{}'.format(mySupportSum) 
        myTransientObjectDates['supportList'] = supportList 

        myTransientObjectDates['total'] = total


        myDatesArray.append(myTransientObjectDates)

    ## array for checking urls
    urlArray = []


    ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        datesArray = []
        myTransientObjectDriver['driver_id'] = str(ele.driver_id)
        myTransientObjectDriver['vehicle_name'] = ele.driver_id
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime
            
        ## iterate through numbers
        if ele.SigningUrlNumber:
            if ele.Signed:
                urlArray.append(ele.SigningUrlNumber)

        ## iterate through each date in datesList
        if len(ele.datesList) > 0:
            for item in ele.datesList:
                datesArray.append(item)
            myTransientObjectDriver['datesList'] = datesArray
        else:
            myTransientObjectDriver['datesList'] = [] 

        ################################## important part to look at ..... here i am going to add a 'field' that is not being saved, but will be returned to the front end... very 
        #### useful because this is going to put all the matching appointments into an array attached to the driver object they belong to ... something ive been doing on the front end

        ### step one .... I have mapped all the date data into an array now... which I will be formatting from now on, dont want to touch the actual data class
        # # if it can be avoided.
        datesObjectArray = []
        for dateObject in myDatesArray:
            if dateObject['driver_id'] == str(ele.driver_id):
                datesObjectArray.append(dateObject)

        myTransientObjectDriver['datesArray'] = datesObjectArray    

        # images version
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['driver_id'] == str(ele.driver_id):
                imagesArray.append(imgObject)

        myTransientObjectDriver['imgArray'] = imagesArray  

        # # vehicles version
        # vehiclesArray = []
        # for vehicleObject in myVehiclesArray:
        #     if vehicleObject['driver_id'] == ele.name:
        #         vehiclesArray.append(vehicleObject)

        # myTransientObjectDriver['vehicleArray'] = vehiclesArray  

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   


    # find out today
    if selectedDate == None:
        currentDate = datetime.date.today()
        dateWeekDay = currentDate.weekday()
        mostRecentSunday = 0
        weekBeforeSunday = 0
        twoWeeksBeforeSunday = 0
        fourWeeksBeforeSunday = 0
        dateWeekDay+=1
        if currentDate.weekday() == 6:
            mostRecentSunday = currentDate 
            weekBeforeSunday = currentDate - datetime.timedelta(days=7) 
        else:
            mostRecentSunday = currentDate - datetime.timedelta(days=dateWeekDay)
            weekBeforeSunday = mostRecentSunday - datetime.timedelta(days=7)
            twoWeeksBeforeSunday = mostRecentSunday - datetime.timedelta(days=14)
            fourWeeksBeforeSunday = mostRecentSunday - datetime.timedelta(days=28)  
    else:
        # from the postman requests
        # myString = str(selectedDate).replace('%20', ' ').replace('date=', '').replace("b'", "").replace("'", "")

        # from the backend
        myString = str(selectedDate).replace("'b'", '').replace('{"date":"', '').replace('"', '').replace("b'", '').replace("}'", '')
        weekBeforeSunday = datetime.datetime.strptime(myString, '%a %b %d %Y').date()
        mostRecentSunday = weekBeforeSunday + datetime.timedelta(days=7)   

    print(weekBeforeSunday, mostRecentSunday)    
        
    # # create array to go onto the driver that will contain all the drivers dates
    payrollArray = []

    # # inside of the driver array loop write some logic that links each date to the driver and push the date into the driver date array
    myWeekArray = []
    for ele in myDriverArray:
        if ele['status'] != 'OffboardedForever':
            for date in ele["datesArray"]:
                isValidDate = 0

                try:
                    datetime.datetime.strptime(date['date'], '%a %b %d %Y')
                except ValueError:
                    isValidDate = 1

                if isValidDate == 0:
                    if weekBeforeSunday <= datetime.datetime.strptime(date['date'], '%a %b %d %Y').date() < mostRecentSunday:
                        myWeekArray.append(date)      

        ##################################   FINAL INVOICE CREATION SECTION ############################################################################                    
    df = pd.DataFrame(myWeekArray)     # this is a dataframe with all the dates in the week we want      
    myInvoiceObj = {}
    allDatesArray = []
    myNum = 0
    while myNum < len(df):
        localArray = []
        for element in df:
            # this line adds the data to the local array
            localArray.append(df[element][df[element].index[myNum]])
        myNum += 1        
        allDatesArray.append(localArray)
        localArray = [] 

    myObj = {
        '0': 0.0,
        'Full Standard Van Route': 121.8,
        'Full Large Van Route': 141.8,
        'Transportation Route': 100,
        'MFN Route': 70,
        'Missort Route': 121.8,
        'Classroom Training': 75,
        'Ride Along': 75,
        'Sweeper': 121.8,
        'None': 0.0
    }
    
    for dateItem in allDatesArray:
        print(dateItem[7])
        if dateItem[9] in myInvoiceObj:
         #   print(myInvoiceObj[dateItem[9]]['route'])

            # sums the routes
            myInvoiceObj[dateItem[9]]['route'] = myInvoiceObj[dateItem[9]]['route'] + float([myObj[dateItem[3]]][0])

            # sums the routes
            myInvoiceObj[dateItem[9]]['parcels'] = myInvoiceObj[dateItem[9]]['parcels'] + float(dateItem[14])

            # sums the routes
            print(float(dateItem[10])*0.17)
            myInvoiceObj[dateItem[9]]['mileage'] = myInvoiceObj[dateItem[9]]['mileage'] + float(dateItem[10])*0.17

            # sums the deduction
            myMoneyObj = float(myInvoiceObj[dateItem[9]]['deduction'][3::]) + float(dateItem[17][3::])
            myInvoiceObj[dateItem[9]]['deduction'] = 'GB£{}'.format(myMoneyObj) 

            # sums the support
            mySupportObj = float(myInvoiceObj[dateItem[9]]['support'][3::]) + float(dateItem[19][3::])
            myInvoiceObj[dateItem[9]]['support'] = 'GB£{}'.format(mySupportObj) 

            
        else:
            myInvoiceObj[dateItem[9]] = {
                    'route': myObj[dateItem[3]],
                    'parcels': dateItem[14],
                    'mileage': dateItem[12]*0.17,
                    'deduction': dateItem[17],
                    'support': dateItem[19],
                    'location': dateItem[7] 
                }

    myFinalObject = {
        'myOneWeekArray': myInvoiceObj,
        'datesList': myWeekArray
    }   

    return myFinalObject          


def tokenizer(managerList, requestBody):
    isAuthenticated = False
    print(requestBody)
    submittedemail = ''
    myString = str(requestBody).replace("b'", "").replace("'", "")

    # from the backend
    # myString = str(selectedDate).replace("'b'", '').replace('{"date":"', '').replace('"', '').replace("b'", '').replace("}'", '')

    return isAuthenticated


def complianceCheck(vanList, scheduledDatesVan, imagesList, driversList, selectedDate=None):
    myVehiclesArray = []
    myImagesArray = []
    myVanDateArray = []
    myDriverArray = []     
    myWeekArray = []

    for ele in imagesList:
        myTransientImage = {}
        myTransientImage['driver_id'] = str(ele.driver_id)
        myTransientImage['vehicle_id'] = str(ele.vehicle_id)
        myTransientImage['image_id'] = ele.image_id
        myTransientImage['name'] = ele.name
        myTransientImage['countryOfIssue'] = ele.countryOfIssue
        myTransientImage['expiryDate'] = ele.expiryDate
        myTransientImage['dueDate'] = ele.dueDate
        myTransientImage['datePassed'] = ele.datePassed
        myTransientImage['photo'] = ele.photo
        myTransientImage['managerApprovedName'] = ele.managerApprovedName
        myTransientImage['managerApprovedDate'] = ele.managerApprovedDate
        myTransientImage['imagesLink'] = ele.imagesLink
        myTransientImage['verified'] = ele.verified
        myTransientImage['driverSigned'] = ele.driverSigned
        myTransientImage['points'] = ele.points
        myTransientImage['nextDVLAScreenshot'] = ele.nextDVLAScreenshot
        
        myImagesArray.append(myTransientImage)

    for ele in vanList:
        myTransientVehicle = {}
        myTransientVehicle['vehicle_id'] = ele.vehicle_id
        myTransientVehicle['registration'] = ele.registration
        myTransientVehicle['make'] = ele.make
        myTransientVehicle['model'] = ele.model
        myTransientVehicle['year'] = ele.year
        myTransientVehicle['companyOwned'] = ele.companyOwned
        myTransientVehicle['vtype'] = ele.vtype
        myTransientVehicle['quotePrice'] = str(ele.quotePrice)
        myTransientVehicle['invoice'] = str(ele.invoice)


        # images version
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['vehicle_id'] == ele.registration:
                imagesArray.append(imgObject)

        myTransientVehicle['imgArray'] = imagesArray  

        myVehiclesArray.append(myTransientVehicle)

       ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        myTransientObjectDriver['driver_id'] = str(ele.driver_id)
        myTransientObjectDriver['vehicle_name'] = ele.vehicle_name
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime 
        myTransientObjectDriver['vanOwner'] = ele.vanOwner
        myTransientObjectDriver['registration'] = ele.registration
        myTransientObjectDriver['vtype'] = ele.vtype
        myTransientObjectDriver['complianceCheck'] = ele.complianceCheck

                # images version
        print('hello')
        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['driver_id'] == str(ele.driver_id):
                imagesArray.append(imgObject)

        myTransientObjectDriver['imgArray'] = imagesArray  

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   


        # find out today
    
    if selectedDate == None:
        print('hurray')
    else:
        # from the postman requests
        # myString = str(selectedDate).replace('%20', ' ').replace('date=', '').replace("b'", "").replace("'", "")

        # from the backend
        myString = str(selectedDate).replace("'b'", '').replace('{"date":"', '').replace('"', '').replace("b'", '').replace("}'", '')
        weekBeforeSunday = datetime.datetime.strptime(myString, '%a %b %d %Y').date()
        mostRecentSunday = weekBeforeSunday + datetime.timedelta(days=7)   

        for ele in myVanDateArray:
            if weekBeforeSunday <= datetime.datetime.strptime(ele['date'], '%a %b %d %Y').date() < mostRecentSunday:
                myWeekArray.append(ele)  
        # images version

        imagesArray = []
        for imgObject in myImagesArray:
            if imgObject['driver_id'] == str(ele.driver_id):
                imagesArray.append(imgObject)

        myTransientObjectDriver['imgArray'] = imagesArray  

    myFinalObject = {
        'vehicles': myVehiclesArray,
        'drivers' : myDriverArray,
        'modifiedvehicles' : myWeekArray

    }   

    return myFinalObject

def addDatedDriver(driversList, datesList, selectedDate=None):
    myDriverArray = []
    myDatesArray = []

    if selectedDate == None:
        currentDate = datetime.date.today()
        dateWeekDay = currentDate.weekday()
        mostRecentSunday = 0
        weekBeforeSunday = 0
        twoWeeksBeforeSunday = 0
        fourWeeksBeforeSunday = 0
        dateWeekDay+=1
        if currentDate.weekday() == 6:
            mostRecentSunday = currentDate 
            weekBeforeSunday = currentDate - datetime.timedelta(days=7) 
        else:
            mostRecentSunday = currentDate - datetime.timedelta(days=dateWeekDay)
            weekBeforeSunday = mostRecentSunday - datetime.timedelta(days=7)
            twoWeeksBeforeSunday = mostRecentSunday - datetime.timedelta(days=14)
            fourWeeksBeforeSunday = mostRecentSunday - datetime.timedelta(days=28) 
            nextSunday = mostRecentSunday + datetime.timedelta(days=14) 
        
        for ele in datesList:
            if mostRecentSunday <= datetime.datetime.strptime(ele.date, '%a %b %d %Y').date() < nextSunday:
                myTransientObjectDates = {}

                myTransientObjectDates['date_id'] = ele.date_id
                myTransientObjectDates['name'] = ele.name
                myTransientObjectDates['inOff'] = ele.inOff
                myTransientObjectDates['route'] = ele.route
                myTransientObjectDates['routeNumber'] = ele.routeNumber
                myTransientObjectDates['logOut_time'] = ele.logOut_time
                myTransientObjectDates['logIn_time'] = ele.logIn_time
                myTransientObjectDates['location'] = ele.location
                myTransientObjectDates['date'] = ele.date
                myTransientObjectDates['driver_id'] = str(ele.driver_id)
                myTransientObjectDates['mileage'] = ele.mileage
                myTransientObjectDates['start_mileage'] = ele.start_mileage
                myTransientObjectDates['finish_mileage'] = ele.finish_mileage
                myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
                myTransientObjectDates['parcel'] = ele.parcel
                myTransientObjectDates['parcelNotDelivered'] = ele.parcelNotDelivered
                myTransientObjectDates['TORH'] = ele.TORH
                myTransientObjectDates['totalRouteForDay'] = ele.totalRouteForDay

                myDatesArray.append(myTransientObjectDates)
    else:
        # from the postman requests
        # myString = str(selectedDate).replace('%20', ' ').replace('date=', '').replace("b'", "").replace("'", "")

        # from the backend
        myString = str(selectedDate).replace("'b'", '').replace('{"date":"', '').replace('"', '').replace("b'", '').replace("}'", '')
        weekBeforeSunday = datetime.datetime.strptime(myString, '%a %b %d %Y').date()
        mostRecentSunday = weekBeforeSunday + datetime.timedelta(days=14)   

        for ele in datesList:
            if weekBeforeSunday <= datetime.datetime.strptime(ele.date, '%a %b %d %Y').date() < mostRecentSunday:
                myTransientObjectDates = {}

                myTransientObjectDates['date_id'] = ele.date_id
                myTransientObjectDates['name'] = ele.name
                myTransientObjectDates['inOff'] = ele.inOff
                myTransientObjectDates['route'] = ele.route
                myTransientObjectDates['routeNumber'] = ele.routeNumber
                myTransientObjectDates['logOut_time'] = ele.logOut_time
                myTransientObjectDates['logIn_time'] = ele.logIn_time
                myTransientObjectDates['location'] = ele.location
                myTransientObjectDates['date'] = ele.date
                myTransientObjectDates['driver_id'] = str(ele.driver_id)
                myTransientObjectDates['mileage'] = ele.mileage
                myTransientObjectDates['start_mileage'] = ele.start_mileage
                myTransientObjectDates['finish_mileage'] = ele.finish_mileage
                myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
                myTransientObjectDates['parcel'] = ele.parcel
                myTransientObjectDates['parcelNotDelivered'] = ele.parcelNotDelivered
                myTransientObjectDates['TORH'] = ele.TORH

                myDatesArray.append(myTransientObjectDates)



    for ele in driversList:
        myTransientObjectDriver = {}
        myTransientObjectDriver['driver_id'] = str(ele.driver_id)
        myTransientObjectDriver['vehicle_name'] = ele.vehicle_name
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime 
        myTransientObjectDriver['vanOwner'] = ele.vanOwner
        myTransientObjectDriver['registration'] = ele.registration
        myTransientObjectDriver['vtype'] = ele.vtype
        myTransientObjectDriver['complianceCheck'] = ele.complianceCheck

        ## iterate through each date in datesList fuck me
        datesArray = []
        for item in myDatesArray:
            if item['driver_id'] == str(ele.driver_id):
                datesArray.append(item)
        myTransientObjectDriver['datesList'] = datesArray

        myDriverArray.append(myTransientObjectDriver) 

    dateArrayLocal = []
    for item in myDatesArray:
        if item['name'] == 'bottomRoutes':
            dateArrayLocal.append(item)

    myFinalObject = {
        'drivers': myDriverArray,
        'bottomArray': dateArrayLocal
    } 

    return myFinalObject

def documentsDriversOnly(driversList, imagesList): 
    myDriverArray = []  
    imageObj = {}   

    for item in imagesList:
        if str(item.driver_id) in imageObj:
            myTransientImage = {}
            myTransientImage['driver_id'] = str(item.driver_id)
            myTransientImage['vehicle_id'] = str(item.vehicle_id)
            myTransientImage['image_id'] = item.image_id
            myTransientImage['name'] = item.name
            myTransientImage['countryOfIssue'] = item.countryOfIssue
            myTransientImage['expiryDate'] = item.expiryDate
            myTransientImage['dueDate'] = item.dueDate
            myTransientImage['datePassed'] = item.datePassed
            myTransientImage['photo'] = item.photo
            myTransientImage['managerApprovedName'] = item.managerApprovedName
            myTransientImage['managerApprovedDate'] = item.managerApprovedDate
            myTransientImage['imagesLink'] = item.imagesLink
            myTransientImage['verified'] = item.verified
            myTransientImage['driverSigned'] = item.driverSigned
            myTransientImage['points'] = item.points
            myTransientImage['nextDVLAScreenshot'] = item.nextDVLAScreenshot
            imageObj[str(item.driver_id)].append(myTransientImage)
        else:
            imageObj[str(item.driver_id)] = []
            myTransientImage = {}
            myTransientImage['driver_id'] = str(item.driver_id)
            myTransientImage['vehicle_id'] = str(item.vehicle_id)
            myTransientImage['image_id'] = item.image_id
            myTransientImage['name'] = item.name
            myTransientImage['countryOfIssue'] = item.countryOfIssue
            myTransientImage['expiryDate'] = item.expiryDate
            myTransientImage['dueDate'] = item.dueDate
            myTransientImage['datePassed'] = item.datePassed
            myTransientImage['photo'] = item.photo
            myTransientImage['managerApprovedName'] = item.managerApprovedName
            myTransientImage['managerApprovedDate'] = item.managerApprovedDate
            myTransientImage['imagesLink'] = item.imagesLink
            myTransientImage['verified'] = item.verified
            myTransientImage['driverSigned'] = item.driverSigned
            myTransientImage['points'] = item.points
            myTransientImage['nextDVLAScreenshot'] = item.nextDVLAScreenshot
            imageObj[str(item.driver_id)].append(myTransientImage)

       ## recreate the driver dataset
    for ele in driversList:
        myTransientObjectDriver = {}
        myTransientObjectDriver['driver_id'] = ele.driver_id
        myTransientObjectDriver['vehicle_name'] = ele.vehicle_name
        myTransientObjectDriver['deleteButton'] = ele.deleteButton
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime 
        myTransientObjectDriver['vanOwner'] = ele.vanOwner 
        myTransientObjectDriver['registration'] = ele.registration 
        myTransientObjectDriver['vtype'] = ele.vtype 
        myTransientObjectDriver['complianceCheck'] = ele.complianceCheck 

        for item in imageObj:
            if item == str(ele.driver_id):
                myTransientObjectDriver['imgArray'] = imageObj[item]
            else:
                myTransientObjectDriver['imgArray'] = []

        ## append object to array
        myDriverArray.append(myTransientObjectDriver)   


    myFinalObject = {
        'drivers' : myDriverArray
    }   

    return myFinalObject

def dailyService(driversList, datesList, deductions, support, selectedDate=None):
    myDriverArray = []
    myDatesArray = []
    myDeductionArray = []
    mySupportArray = []

    print(driversList)

    if selectedDate == None:
        currentDate = datetime.date.today()

        for ele in deductions:
            if not ele.date:
                print('')
            else:    
                if datetime.datetime.strptime(ele.date, '%a %b %d %Y').date() == currentDate:
                    myTransientDeduction = {}
                    myTransientDeduction['deduction_id'] = ele.deduction_id
                    myTransientDeduction['date_id'] = str(ele.date_id)
                    myTransientDeduction['name'] = ele.name
                    myTransientDeduction['date'] = ele.date
                    myTransientDeduction['amount'] = str(ele.amount)

                    myDeductionArray.append(myTransientDeduction)

        for ele in support:
            if not ele.date:
                print('')
            else:    
                if datetime.datetime.strptime(ele.date, '%a %b %d %Y').date() == currentDate:
                    myTransientSupport = {}
                    myTransientSupport['support_id'] = ele.support_id
                    myTransientSupport['date_id'] = str(ele.date_id)
                    myTransientSupport['date'] = ele.date
                    myTransientSupport['amount'] = str(ele.amount)

                    mySupportArray.append(myTransientSupport)    
        
        for ele in datesList:
            if datetime.datetime.strptime(ele.date, '%a %b %d %Y').date() == currentDate:
                myTransientObjectDates = {}

                myTransientObjectDates['date_id'] = ele.date_id
                myTransientObjectDates['name'] = ele.name
                myTransientObjectDates['inOff'] = ele.inOff
                myTransientObjectDates['route'] = ele.route
                myTransientObjectDates['routeNumber'] = ele.routeNumber
                myTransientObjectDates['logOut_time'] = ele.logOut_time
                myTransientObjectDates['logIn_time'] = ele.logIn_time
                myTransientObjectDates['location'] = ele.location
                myTransientObjectDates['date'] = ele.date
                myTransientObjectDates['driver_id'] = str(ele.driver_id)
                myTransientObjectDates['mileage'] = ele.mileage
                myTransientObjectDates['start_mileage'] = ele.start_mileage
                myTransientObjectDates['finish_mileage'] = ele.finish_mileage
                myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
                myTransientObjectDates['parcel'] = ele.parcel
                myTransientObjectDates['parcelNotDelivered'] = ele.parcelNotDelivered
                myTransientObjectDates['TORH'] = ele.TORH
                myTransientObjectDates['totalRouteForDay'] = ele.totalRouteForDay

                myDeductionSum = 0
                mySupportSum = 0
                total = 0
                deductionList = []
                supportList = []

                for element in myDeductionArray: 
                    if element['date_id'] == str(ele.date_id):
                        myDeductionSum += float(element['amount'][3::])
                        deductionList.append(element)
                        
                myTransientObjectDates['deductionSum'] = 'GB£{}'.format(myDeductionSum) 
                myTransientObjectDates['deductionList'] = deductionList 

                for element in mySupportArray: 
                    if element['date_id'] == str(ele.date_id):
                        mySupportSum += float(element['amount'][3::])
                        supportList.append(element)

                total = mySupportSum - myDeductionSum        

                myTransientObjectDates['supportSum'] ='GB£{}'.format(mySupportSum) 
                myTransientObjectDates['supportList'] = supportList 

                myTransientObjectDates['total'] = total

                myDatesArray.append(myTransientObjectDates)
    else:
        # from the postman requests
        # myString = str(selectedDate).replace('%20', ' ').replace('date=', '').replace("b'", "").replace("'", "")
        # print('*********************** my string: ', myString)

        # from the backend
        myString = str(selectedDate).replace("'b'", '').replace('{"date":"', '').replace('"', '').replace("b'", '').replace("}'", '') 
        selectedDate = datetime.datetime.strptime(myString, '%a %b %d %Y').date()

        for ele in deductions:
            if not ele.date:
                print('')
            else:    
                if datetime.datetime.strptime(ele.date, '%a %b %d %Y').date() == selectedDate:
                    myTransientDeduction = {}
                    myTransientDeduction['deduction_id'] = ele.deduction_id
                    myTransientDeduction['date_id'] = str(ele.date_id)
                    myTransientDeduction['name'] = ele.name
                    myTransientDeduction['amount'] = str(ele.amount)
                    myTransientDeduction['date'] = ele.date

                    myDeductionArray.append(myTransientDeduction)

        for ele in support:
            if not ele.date:
                print('')
            else: 
                if datetime.datetime.strptime(ele.date, '%a %b %d %Y').date() == selectedDate:
                    myTransientSupport = {}
                    myTransientSupport['support_id'] = ele.support_id
                    myTransientSupport['date_id'] = str(ele.date_id)
                    myTransientSupport['name'] = ele.name
                    myTransientSupport['date'] = ele.date
                    myTransientSupport['amount'] = str(ele.amount)

                    mySupportArray.append(myTransientSupport)  

        for ele in datesList:
            if datetime.datetime.strptime(ele.date, '%a %b %d %Y').date() == selectedDate:
                myTransientObjectDates = {}

                myTransientObjectDates['date_id'] = ele.date_id
                myTransientObjectDates['name'] = ele.name
                myTransientObjectDates['inOff'] = ele.inOff
                myTransientObjectDates['route'] = ele.route
                myTransientObjectDates['routeNumber'] = ele.routeNumber
                myTransientObjectDates['logOut_time'] = ele.logOut_time
                myTransientObjectDates['logIn_time'] = ele.logIn_time
                myTransientObjectDates['location'] = ele.location
                myTransientObjectDates['date'] = ele.date
                myTransientObjectDates['driver_id'] = str(ele.driver_id)
                myTransientObjectDates['mileage'] = ele.mileage
                myTransientObjectDates['start_mileage'] = ele.start_mileage
                myTransientObjectDates['finish_mileage'] = ele.finish_mileage
                myTransientObjectDates['timeDifference'] = timeDifference(ele.logIn_time, ele.logOut_time)
                myTransientObjectDates['parcel'] = ele.parcel
                myTransientObjectDates['parcelNotDelivered'] = ele.parcelNotDelivered
                myTransientObjectDates['TORH'] = ele.TORH

                myDeductionSum = 0
                mySupportSum = 0
                total = 0
                deductionList = []
                supportList = []

                for element in myDeductionArray: 
                    if element['date_id'] == str(ele.date_id):
                        myDeductionSum += float(element['amount'][3::])
                        deductionList.append(element)
                        
                myTransientObjectDates['deductionSum'] = 'GB£{}'.format(myDeductionSum) 
                myTransientObjectDates['deductionList'] = deductionList 

                for element in mySupportArray: 
                    if element['date_id'] == str(ele.date_id):
                        mySupportSum += float(element['amount'][3::])
                        supportList.append(element)

                total = mySupportSum - myDeductionSum        

                myTransientObjectDates['supportSum'] ='GB£{}'.format(mySupportSum) 
                myTransientObjectDates['supportList'] = supportList 

                myTransientObjectDates['total'] = total

                myDatesArray.append(myTransientObjectDates)



    for ele in driversList:
        myTransientObjectDriver = {}
        myTransientObjectDriver['driver_id'] = str(ele.driver_id)
        myTransientObjectDriver['vehicle_name'] = ele.vehicle_name
        myTransientObjectDriver['name'] = ele.name
        myTransientObjectDriver['location'] = ele.location
        myTransientObjectDriver['email'] = ele.email
        myTransientObjectDriver['phone'] = ele.phone
        myTransientObjectDriver['address'] = ele.address
        myTransientObjectDriver['status'] = ele.status
        myTransientObjectDriver['DriverUniqueId'] = ele.DriverUniqueId
        myTransientObjectDriver['SigningUrlNumber'] = ele.SigningUrlNumber
        myTransientObjectDriver['Signed'] = ele.Signed
        myTransientObjectDriver['approvedBy'] = ele.approvedBy
        myTransientObjectDriver['approvedDateAndTime'] = ele.approvedDateAndTime 
        myTransientObjectDriver['vanOwner'] = ele.vanOwner
        myTransientObjectDriver['registration'] = ele.registration
        myTransientObjectDriver['vtype'] = ele.vtype
        myTransientObjectDriver['complianceCheck'] = ele.complianceCheck

        ## iterate through each date in datesList fuck me
        datesArray = []
        for item in myDatesArray:
            if item['driver_id'] == str(ele.driver_id):
                datesArray.append(item)
        myTransientObjectDriver['datesList'] = datesArray

        myDriverArray.append(myTransientObjectDriver) 

    myFinalObject = {
        'drivers': myDriverArray,
    } 

    return myFinalObject
