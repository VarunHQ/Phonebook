import sys

def initial_phonebook():
    rows, cols = int(input("Enter initial number of contacts: ")), 5


    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (Only):" % (i+1))
        print("Note: * indicates mandatory fields.")
        print("_______________________________________________________________________________________")
        temp = []
    for j in range(cols):
        if j == 0:
            temp.append(input("Enter Name*: "))

            if temp[j] == '' or temp[j] == ' ':
                sys.exit("Name cannot be empty or whitespace. Please enter a valid name.")
        if j == 1:
            temp.append(input("Enter Phone Number*: "))

        if j == 2:
            temp.append(str(input("Enter Email:")))

            if temp[j] == '' or temp[j] == ' ':
                temp[j] = "N/A"
        if j == 3:
            temp.append(str(input("Enter DOB (dd/mm/yyyy):  ")))

            if temp[j] == '' or temp[j] == ' ':
                temp[j] = "N/A"

        if j == 4:
            temp.append(str(input("Enter Category {Family, Friends, Work, Others}: ")))

            if temp[j] == '' or temp[j] == ' ':
                temp[j] = "N/A"

    phone_book.append(temp)

    print(phone_book)
    return phone_book

def menu()
    print("**************************************************************************************************")
    print("\t\t\t Maxrun's Phonebook", flush=False)
    print("**************************************************************************************************") 
    print("You can perform the following operations on this phonebook\n")
    print("--------------------------------------------------------------------------------------------------") 
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a Contact")
    print("5. Display all contacts")
    print("6. Exit Phonebook")

    choice = int(input("Please enter your choice: "))

    return choice 

def add_contact(pb):
    dip[]
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter Name: ")))
        if i == 1:
            dip.append(str(input("Enter Mobile-Number: ")))
        if i == 2:
            dip.append(str(input("Enter Email: ")))
        if i == 3:
            dip.append(str(input("Enter DOB (dd/mm/yyyy): ")))
        if i == 4:
            dip.append(str(input(Enter Category {Family, Friends, Work, Others}: )))

    pb.append(dip)
    
            