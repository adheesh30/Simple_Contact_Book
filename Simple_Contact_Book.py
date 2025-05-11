
contacts= {}     # empty dictionary to store contacts

while True:         # this code runs the menu again and again until user choose exit
    print("\nContact Book Menu: ")
    print("1. Add Contact") 
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")    # Choice is a variable, not function.

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact Added Successfully!")

    elif choice == "2":
        print("\nAll Contacts:")
        for name, number in contacts.items():   # 'for' loop will print the items from the dictionary in the order they were added.
            print(f"{name} : {number}")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}'s number is {contacts[name]}")  # {contacts[name]} gives the phone number from the dictionary.
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            contacts.pop(name)
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        name = input("Enter name to update: ")
        if name in contacts:
            new_number = input("Enter new phone number: ")
            contacts[name] = new_number   # Save the new number for the person named in the contact dictionary.
            print("Contact Updated Successfully!")
        else: 
            print("Contact Not Found!")

    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid Choice! Please enter 1-6.")
