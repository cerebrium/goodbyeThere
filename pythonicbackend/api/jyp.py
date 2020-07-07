import csv
import pandas as pd
import numpy as np
import math
import glob
import datetime

import csv
import pandas as pd
import numpy as np
import math
import glob
import datetime




##----Here we first clean data and add Porper Date format to each day of the week

# df = pd.read_csv("sunday.csv")
# df.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
# df.fillna(0,inplace = True)
# df.drop(["VANS", "Unnamed: 16"],axis = 1,inplace = True, errors = 'ignore')
# df["date"] = "Sun 26 April 2020"
# df.to_csv("sunday.csv", index=False)
# df


# df = pd.read_csv("monday.csv")
# df.dropna(subset=['IN'], axis = 'rows', how ='all', inplace = True) 
# df.fillna(0,inplace = True)
# df.drop(["VANS", "Unnamed: 16","WEEK"],axis = 1,inplace = True, errors = 'ignore')
# df["date"] = "Mon 27 April 2020"
# df.to_csv("monday.csv", index=False)
# df

# df = pd.read_csv("tuesday.csv")
# df.dropna(subset=['IN'], axis = 'rows', how ='all', inplace = True) 
# df.fillna(0,inplace = True)
# df.drop(["VANS","WEEK"],axis = 1,inplace = True, errors = 'ignore')
# df["date"] = "Tue 28 April 2020"
# df.to_csv("tuesday.csv", index=False)
# df

# wed = pd.read_csv("wednesday.csv")
# wed.dropna(subset=['IN'], axis = 'rows', how ='all', inplace = True) 
# wed.fillna(0,inplace = True)
# wed.drop(["VANS","WEEK"],axis = 1,inplace = True, errors = 'ignore')
# wed["date"] = "Wed 29 April 2020"
# wed.to_csv("wednesday.csv", index=False)





# df = pd.read_csv("thursday.csv")
# df.dropna(subset=['IN'], axis = 'rows', how ='all', inplace = True) 
# df.fillna(0,inplace = True)
# df.drop(["VANS","WEEK"],axis = 1,inplace = True, errors = 'ignore')
# df["date"] = "Thu 30 April 2020"
# df.to_csv("thursday.csv", index=False)
# df


# df = pd.read_csv("friday.csv")
# df.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
# df.fillna(0,inplace = True)
# df.drop(["VANS","WEEK"],axis = 1,inplace = True, errors = 'ignore')
# df["date"] = "Fri 1 May 2020"
# df.to_csv("friday.csv", index=False)
# df


# df = pd.read_csv("saturday.csv")
# df.dropna(subset=['ROUTE'], axis = 'rows', how ='all', inplace = True) 
# df.fillna(0,inplace = True)
# df.drop(["VANS","WEEK"],axis = 1,inplace = True, errors = 'ignore')
# df["date"] = "Sat 2 May 2020"
# df.to_csv("saturday.csv", index=False)
# df


#here we combine our clean data
sun = pd.read_csv("sunday.csv")
mon = pd.read_csv("monday.csv")
tue = pd.read_csv("tuesday.csv")
wed = pd.read_csv("wednesday.csv")
thu = pd.read_csv("thursday.csv")
fri = pd.read_csv("friday.csv")
sat = pd.read_csv("saturday.csv")

myDatesArray = pd.concat([sun,mon,tue,wed,thu,fri,sat], axis=0)
myDatesArray = myDatesArray.reset_index(drop=True)
#myDatesArray
#myDatesArray.dtypes




####-----------------



from collections import defaultdict
myOneWeekArray = []

#Here i manually typed the date so i can access easy the data and not waste time with the date types
weekBeforeSunday = "Sun 26 May 2020"
mostRecentSunday = "Sun 3 May 2020"


# currentDate = datetime.date.today()
# dateWeekDay = currentDate.weekday()
# mostRecentSunday = 0
# weekBeforeSunday = 0
# twoWeeksBeforeSunday = 0
# fourWeeksBeforeSunday = 0
# dateWeekDay+=1
# if currentDate.weekday() > 0:
#     if currentDate.weekday() == 6:
#         print(currentDate)    
#     else:
#         mostRecentSunday = currentDate - datetime.timedelta(days=dateWeekDay)
#         weekBeforeSunday = mostRecentSunday - datetime.timedelta(days=7)
#         twoWeeksBeforeSunday = mostRecentSunday - datetime.timedelta(days=14)
#         fourWeeksBeforeSunday = mostRecentSunday - datetime.timedelta(days=28)
# print('last week was from: ', weekBeforeSunday, ' until: ', mostRecentSunday, ' last two weeks were: ', twoWeeksBeforeSunday, ' until ', mostRecentSunday)
      

for row in myDatesArray.itertuples(index=True, name='Pandas'):
    invoiceObject = {}
    #print(getattr(row, "date"))
    if getattr(row, "NAME") == getattr(row, "NAME"):
        if weekBeforeSunday < getattr(row, "date") < mostRecentSunday:
            if len(myOneWeekArray) > 0:
                for element in myOneWeekArray[0]:
                    if element == 'LVP':
                        myOneWeekArray[0][element] = myOneWeekArray[0][element] + getattr(row, "LVP")
                        if element == 'LWP':
                            myOneWeekArray[0][element] = myOneWeekArray[0][element] + getattr(row, "LWP")
                            #print(myOneWeekArray[0][element])
        else:
            invoiceObject['NAME'] = getattr(row, "NAME")
            invoiceObject['ROUTE'] = getattr(row, "ROUTE")
            invoiceObject['LWP'] = getattr(row, "LWP")
            invoiceObject['LVP'] = getattr(row, "LVP")
            invoiceObject['Deductions'] = getattr(row, "SUP")
            invoiceObject['Fuel'] = getattr(row, "FUEL")
            myOneWeekArray.append(invoiceObject)
                        
                        
#print(myOneWeekArray)
#type(myOneWeekArray)
                

    #count all routes
tempRoute = defaultdict(list)
for d in myOneWeekArray:
    tempRoute[d['NAME']].append(d['ROUTE'])
routes = [{'NAME': k, 'ROUTE': v, 'count': len(v)} for k, v in tempRoute.items()] 

totalRoutes = sum(item['count'] for item in routes)
print("Total routes for WEEK 18 is:", totalRoutes)


#here we will count MFN and BULK routes


    #count all LVP
# tempLVP = defaultdict(list)
# for d in myOneWeekArray:
#     tempLVP[d['NAME']].append(d['LVP'])
# myLVP = [{'NAME': k, 'LVP': v, 'count': len(v)} for k, v in tempLVP.items()] 
# myLVP
# # totalLVP = sum(item['count'] for item in myLVP)
# # print("Total LVP for WEEK 18 is:", totalLVP)