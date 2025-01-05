# contact_book
Python code for contact book

Task Description: Contact Book Application
Overview
In this task, you will build a Contact Book Application that allows users to manage their personal contacts. The application will store contact details such as name, phone number, and email, and provide options to add, search, edit, delete, and display contacts. The program will also allow the user to save and load their contacts from a file, ensuring that data is persistent between sessions.

Task Requirements
Basic Functionality
    1. Add a Contact:
        ◦ The user should be able to add a new contact by providing the name, phone number, and email.
        ◦ The program should validate the phone number (must be in a specific format, e.g., (123) 456-7890) and email (must be a valid email address format).
    2. Search for a Contact:
        ◦ The user should be able to search for a contact by name, phone number, or email.
        ◦ If the contact is found, display the contact's details (name, phone, email).
        ◦ If no contact is found, display a message indicating that no match was found.
    3. Delete a Contact:
        ◦ The user should be able to delete a contact by providing the contact's name.
        ◦ If the contact exists, it should be removed from the contact book.
    4. Display All Contacts:
        ◦ The program should display a list of all contacts stored in the contact book, sorted by name.
        ◦ If there are no contacts, the program should inform the user.
    5. Edit a Contact:
        ◦ The user should be able to update a contact’s phone number or email.
        ◦ Only the specified fields should be updated, and the program should validate the new information.

Advanced Features (Optional)
    1. Save Contacts to a File:
        ◦ The user should be able to save all contacts to a file (e.g., JSON format) so that the contact book persists between program runs.
        ◦ When the program starts, it should automatically load the saved contacts from the file.
    2. Input Validation:
        ◦ Ensure that the phone number and email follow the correct formats before adding or editing a contact.
        ◦ Provide user-friendly error messages if the input is invalid.
    3. Sort Contacts:
        ◦ Display the contacts in alphabetical order by name, phone number, or email.
    4. Search by Phone Number or Email:
        ◦ Extend the search functionality to allow users to search by phone number or email address.
    5. Backup Feature:
        ◦ Allow the user to create a backup of their contact list to another file.
    6. User Interface:
        ◦ The program should be easy to use, with a simple text-based menu that allows the user to select an option.
        ◦ Provide clear instructions and feedback throughout the process.

Example User Story
    1. The user starts the program and sees a menu of options.
    2. They choose to add a contact, entering a name, phone number, and email.
    3. They then choose to display all contacts, and the program shows the list of contacts sorted by name.
    4. They search for a contact by name or phone number and see the contact details.
    5. They edit a contact, changing the phone number or email, and the program validates the new information.
    6. The user can delete a contact by providing its name.
    7. They can save the contact list to a file, ensuring that the contacts will persist when the program is restarted.

Skills Practiced
    • Dictionaries: Storing and accessing contact details using key-value pairs.
    • Lists: Managing a collection of contacts and sorting them.
    • Tuples: Understanding when to use immutable data.
    • Input Validation: Ensuring that user inputs are in the correct format.
    • File I/O: Saving and loading data to and from files.
    • Modular Programming: Organizing the code into separate, reusable functions.

