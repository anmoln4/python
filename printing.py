#Employee:Empcode
import datetime
import random
import calendar
import getMethod


def printWorkingHours(data,year,month):
    print("\n-------------Printing Working Hours Details Of Month ",month,",year",year,"-----------\n")
    years=data[0]
    months=data[1]
    day=data[2]
    hours=data[3]
    i=years.index(year)
    j=months[i].index(month)
    for k in range(0,len(day[i][j])):
        print("Date:  ",datetime.date(years[i],months[i][j],day[i][j][k]),"    Working Hours: ",hours[i][j][k])


def printSalary(data,year):
    print("\n-----------Printing Salary Details of Year",year ,"------------\n")
    years=data[0]
    months=data[1]
    salary=data[4]
    i=years.index(year)
    for j in range(0,len(months[i])):
        print("year:  ",year," and Month: ",months[i][j],"       salary:  ",salary[i][j])
        
def printBasicDetails(data):
    print("\n--------Printing Basic Detail-----\n")
    print("Employee cod:",data[0])
    print("Employee Name:",data[1])
    print("Date of joining:",data[2])
    now=datetime.datetime.now()
    print("Current Date is:",now.date())
    print("\n Working Hours Details of Current month----->")
    printWorkingHours(data[4],now.year,now.month)
    print("\n Salary Details of Current Year----->")
    printSalary(data[5],now.year)




def printContactDetails(data):
    print("\n------Printing Contact Details----\n")
    print("    Add: ",data[3][0])
    print("     Personal ph. ",data[3][1])
    print("   office ph. ",data[3][2])
