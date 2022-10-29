
# initiation a new instance of a phone book
PhonebookApp = PhoneBook()
while 1:
    mainMenuInput = input('''
Hello there!
Welcome to your phonebook
what would you like to do?
[1] Create a new contact.
[2] Search for a contact.
[3] Get all contact. 
[4] Close application. \n
    ''')

    if str(mainMenuInput).strip() == '1':
        name = input(     '''
Please enter name of contact:
        ''')
        number = int(input(   '''
Please enter mobile number:
            '''))
        contacts = PhonebookApp.displayContacts()
        print("Successfully added! \n" + contacts) if PhonebookApp.addContact(name, number) else None
    elif str(mainMenuInput).strip() == '2':
        name = str(input(   '''
Please enter name of contact:
            '''))
        response = PhonebookApp.searchContact(name)
        print(response) if response else print(f"\tSorry {name.capitalize()} cannot be found.")
    elif str(mainMenuInput).strip() == '3':
        contacts = PhonebookApp.displayContacts()
        print(contacts)
    elif str(mainMenuInput).strip() == '4':
        sys.exit()