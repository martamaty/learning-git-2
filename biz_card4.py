class Biz_Card:
    def __init__(self, name, surname,company, position, mail):
       self.name = name
       self.surname = surname
       self.company = company
       self.position = position
       self.mail = mail

    def __str__(self):
        return f'{self.name} {self.surname} {self.position} {self.mail}'
"""
    def contact(self,name):
        for x in lista:
            if x.name == key:
                return x
"""

"""       
        if self.name == name:
            print(name)
            print(f'{self.name} {self.surname} {self.position} {self.mail}')
"""
        
        #input(surname)
        
            #raise ValueError(f"imie {name} inne niz podane{self.name}")
        

    
    # zadanie 7.2 metoda
    
    
    
     

a = Biz_Card(name="jarek", surname="czaplicki", company="ursus", position="traktorzysta", mail="trak.czap")
b = Biz_Card(name="maniak", surname="benek", company="urzad pracy", position="bezrobotnz", mail="ben.bez")
c = Biz_Card(name="franek", surname="pagowski", company="toi-toi", position="sprzatacz", mail="pag.toi")
d = Biz_Card(name="darek", surname="mruz", company="iglotex", position="lodziarz", mail="mruz.chlod")
e = Biz_Card(name="marek", surname="galaks", company="sex-shop", position="model", mail="gal.sex")

# Cwiczenie 7.2.1 z uzyciem __str__
lista=[a,b,c,d]
key = input("Enter Employee Name: ")

# print(Biz_Card.contact)

for x in lista:
    if  key == x.surname:
        print(x)

""" # Variables
       self.contact = 0

   def accelerate(self, step=name):
       self.current_speed += step

   def decelerate(self, step=10):
       self.current_speed -= step"""

#print(Biz_Card.contact('name',))