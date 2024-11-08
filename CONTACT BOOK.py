# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    print("Adding a new contact:")
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")

    # Store the contact in the dictionary
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("List of contacts:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("------------------------")

# Function to search for a contact
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, contact_info in contacts.items():
        if search_term in [name, contact_info['phone']]:
            print(f"Name: {name}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("------------------------")
            found = True
    if not found:
        print("No matching contacts found.")

# Function to update an existing contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact '{name}':")
        phone = input("Enter new phone number (press enter to leave unchanged): ")
        email = input("Enter new email address (press enter to leave unchanged): ")
        address = input("Enter new address (press enter to leave unchanged): ")

        # Update contact details if new data is provided
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address

        print(f"Contact '{name}' updated successfully!\n")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print(f"Contact '{name}' not found.")

# Main program loop
while True:
    print("\n*** Contact Book Menu ***")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
