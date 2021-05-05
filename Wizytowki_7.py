#Wizytowki_7.3_dziedziczenie

#BaseContact

class BaseContact:
    def __init__(self, name, surname, mail, phone):
       self.name = name
       self.surname = surname
       self.phone = phone
       self.mail = mail

class BusinessContact(BaseContact):
    def __init__(self, position,company,company_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company = company
       self.company_phone = company_phone

    def __str__(self):
        return f'{self.position} {self.company} {self.company_phone}'

#p1 = BusinessContact(name="Jarek", surname="Czaplicki", company="ursus", position="traktorzysta", mail="czap.trak",phone="683452321", company_phone="431824967")
#print(p1.name)
#print(p1.phone)
    



#print("do kogo chcesz zadzwonić?" ) 
#print("podaj imie z duzej litery")
#y = int(input())

Jarek = BusinessContact(name="Jarek", surname="Czaplicki", company="ursus", position="traktorzysta", mail="czap.trak",phone="683452321", company_phone="431824967")
y = int(input("podaj imie z duzej litery"))
if y == (Jarek):
    print(Jarek)
#print(x.surname)

#swapcase()	Odwraca rodzaj każdej litery – małe na duże, duże na małe

"""print("podać numer służbowy, czy numer prywatny?")
x=input()
if x == 1:
    print(jarek.phone)
"""    
"""
if x = numer służbowy:
    print (company_phone)
else:
    print(phone)"""


a = BaseContact(name="Jarek", surname="Czaplicki", mail="czap.trak",phone="683452321")
b = BaseContact(name="maniak", surname="benek", mail="ben.bez", phone="995561254")
c = BaseContact(name="franek", surname="pagowski", mail="pag.toi", phone="321468753")
d = BaseContact(name="darek", surname="mruz", mail="mruz.chlod",phone="856427154")
e = BaseContact(name="marek", surname="galaks", mail="gal.sex", phone="951852456")

Jarek = BusinessContact(name="Jarek", surname="Czaplicki", company="ursus", position="traktorzysta", mail="czap.trak",phone="683452321", company_phone="431824967")
Maniek = BusinessContact(name="Maniak", surname="benek", company="urzad pracy", position="bezrobotnz", mail="ben.bez", phone="995561254", company_phone="167943258")
Franek = BusinessContact(name="Banek", surname="pagowski", company="toi-toi", position="sprzatacz", mail="pag.toi", phone="321468753", company_phone="741258963")
Darek= BusinessContact(name="Darek", surname="mruz", company="iglotex", position="lodziarz", mail="mruz.chlod",phone="856427154", company_phone="753159852")
Marek = BusinessContact(name="Marek", surname="galaks", company="sex-shop", position="model", mail="gal.sex", phone="951852456", company_phone="213645978")





"""lista=[a,b,c,d,e]
liste=[aa,bb,cc,dd,ee]

for x in lista:
    print("Dane podstawowe") 
    print(x.name,x.surname,x.phone,x.mail)
    
for y in liste:
    print("Dane firmowe") 
    print(y.name,y.surname,y.position,y.company, y.company_phone)

#BusinessContact       
#a = BusinessContac(position="Mercedes", company="Actros", company_phone="black")
#ruck.company_phone
#print(a)"""




