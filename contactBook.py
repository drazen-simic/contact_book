def add_contact(contact_book, name, phone, email):
    """Add a new contact to the contact book."""
    contact_book[name] = {'phone': phone, 'email': email}
    print(f"Contact for {name} added successfully!")

def search_contact(contact_book, name):
    """Search for a contact by name."""
    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"Contact for {name} not found.")

def delete_contact(contact_book, name):
    """Delete a contact by name."""
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"Contact for {name} not found.")

def display_contacts(contact_book):
    """Display all contacts."""
    if not contact_book:
        print("No contacts available.")
        return
    for name, info in contact_book.items():
        print(f"\n{name}:")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")

def main():
    """Main program loop to interact with the user."""
    contact_book = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            add_contact(contact_book, name, phone, email)
        elif choice == "2":
            name = input("Enter contact name to search: ").strip()
            search_contact(contact_book, name)
        elif choice == "3":
            name = input("Enter contact name to delete: ").strip()
            delete_contact(contact_book, name)
        elif choice == "4":
            display_contacts(contact_book)
        elif choice == "5":
            print("Exiting the contact book program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
