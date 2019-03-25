from Person import Person


def print_contacts(contact_list):
    for contact in contact_list:
        print("Name: " + contact.name)
        print("Address: " + contact.address)
        print("Birthday: " + contact.birthday)
        print("Phone number: " + contact.phone_number)
        print("Email: " + contact.email)
        print("Proffesion: " + contact.proffesion)
        print("Interests: " + contact.interests)
        print()


def add_contact():
    print("Enter the details of the contact ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    birthday = input("Enter birthday: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    proffesion = input("Enter proffesion: ")
    interests = input("Enter interests: ")

    person = Person(name)
    person.address = address
    person.birthday = birthday
    person.phone_number = phone_number
    person.email = email
    person.proffesion = proffesion
    person.interests = interests

    return person

def find_contact_by_name(contact_list, contact_name):
    for contact in contact_list:
        if contact.name == contact_name:
            return contact

        return False

def update_file(contact_list):
    file_writer = open(CONTACT_BOOK_FILE_PATH, "w")
    for contact in contact_list:
        file_writer.write(contact.name + "," + contact.address + "," + contact.birthday + "," +
                          contact.phone_number + "," + contact.email + "," + contact.proffesion + "," + contact.interests + "\n")



CONTACT_BOOK_FILE_PATH = "contact_book"

person = Person("dsa")

text_file = open(CONTACT_BOOK_FILE_PATH, "r")

contact_list = []

for line in text_file:
    person_info = line.strip().split(",")

    person = Person(person_info[0])
    person.address = person_info[1]
    person.birthday = person_info[2]
    person.phone_number = person_info[3]
    person.email = person_info[4]
    person.proffesion = person_info[5]
    person.interests = person_info[6]

    contact_list.append(person)

text_file.close()

print("This is a personal contact book.")
print("You can perform actions by typing the number associated with them.")

choice = ""

while (choice != "5"):
    print()
    print("1.Show records in book")
    print("2.Add record in book")
    print("3.Remove record from book")
    print("4.Update record in book")
    print("5.Exit")

    choice = input()

    if choice == "1":
        print_contacts(contact_list)

    elif choice == "2":
        contact_list.append(add_contact())
        update_file(contact_list)

    elif choice == "3":
        contact_name = input("Enter the name of the contact you want to remove ")
        if find_contact_by_name(contact_list, contact_name) == False:
            print("Can't find contact with this name")
        else:
            contact_list.remove(find_contact_by_name(contact_list, contact_name))
            update_file(contact_list)

    elif choice == "4":
        contact_name = input("Enter the name of the contact you want to modify ")
        if find_contact_by_name(contact_list, contact_name) == False:
            print("Can't find contact with this name")
        else:
            print("Enter what you want to modify")
            print("1.Name")
            print("2.Address")
            print("3.Birthday")
            print("4.Phone number")
            print("5.Email")
            print("6.Proffesion")
            print("7.Interests")

            choice = input()

            if choice == "1":
                print("Enter the new name of the contact")
                new_name = input()
                find_contact_by_name(contact_list, contact_name).name = new_name

            elif choice == "2":
                print("Enter the new address of the contact")
                new_address = input()
                find_contact_by_name(contact_list, contact_name).address = new_address

            elif choice == "3":
                print("Enter the new birthday of the contact")
                new_birthday = input()
                find_contact_by_name(contact_list, contact_name).birthday = new_birthday

            elif choice == "4":
                print("Enter the new phone number of the contact")
                new_phone_number = input()
                find_contact_by_name(contact_list, contact_name).phone_number = new_phone_number

            elif choice == "5":
                print("Enter the new email of the contact")
                new_email = input()
                find_contact_by_name(contact_list, contact_name).email = new_email

            elif choice == "6":
                print("Enter the new proffesion of the contact")
                new_proffesion = input()
                find_contact_by_name(contact_list, contact_name).proffesion = new_proffesion

            elif choice == "7":
                print("Enter the new interests of the contact")
                new_interests = input()
                find_contact_by_name(contact_list, contact_name).interests = new_interests

            update_file(contact_list)

    elif choice == "5":
        break
