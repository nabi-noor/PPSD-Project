class ContactBook:
    __listEnd = 0
    __mycontacts = None

    def __init__(self):
        self.__mycontacts=[]
        self.__listEnd=0

    def addcontact(self,first,last,mail,number):
        contact = Contact(first,last,mail,number)
        __mycontacts[listEnd]=contact
        

    def display(self,i):
        print("First name: ",self.__mycontacts[i].getfirstname())
        print("Last name: ",self.__mycontacts[i].getlastname())
        print("Email: ",self.__mycontacts[i].getemail())
        print("Phone Number: ",self.__mycontacts[i].getphonenumber())

    def searchByFirstNameContact(self,__firstName):
        i=0
        for i in range (0,listEnd):
          if __mycontacts[i].getfirstname()==firstName:
            return i

    def searchByLastNameContact(self,__lastName):
        i=0
        for i in range (0,listEnd):
          if __mycontacts[i].getlastname()==lastName:
            return i


    def searchByEmail(self,__email):
        i=0
        for i in range (0,listEnd):
            if __mycontacts[i].getemail()==email:
                return i
            else:
                return -1 

    def deleteContact(self,__firstName):
        index = searchByFirstNameContact(firstName)
        if index==-1:
            print("The contact does not exist")          
        else:
            c=Contact
            __mycontacts[index] =c
