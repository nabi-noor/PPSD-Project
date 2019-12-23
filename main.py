class Contact:
    1

    def getfirstname(self):
        return self.__firstName

    def getlastname(self):
        return self.__lastName

    def getemail(self):
        return self.__email

    def getphonenumber(self):
        return self.__phonenumber      

    def __init__(self,first,last,mail,num):
        self.__firstName=first
        self.__lastName=last
        self.__email=mail
        self.__phonenumber=num 

    def setfirstname(self,first):
        self.__firstName=first

    def setlastname(self,last):
        self.__lastName=last

    def setEmail(self,mail):
        self.__email=mail

    def setphonenumber(self,num):
        self.__phonenumber=num

    def display(self):
        print("First Name = ", self.__firstName)
        print("Last Name = ", self.__lastName)
        print("Email = ", self.__email)
        print("Phone Number = ", self.__phonenumber)    
  
class ContactBook:
    __listEnd = 0
    __mycontacts = None

    def __init__(self):
        self.__mycontacts=[]
        self.__listEnd=0

    def addcontact(self,first,last,mail,number):
        contact = Contact(first,last,mail,number)
        self.__mycontacts.append(contact)
        

    def display(self):
        for i in self.__mycontacts:
            i.display()

    def searchByFirstNameContact(self,firstName):
        for i in self.__mycontacts:
          if i.getfirstname()==firstName:
            return i
        return -1

    def searchByLastNameContact(self,lastName):
        for i in self.__mycontacts:
          if i.getlastname()==lastName:
            return i
        return -1


    def searchByEmail(self,email):
        for i in self.__mycontacts:
            if i.getemail()==email:
                return i
        return -1 

    def modifyEmail(self,contact,email):
        contact.setEmail(email)

    def modifyFirstName(self,contact,firstname):
        contact.setFirstName(firstname)
    
    def modifyLastName(self,contact,lastname):
        contact.setlastname(lastname)

    def modifyPhoneNumber(self,contact,phone):
        contact.setphonenumber(phone)
    
if __name__ == "__main__":
    file = open("Contacts.txt","w")
    contactBook = ContactBook()
    choice = 1
    while choice == 1:
        print("Enter 1 to add a contact\n")
        print("Enter 2 to print contacts\n")
        print("Enter 3 to search contact\n")
        print("Enter 4 to modify first name of contact\n")
        print("Enter 5 to modify last name of contact\n")
        print("Enter 6 to modify email of contact\n")
        print("Enter 7 to modify contact\n")
        choice = int(input("Please enter your choice"))
        if choice == 1:
            firstName = input("Enter your first name")
            lastName = input("Enter your last name")
            email = input("Enter your email")
            phoneNumber = int(input("Enter your phone number without '0'"))
            contactBook.addcontact(firstName,lastName,email,phoneNumber)
        elif choice == 2:
            contactBook.display()
        elif choice == 3:
            print("To search using first name enter 1")
            print("To search using last name enter 2")
            print("To search using email enter 3")
            choice = int(input("Please enter your choice"))
            if choice == 1:
                firstName = input("Please enter contact's first name")
                i = contactBook.searchByFirstNameContact(firstName)
                if i == -1:
                     print("Contact does not exist")
            else:
                i.display()
        elif choice == 2:
            lastName = input("Enter contact's last name")
            i = contactBook.searchByLastNameContact(lastName)
            if i == -1:
                print("Contact does not exist")
            else:
                i.display()
        elif choice == 3:
            email = input("Enter the email of contact")
            i = contactBook.searchByEmail(email)
            if i == -1:
                print("Contact does not exist")
            else:
                i.display()
        elif choice == 4:
            firstName = input("Please enter contact's first name")
            i = contactBook.searchByFirstNameContact(firstName)
            if i == -1:
                print("Contact does not exist")
            else:
                contactBook.modifyFirstName(i,firstName)
        elif choice == 5:
            lastName = input("Enter contact's last name")
            i = contactBook.searchByLastNameContact(lastName)
            if i == -1:
                print("Contact does not exist")
            else:
                contactBook.modifyLastName(i,lastname)
        elif choice == 6:
            email = input("Enter the email of contact")
            i = contactBook.searchByEmail(email)
            if i == -1:
                print("Contact does not exist")
            else:
                contactBook.modifyEmail(i,email)
        elif choice == 7:
            firstname = input("Enter the First Name")
            i = contactBook.searchByFirstNameContact(firstname)
            if i == -1:
                print("Contact does not exist")
            else:
                phone = int(input("Please enter your phone number wwithout 0"))
                contactBook.modifyEmail(i,phone)
            
        else:
            print("Please enter a valid choice")        
        choice = int(input("If you want to continue using the progarm then enter 1 else enter 0"))