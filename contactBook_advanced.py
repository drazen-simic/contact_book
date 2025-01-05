import json
import re

def add_contact(contact_book, name, phone, email):
    """Add a new contact to the contact book."""
    if not validate_phone(phone):
        print("You entered invalid format of telephone number.")
        return

    if not validate_email(email):
        print("You entered invalid format of mail adress.")
        return
    
    contact_book[name] = {"phone number":phone, "email":email}
    print("Contact successfully added.")


def validate_phone(phone):
    """Validate phone number format (example: (123) 456-7890)."""
    phone_pattern = ""
    return bool(re.match(phone_pattern, phone))


def validate_email(email):
    """Validate email address format."""
    email_pattern = ""
    return bool(re.match(email_pattern, email))


def search_contact(contact_book, search_term):
    """Search for a contact by name, phone, or email."""
    found = False
    
    for name, details in contact_book.items():
        if search_term in name or search_term in details["phone number"] or search_term in details["email"]:
            print(f"{name}")
            print(f"phone number: {details["phone number"]}")
            print(f"mail: {details["email"]}")
            found = True

    if not found:
        print(f"Contact for {search_term} is not founded!")


def delete_contact(contact_book, name):
    """Delete a contact by name."""
    if name in contact_book:
        del contact_book[name]
        print (f"Contact {name} is erased!")
    
    else:
        print("Name is not found!")


def display_contacts(contact_book):
    """Display all contacts sorted by name."""
    if not contact_book:
        print("Contact book is empty!")
        return
    
    else:
        for name, info in sorted(contact_book.items()):
            print(f"{name}")
            print(f"phone: {info["phone number"]}")
            print(f"mail: {info["email"]}")


def edit_contact(contact_book, name, phone=None, email=None):
    """Edit the phone or email of an existing contact."""
    if name in contact_book:
        if phone:
            if not validate_phone(phone):
                print("Number is not valid!")
                return
            else:
                contact_book[name]["phone number"] = phone

        if email:
            if not validate_email(email):
                print("Email is not valid!")
                return
        else:
            contact_book[name]["email"] = email


def save_contacts(contact_book, filename="contacts.json"):
    """Save the contact book to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(contact_book, file)
        print(f"Contacts saved to {filename}.")


def load_contacts(filename="contacts.json"):
    """Load the contact book from a JSON file."""
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved contacts found, starting a new contact book.")
        return {}


def main():
    """Main program loop to interact with the user."""
    contact_book = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display all Contacts")
        print("5. Edit Contact")
        print("6. Save Contacts")
        print("7. Exit")
        
        choice = input("Choose an option: ").strip()

        if choice == "1":
            
            name = input("Enter name: ").strip().title()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email adress: ").strip()

            add_contact(contact_book=contact_book, name=name, phone=phone, email=email)

            print(contact_book)

        elif choice == "2":
            
            search_term = input("Enter search term!")
            search_contact(contact_book, search_term)

        elif choice == "3":
            name = input("Enter the name of the contact you want to delete: ")
            delete_contact(contact_book, name)
        
        elif choice == "4":
            display_contacts(contact_book)
        
        elif choice == "5":
            name = input("Enter name for editing: ").strip().title()
            phone = input("Enter a new phone number: ").strip()
            email = input("Enter a new email adress: ").strip()
            edit_contact(contact_book, name, phone, email)
        
        elif choice == "6":
            save_contacts(contact_book)
        
        elif choice == "7":
            print("You are exiting from Contact Book!")
            break
        
        else:
            pass


if __name__ == "__main__":
    main()
