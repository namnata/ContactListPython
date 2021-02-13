class Person:


    def __init__(self, firstName, lastName, phoneNumber, email):

        # Instance variables
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email



        @classmethod
        def save_contact(self):
           Person.contactList.append(self)

        @classmethod
        def remove_contact(self):
            Person.contactList.remove(self)

        @classmethod
        def find_by_number(cls, number):
            for person in cls.contactList:
                if person.phoneNumber == number:
                    return person

        @classmethod
        def display_contacts(cls):
            return cls.contactList

        @classmethod
        def add(cls, name, surname, number, email):
            return cls(name, surname, number, email)

        def __getitem__(self, key):
            return getattr(self, key)

        def __setitem__(self, key, value):
            setattr(self, key, value)

        def __str__(self):
            return (str(self.firstName) + ":" + str(self.lastName))


    def add_contact(person):

        person.save_contact()

    def delete_contact(person):

        person.remove_contact()

    def find_contact(cls, firstName):
        for person in contactList:
            if person.firstName == firstName:

                return person



    # Print function for display method like in C#
    def print_people(self):

        print("First Name: " + self.firstName())
        print("Last Name: " + self.lastName)
        print("Phone Number: " + self.phoneNumber)
        print("Email: " + self.email)
        print("-------------------")



contactList = [] #list of contacts
msg_error = '{}Invalid option. Please use numeric options{}'.format('\033[31m', '\033[m')  # Red text
menu_options = input('Press any key to continue - ')

# I used while loop because there is no switch case in Python
while True:
    print("======Natalia's Contact List======")
    print('Choose from the following options (0 - 5):')
    print("""             [ 1 ] Add
             [ 2 ] Update
             [ 3 ] Remove
             [ 4 ] Find 
             [ 5 ] Display
             [ 0 ] Finish""")

    # This if and elif blocks check if user input ranges from 0-5

    option = input('')
    if not option.isnumeric():
        print(msg_error)
        continue
    elif option not in '012345':
        print(msg_error)
        continue

        # Convert a value into a integer

    else:
        option = int(option)
        if option == 0:
            print('>>>Program ended\n')
            break


            # Add a new contact
        elif option == 1:

            firstName = input('First name: ').capitalize().strip
            lastName = input('Last Name: ').capitalize().strip()
            phoneNumber = input('Phone number: ').strip()
            email = input('Email: ').strip().lower()

            person = Person(firstName, lastName, phoneNumber, email)
            contactList.append(person)
            print('The new person is added to your contact list\n')

        # Update contact information =============== not finished==============

        elif option == 2:
            nameSearch = input('Enter existing contact name : ').capitalize().strip
            if not contactList:
                print()
                continue

        # Remove contact method doesn't work =============== The same problem I wanted to use
        # FirstOrDefault function but couldn't implement it properly
        elif option == 3:

            search_name = input('Enter the first name of the contact you want to remove from the contact list: ')

            #p = next(c for c in contactList if c.firstName == search_name), None)

            if not contactList:
                input("Your contact list is empty. Press Enter to continue...\n")


            for person in contactList:
                if person.firstName == search_name:
                    contactList.remove(person)



        # Find contact method doesn't work. I've tried to implement logic like in C# ==============
        # I wanted to use FirstOrDefault function like in C# but didn't have time to implement it properly


        elif option == 4:

            search_name = input('Enter the name of the contact you want to display: ')

            #p = next(c for c in contactList if c.firstName == search_name), None)

            if not contactList:
                input("Contact is not found. Press Enter to continue...\n")

            else:
                print(p)


        # Display all contacts =============== it works

        elif option == 5:


            if not contactList:
                input("Your contact list is empty. Press Enter to continue...\n")


            else:
                print("Here are the current people in your contact list:")
            for obj in contactList:
                obj.print_people()

