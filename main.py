# ANUPAM KUMAR VERMA MCA Ist year(CODSOFT INTERNSHIP)
class Contact:
    def __init__(me, name, phone, email):
        me.name = name
        me.phone = phone
        me.email = email

class ContactBook:
    def __init__(me):
        me.contacts = []

    def add_contact(me, contact):
        me.contacts.append(contact)

    def view_contacts(me):
        for contact in me.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(me, search_term):
        results = []
        for contact in me.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                results.append(contact)
        return results

    def update_contact(me, old_name, new_contact):
        for i, contact in enumerate(me.contacts):
            if contact.name == old_name:
                me.contacts[i] = new_contact

    def delete_contact(me, name):
        for i, contact in enumerate(me.contacts):
            if contact.name == name:
                del me.contacts[i]

def main():
    contact_book = ContactBook()

    while True:
        print("\nPython Contact Book :")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your own choice for this: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Mobile number: ")
            email = input("Enter Email: ")
            new_contact = Contact(name, phone, email)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_term)
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            new_contact = Contact(name, phone, email)
            contact_book.update_contact(old_name, new_contact)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            break

if __name__ == '__main__':
    main()