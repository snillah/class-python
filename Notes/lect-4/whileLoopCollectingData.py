


print("""
    ADD,
    VIEW,
    EDIT,
    DELETE, => CRUD OPEARTIONS
      """)
localData = [] 

check =1

while check:
    c = int(input("Enter you Choice : "))
    match c:
        case 1: 
            print("Add New Data")
            name = input("Enter your Name: ")
            age = input("Enter your age: ")
            role= input("Enter your Role: ")
            city = input("Enter your City: ")
            
            if(name and age and role and city):
                localData.append({name,age,role,city})
                print("Successfully Add:",localData)
            else:
                print("enter all the details")
        case _:
                print("Thank you")
                check = 0

print("report",localData)