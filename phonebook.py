from difflib import get_close_matches


class PhoneBook:
    """Phonebook implementation using Python dictionary as underlying storage"""

    def __init__(self):
        """Creates an empty Phonebook"""
        self.records = {}

    def add(self):
        """Adds a contact with name and phone number in O(1)"""
        contact_name = input("Name: ")

        # checks if the name already exists in the database
        if contact_name in self.records:
            print(f"Contact details of {contact_name} already exist!")
            option = input("Would you like to override it(y/n)? ")
            if option.lower() == 'y' or option.lower() == 'yes':
                phone_number = input("Phone No(eg.0544......): ")

                # overrides the existing phone number
                if len(phone_number.strip()) == 10:
                    self.records[contact_name] = phone_number
                else:
                    print("Invalid phone number!")
            else:
                pass
        else:
            # checks if the name entered is empty or not
            if len(contact_name.strip()) > 0:
                phone_number = input("Phone No(eg.0544......): ")

                # checks that the phone number has 10 digits before storing it
                if len(phone_number) == 10:
                    self.records[contact_name] = phone_number
                    print("Added successfully")
                else:
                    print('Invalid Details entered!')
                    option = input("Would you like to correct it(y/n)? ")
                    if option.lower() == 'y' or option.lower() == 'yes':
                        self.add()
                    else:
                        pass
            else:
                print("Invalid details entered!")
                option = input("Would you like to correct it(y/n)")
                if option.lower() == 'y' or option.lower() == 'yes':
                    self.add()
                else:
                    pass

    def remove(self):
        """Removes contact details of name provided in O(1)"""
        contact_name = input("Name: ")

        # checks for the name in the database and verifies that the user is willing to delete it
        if contact_name in self.records:
            option = input(f"Do you want to delete details of {contact_name} (y/n?)")
            if option == 'y' or option == 'yes':
                del self.records[contact_name]  # removes the details of the name provided
                print("Deleted")
            else:
                pass
        else:
            print("Name not found!!!")

    def search(self):
        """Returns contact details of the name provided in O(1)"""
        contact_name = input("Name: ")

        # checks that the input is not empty and the name exists in the database
        if len(contact_name) > 0:
            if contact_name in self.records:
                print(f"{contact_name} - {self.records[contact_name]}")
            else:
                print(f"Contact details for {contact_name} not found!\n")

                # checks for possible matches to the input
                close_match = get_close_matches(contact_name, self.records.keys())
                if len(close_match) > 0:
                    print("Possible matches")

                    # returns the value of any possible match to the input
                    for i in range(len(close_match)):
                        print(f"{close_match[i]} - {self.records[close_match[i]]}")
        else:
            print("Invalid Details Entered!")
            option = input("Would you like to give it another try(y/n)?")
            if option.lower() == 'y' or option.lower() == 'yes':
                self.search()
            else:
                pass

    def list(self):
        """Returns record of all contacts in  alphabetical order in O(n)"""
        if len(self.records) > 0:
            for key in sorted(self.records):
                print(f"{key} - {self.records[key]}")
        else:
            print("Phonebook is empty!!!")

    def num_of_records(self):
        """Returns the number of contacts in the phonebook in O(1)"""
        if len(self.records) <= 0:
            print("Phonebook is empty")
        elif len(self.records) == 1:
            print("1 contact")
        else:
            print(f"{len(self.records)} contacts")

    def list_by_prefix(self):
        """Returns all contacts starting with the letter entered in O(n)"""
        letter = input("Letter(eg. a): ")

        # loops through the database to check if any stored data has a match with the input pattern
        for key in self.records:
            if key.startswith(f'{letter}'):
                print(f"{key} - {self.records[key]}")
            else:
                print("No match found!")


# main interface
if __name__ == '__main__':

    import sys
    import os

    phone_book = PhoneBook()

    while True:
        os.system("clear")

        choice = input("""
                PHONEBOOK DIRECTORY           
           
                [1] Add contact               
                [2] Search Contact            
                [3] Delete Contact            
                [4] View Contacts by Letter
                [5] View all Contacts	       
                [6] Number of Contacts          
                [7] Exit                      
             """)

        if choice == '1':

            phone_book.add()
            n = input("Press Enter to continue...")

        elif choice == '2':

            phone_book.search()
            n = input("Press Enter to continue...")

        elif choice == '3':

            phone_book.remove()
            n = input("Press Enter to continue...")

        elif choice == '4':

            phone_book.list_by_prefix()
            n = input("Press Enter to continue...")

        elif choice == '5':
            phone_book.list()
            n = input("Press Enter to continue...")

        elif choice == '6':
            phone_book.num_of_records()
            n = input("Press Enter to continue...")

        elif choice == '7':
            sys.exit("Thanks for using our service, Bye!")

        else:
            print("Invalid option!!!")
            n = input("Press Enter to continue...")
