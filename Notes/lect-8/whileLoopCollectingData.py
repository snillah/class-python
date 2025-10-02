
import csv
localData = [] 
def initalData(readData):
     with open("student.csv",'w',newline='') as file:
                    writeValues = csv.writer(file)
                    writeValues.writerow(['Name','Age','Role','City'])
                    print("@@",readData)
                    writeValues.writerows(readData)      
def getDatFunction():
        try:
             with open("student.csv",'r') as file:
                readValues = csv.reader(file)
                for data in readValues:
                      if data:
                        localData.append(data)
                    #   print("@@=>",data)
        except FileNotFoundError:
                initalData([])
                print("File Not found.Creating File")

        finally:
             print("Execution Finished")

# Activities
def InsertFunction (addData):
        try:
             with open("student.csv",'a',newline='') as file:
                addingNewValue = csv.writer(file)
                # localData.append(addData)
                addingNewValue.writerow(addData)

        except FileNotFoundError:
                 print("File Not found.")

        finally:
             print("Add Execution Finished")

def ViewDatFunction():
        try:
             with open("student.csv",'r') as file:
                readValues = csv.reader(file)
                for data in readValues:
                      print(data)
        except FileNotFoundError:
                initalData([])
                print("File Not found.Creating File")

        finally:
             print("Execution Finished")

def DeleteDataFunction(data):
        tempData = []
        try:
             with open("student.csv",'r') as file:
                readValues = csv.reader(file)
                for list in readValues:
                      for item in list:
                            if data not in item:
                                  continue
                tempData.append(list)
                    
                # print("Jump Data",tempData)
                initalData(tempData)
                                
        except FileNotFoundError:
                initalData([])
                print("File Not found.Creating File")

        finally:
             print("Execution Finished")


check =1
c = ""
getDatFunction()
while check:
    print("Insert - 1,View - 2,Delete - 3, LogOut - 0")
    if c == "":
        c = int(input("Enter you Choice : "))
    else:
        c
    match c:
        case 1|"1": 
            data =[]
            print("Add New Data")
            name = input("Enter your Name: ")
            age = input("Enter your age: ")
            role= input("Enter your Role: ")
            city = input("Enter your City: ")
            
            if(name and age and role and city):
                # data.append([name,age,role,city])
                InsertFunction([name,age,role,city])
                print("Successfully Add:")
                c=""
            else:
                c=1
                print("enter all the details")
        case 2:
                ViewDatFunction()
                c=""
        case 3:
                deleteName = input("Enter the Name : ")
                if deleteName == "":
                    c=3
                else:
                    DeleteDataFunction(deleteName)
                    print("Delete")
                    c=""
        case 0:
                print("Thank you")
                check = 0
                break
        case _:
                c =""

print("report",localData)

