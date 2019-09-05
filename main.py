import attendance
import printing
import getMethod
import datetime

#employee=["EmpCode","Nmae","DoJ","ADDRESS","Working Hours","Permonth Salary"]
emp001=["Emp001","Lokesh Kumar"]
emp002=["Emp002","Reyansh Yadav"]

employees=[emp001,emp002]
totalEmp=len(employees)


for em in range(0,totalEmp):
    employees[em].append(getMethod.getDoj())
    employees[em].append(getMethod.getAddress())
    employees[em].append(getMethod.getJobDetails(employees[em][2]))
    employees[em].append(employees[em][4])




def findingEmp(emp1):
    for i in range(0,2):
        if (emp1==employees[i][0]):
            emp1=employees[i]
            return emp1
    return "ERRORCODE"



while 1:
    emp=findingEmp(input("Enter EmpId to access the details"))
    if(emp !="ERRORCODE"):
        printing.printBasicDetails(emp)
        while 1:
            print("\n-----------select one option from the given option---")
            key=int(input("1. Contact Details \n 2. Working Hours Details \n 3. Salary Details \n 4. Exit:"))
            if key==1:
                printing.printContactDetails(emp)
            if key==3 or key==2:
                while 1:
                    year=int(input("   Please Enter the year Details:"))
                    if year >=emp[2].year and year<=datetime.datetime.now().year:
                        break
                    else:
                        print("Invalid Year try with another input.")
                        continue
                if key==2:
                    month=int((input("  Enter the month:  ")))
                    printing.printWorkingHours(emp[4],year,month)
                else:
                    printing.printSalary(emp[4],year)
            if key==4:
                break
            if(input("\nTo display other Details press 'Y' and for exit press other key: ")!='y'):
            
                break
        else:
            
            
            print("Cannot find this EmpId ,try again with other EmpId.....")
            if(input("\nFor continue press 'Y' and for exit press other key: ")!='y'):
                
                break

        if(input("\n\n For other Employees, press 'Y' and for exit press other key: ")!='y'):
            
            break
  
