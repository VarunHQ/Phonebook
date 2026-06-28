# importing the module
import sys

# this function will be the first to run as soon as the main function executes
def initial_slambook():
    rows, cols = int(input("Please enter number of yours: ")), 5

    # We are collecting the initial number of contacts the user wants to have in the
    # phonebook already. User may also enter 0 if he doesn't wish to enter any.
    slam_book = []
    print(slam_book)

    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY): " % (i+1))
        print("NOTE: * indicates mandatory fields")
        print ("………………………………………………………………………………")

        temp = []
        for j in range(cols):
            # We have taken the conditions for values of j only for the personalized fields
            # such as name, number, e-mail id, dob, category etc
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                # We need to check if the user has left the name empty
                # name & number are mandatory fields.
                # So implement a condition to check as below.
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit(
                        "Name is a mandatory field. Process exiting due to blank field..."
                    )
                # This will exit the process if a blank field is encountered.

            if j == 1:
                temp.append(int(input("Enter number*: ")))
                # We do not need to check if user has entered the number because int automatically
                # takes care of it. Int value cannot accept a blank as that counts as a string.
                # So process automatically exits without us using the sys package.

            if j == 2:
                temp.append(str(input("Enter something about your friend: ")))
                # Even if this field is left as blank, None will take the blank's place
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                # Whatever format the user enters dob in, it won't make
                if temp[j] == '' or temp[j] == ' ':
                    # Even if this field is left as blank, None will take the blank's place
                    temp[j] = None

            if j == 4:
                temp.append(
                    str(input("Enter category(Family/Friends/Work/Others): "))
                )
                # Even if this field is left as blank, None will take the blank's place

                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

        slam_book.append(temp)
        # By this step we are appending a list temp into a list phone_book
        # That means phone_book is a 2-D array and temp is a 1-D array

    print(slam_book)
    return slam_book

def menu():
    # We created this simple menu function for
    # code reusability & also for an interactive console
    # Menu func will only execute when called
    print("**********************************************************************")
    print("                         SLAMBOOK MENU")
    print("**********************************************************************")
    print("1. Display all contacts")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Exit")
    print("**********************************************************************")
    choice = int(input("Enter your choice (1-5): "))
    return choice

def display_all_contacts(slam_book):
    """Display all contacts in the slambook"""
    if not slam_book:
        print("No contacts in the slambook!")
        return
    
    print("\n" + "=" * 80)
    print("                         ALL CONTACTS")
    print("=" * 80)
    for index, contact in enumerate(slam_book, 1):
        print(f"\nContact {index}:")
        print(f"  Name:     {contact[0]}")
        print(f"  Number:   {contact[1]}")
        print(f"  About:    {contact[2]}")
        print(f"  DOB:      {contact[3]}")
        print(f"  Category: {contact[4]}")
    print("=" * 80 + "\n")

def search_contact(slam_book):
    """Search for a contact by name"""
    if not slam_book:
        print("No contacts in the slambook!")
        return
    
    search_name = input("Enter the name to search: ").lower()
    found = False
    
    for index, contact in enumerate(slam_book, 1):
        if contact[0].lower() == search_name:
            print(f"\nContact Found!")
            print(f"  Name:     {contact[0]}")
            print(f"  Number:   {contact[1]}")
            print(f"  About:    {contact[2]}")
            print(f"  DOB:      {contact[3]}")
            print(f"  Category: {contact[4]}")
            found = True
            break
    
    if not found:
        print(f"Contact '{search_name}' not found!")

def update_contact(slam_book):
    """Update a contact's information"""
    if not slam_book:
        print("No contacts in the slambook!")
        return
    
    name = input("Enter the name of contact to update: ").lower()
    
    for contact in slam_book:
        if contact[0].lower() == name:
            print("\nWhat would you like to update?")
            print("1. Number")
            print("2. About")
            print("3. DOB")
            print("4. Category")
            update_choice = int(input("Enter your choice (1-4): "))
            
            if update_choice == 1:
                contact[1] = int(input("Enter new number: "))
            elif update_choice == 2:
                contact[2] = input("Enter new about: ")
            elif update_choice == 3:
                contact[3] = input("Enter new DOB (dd/mm/yy): ")
            elif update_choice == 4:
                contact[4] = input("Enter new category: ")
            
            print("Contact updated successfully!")
            return
    
    print(f"Contact '{name}' not found!")

def delete_contact(slam_book):
    """Delete a contact from the slambook"""
    if not slam_book:
        print("No contacts in the slambook!")
        return
    
    name = input("Enter the name of contact to delete: ").lower()
    
    for i, contact in enumerate(slam_book):
        if contact[0].lower() == name:
            slam_book.pop(i)
            print(f"Contact '{name}' deleted successfully!")
            return
    
    print(f"Contact '{name}' not found!")

def main():
    """Main function to run the slambook application"""
    print("\n" + "=" * 80)
    print("                    WELCOME TO SLAMBOOK")
    print("=" * 80)
    
    slam_book = initial_slambook()
    
    while True:
        choice = menu()
        
        if choice == 1:
            display_all_contacts(slam_book)
        elif choice == 2:
            search_contact(slam_book)
        elif choice == 3:
            update_contact(slam_book)
        elif choice == 4:
            delete_contact(slam_book)
        elif choice == 5:
            print("\nThank you for using Slambook! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the main function
if __name__ == "__main__":
    main()