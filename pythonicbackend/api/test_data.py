import csv
import pandas as pd
import numpy as np
import math
import glob
import datetime

# always put stuff in functions... it scopes your variables and its cleaner.. making different functions do different things is modular and good code
def importData(schedule, drivers, driverManager, ScheduledDatesManager):

    # create array
    myArray = []

    # create variable for import

    sun = pd.read_csv("sunday.csv")
    mon = pd.read_csv("monday.csv")
    tue = pd.read_csv("tuesday.csv")
    wed = pd.read_csv("wednesday.csv")
    thu = pd.read_csv("thursday.csv")
    fri = pd.read_csv("friday.csv")
    sat = pd.read_csv("saturday.csv")
    data = pd.concat([sun,mon,tue,wed,thu,fri,sat], axis=0)
    
    data = data.reset_index(drop=True)






    # clean data -- good job, this is exactly what jupyter notebooks is for... youll need to do more of this kind of thing... for instances I removed the spaces from the 
    # csv file manually.... cant have spaces in names or will cause errors elsewhere
    # data.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
    # data.fillna(0,inplace = True)

    # driver = drivers.objects.create_driver(row[0]) -- example :)
    # loop through data and grab every row that belongs to the 'name' column in the data

    #print(data)

    # for d in data:
    #     if d['NAME'] == d['NAME']:
    #         driver = drivers.objects.create_driver(d['NAME'])  

    localList = []
    for row in data['NAME']:
        localList.append(row)
    mylist = list(dict.fromkeys(localList))
    for name in mylist:
        driver = drivers.objects.create_driver(name) 



        # driver = drivers.objects.create_driver(row)  




#   ##################################### adding the set of arrays to the backend ####################################


    myObj = {}

    df = pd.DataFrame(data)
    myNum = 0
    # Key in myObj = index of name in mylist
    AllDriversArray = []
    while myNum < len(data):
        localArray = []
        for element in df:
            # this line adds the data to the local array
            localArray.append(df[element][df[element].index[myNum]])
        myNum += 1        
        AllDriversArray.append(localArray)
        localArray = [] 

    for element in AllDriversArray:
        if mylist.index(element[0]) in myObj:
            myObj[mylist.index(element[0])].append([
                element[0], 
                element[1], 
                element[2], 
                element[3], 
                element[4], 
                element[5], 
                element[6], 
                element[7], 
                element[8], 
                element[9], 
                element[10], 
                ]
            )
        else:
            myObj[mylist.index(element[0])] = [
                [
                element[0], 
                element[1], 
                element[2], 
                element[3], 
                element[4], 
                element[5], 
                element[6], 
                element[7], 
                element[8], 
                element[9], 
                element[10], 
                ]
            ]  
    #print(myObj)    

    for key in myObj:
    
        for ele in myObj[key]:
            scheduledDate = schedule.objects.create_date(
                ele[0], 
                ele[1], 
                ele[2], 
                ele[3], 
                ele[4], 
                ele[5], 
                ele[6], 
                ele[7], 
                ele[8], 
                ele[9], 
                ele[10],
                key+1,)

                # myObj[mylist.index(df[element])].append(
                    
                # )

    # for key in myObj .... if it exists, add array to the list, else create key value pair


    # then iterate through myObj, for each element in it, iterate through that elements list and add that date to the backend with the foreign key of the driver equal to the key of myObj




  ##################################### End ########################################################################




    # while myNum < len(data):
    #     localArray = []
    #     for row in data:
    #         print(data[row])
    #         # print(mylist.index(data[row]))
    #         # this line adds the data to the local array
    #         # print(localArray.append(data[row][data[row].index[myNum]]))

    #     #     if myNum+1 in myObj:
    #     #         myObj[myNum+1].append(
    #     #             [
    #     #                 localArray[0], 
    #     #                 localArray[1], 
    #     #                 localArray[2], 
    #     #                 localArray[3], 
    #     #                 localArray[4], 
    #     #                 localArray[5], 
    #     #                 localArray[6], 
    #     #                 localArray[7], 
    #     #                 localArray[8], 
    #     #                 localArray[9], 
    #     #                 localArray[10], 
    #     #                 localArray[11], 
    #     #                 localArray[12],
    #     #                 localArray[13], 
    #     #                 localArray[14],
    #     #                 localArray[15],

    #     #             ]
    #     #         )
    #     #     else:
    #     #         myObj[myNum+1] = [
    #     #             localArray[0], 
    #     #             localArray[1], 
    #     #             localArray[2], 
    #     #             localArray[3], 
    #     #             localArray[4], 
    #     #             localArray[5], 
    #     #             localArray[6], 
    #     #             localArray[7], 
    #     #             localArray[8], 
    #     #             localArray[9], 
    #     #             localArray[10], 
    #     #             localArray[11], 
    #     #             localArray[12],
    #     #             localArray[13], 
    #     #             localArray[14],
    #     #             localArray[15],
    #     #         ]

    #     #     # this line adds the local array to the returned array
    #     #     myArray.append(localArray)    

    #     #     # this line uses array indexing to add each item to the date class

    #     # localArray = []    
    #     myNum = myNum + 1
    return myArray

        # scheduledDate = schedule.objects.create_date(
        #     localArray[0], 
        #     localArray[1], 
        #     localArray[2], 
        #     localArray[3], 
        #     localArray[4], 
        #     localArray[5], 
        #     localArray[6], 
        #     localArray[7], 
        #     localArray[8], 
        #     localArray[9], 
        #     localArray[10], 
        #     localArray[11], 
        #     localArray[12],
        #     localArray[13], 
        #     localArray[14],
        #     localArray[15],
        #     myNum+1)


#get our csv data script, the "data" will repsresents sunday
#any other day will be in a file named after it, expect for saturday

# create variable for import
# data = pd.read_csv("monday.csv")

#     # csv file manually.... cant have spaces in names or will cause errors elsewhere
# data.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
# data.fillna(0,inplace = True)
# #print(data)

# #count the number of ALL routes
# #data['IN'] = data['IN'].astype(float)
# numOfRoutes = data['IN'].value_counts()[1]  
# numOfMFNRoutes = data['ROUTE'].value_counts()['MFN']
# numOfFUllRoutes = numOfRoutes - numOfMFNRoutes


# #count number of LVP and LWP respectively
# numOfLVP = int(data['LVP'].sum())
# numOfLWP = int(data['LWP'].sum())
# numOfParcels = int(data['PARCEL'].sum())


# #here I just print out the results
# names = ['Routes: ',"FULL: ", 'MFN: ', 'LVP: ', 'LWP: ','Parcels: ']
# values = [str(numOfRoutes),str(numOfFUllRoutes),str(numOfMFNRoutes),
#           str(numOfLVP),str(numOfLWP),str(numOfParcels)]
# for i in names:
#     n1 = names[0] + f" " + values[0] 
#     n2 = names[1] + f" " + values[1]
#     n3 = names[2] + f" " + values[2]
#     n4 = names[3] + f" " + values[3]
#     n5 = names[4] + f" " + values[4]
#     n6 = names[5] + f" " + values[5]
#     text = f"Statistics for today:"
#     datStats = [text,n1,n2,n3,n4,n5,n6]
# #print("Monday Report:", datStats)
# #print(text,n1,n2,n3,n4,n5,n6)

