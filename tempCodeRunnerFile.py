contacts = []
name1 = input("Enter name: ")
phone1 = input("Enter phone number: ")
contacts.append([name1, phone1])
print("\n--- Contact List ---")
for contact in contacts:
    print(f"Name: {contact[0]}, Phone: {contact[1]}")
search_name = input("\nEnter name to search: ")
found = False
for contact in contacts:
    if contact[0].lower() == search_name.lower():
        print(f"Number found: {contact[1]}")
        found = True
        break
if not found:
    print("Contact not found.")
delete_name = input("\nEnter name to delete: ")
for contact in contacts:
    if contact[0].lower() == delete_name.lower():
        contacts.remove(contact)
        print("Contact deleted successfully.")
        break
contacts.sort(key=lambda x: x[0])
print("\nSorted Contacts:", contacts)
pakistani_numbers = [c for c in contacts if c[1].startswith('03')]
print("\nNumbers starting with '03':", pakistani_numbers)