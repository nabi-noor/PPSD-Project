import sqlite3
class Contact:
    __firstName = ""
    __lastName = ""
    __phoneNumber = 0
    __email = ""
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
  
class ContactBook:
    __listEnd = 0
    __mycontacts = None

    def __init__(self):
        self.__mycontacts=[]
        self.__listEnd=0

    def addcontact(self,first,last,mail,number):
        contact = Contact(first,last,mail,number)
        self.__mycontacts[self.__listEnd]=contact
        

    def display(self,i):
        print("First name: ",self.__mycontacts[i].getfirstname())
        print("Last name: ",self.__mycontacts[i].getlastname())
        print("Email: ",self.__mycontacts[i].getemail())
        print("Phone Number: ",self.__mycontacts[i].getphonenumber())

    def searchByFirstNameContact(self,firstName):
        i=0
        for i in range (0,self.__listEnd):
          if self.__mycontacts[i].getfirstname()==firstName:
            return i
        return -1

    def searchByLastNameContact(self,lastName):
        i=0
        for i in range (0,self.__listEnd):
          if self.__mycontacts[i].getlastname()==lastName:
            return i


    def searchByEmail(self,email):
        i=0
        for i in range (0,self.__listEnd):
            if self.__mycontacts[i].getemail()==email:
                return i
            else:
                return -1 

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Contacts(FirstName TEXT, LastName TEXT, Email TEXT, PhoneNumber REAL)")

def enterData(firstName,lastName,email,phoneNumber):
    c.execute("INSERT INTO Contacts (FirstName, LastName, Email, PhoneNumber) VALUES (?,?,?,?)",(firstName,lastName,email,phoneNumber))
    conn.commit()


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
cursor = c.connection.cursor()
cursor.execute("SELECT * FROM Contacts")

for row in cursor: 
    print("First Name = ", row[0], " Last Name = ", row[1], " Email = ", row[2], " Phone Number = ", row[3])
conn.close()
