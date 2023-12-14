import pymongo

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/" #mongo link
client = pymongo.MongoClient(CONNECTION_STRING)
database = client["yar_data"]
collection = database["test"] #mongoDB code to conect info to data

def add_employee():
    first_name = input("Enter the first name: ") #add list
    last_name = input("Enter the last name: ")
    job_title = input("Enter the job title: ")
    department = input("Enter the department: ")
    adres = input("Enter the address: ")
    telefon = input("Enter the phone number: ")
    ofice = input("Enter the office: ")
    
    employee = {
        "First Name": first_name,
        "Last Name": last_name,
        "Job Title": job_title,
        "Department": department,
        "adres": adres,
        "telefon": telefon,
        "ofice": ofice
    }
    
    collection.insert_one(employee)
    print("New employee added!")

def edit_employee(): #edit comand list
    first_name = input("Enter the first name of the employee you want to edit: ")
    last_name = input("Enter the last name of the employee you want to edit: ")
    
    employee = collection.find_one({"First Name": first_name, "Last Name": last_name})
    
    if employee:
        print("Employee found:")
        print(employee)
        
        new_job_title = input("Enter the new job title: ")
        new_department = input("Enter the new department: ")
        
        collection.update_one({"First Name": first_name, "Last Name": last_name},
                              {"$set": {"Job Title": new_job_title, "Department": new_department}})
        
        print("Employee updated!")
    else:
        print("Employee with the specified name was not found.")

def delete_employee(): #del user from list
    first_name = input("Enter the first name of the employee you want to delete: ")
    last_name = input("Enter the last name of the employee you want to delete: ")
    
    result = collection.delete_one({"First Name": first_name, "Last Name": last_name})
    
    if result.deleted_count > 0:
        print("Employee deleted!")
    else:
        print("Employee with the specified name was not found.")

def list_employees(): #show userlist
    cursor = collection.find()
    if cursor.count() == 0:
        print("No employees are registered.")
    else:
        for employee in cursor:
            print("First Name:", employee["First Name"])
            print("Last Name:", employee["Last Name"])
            print("Job Title:", employee["Job Title"])
            print("Department:", employee["Department"])
            print("ofice:", employee["ofice"])
            print("telefon:", employee["telefon"])
            print("adres:", employee["adres"])
            print()

while True:
    print("\nSelect an action:")
    print("1. Add a new employee")
    print("2. Edit an employee")
    print("3. Delete an employee")
    print("4. List all employees")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ") #comand list 
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        edit_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        list_employees()
    elif choice == "5":
        client.close()
        break
    else:
        print("Invalid choice. Please try again.") 