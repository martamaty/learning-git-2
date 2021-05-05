class Biz_Card:
    def __init__(self, name, surname,company, position, mail):
       self.name = name
       self.surname = surname
       self.company = company
       self.position = position
       self.mail = mail

def contact(name):
    print(f"kontaktuje sie z (name,surname): ")
    input()
    self.name=name
        
        

    
    # zadanie 7.2 metoda
    def __str__(self):
        return f'{self.name} {self.surname} {self.position} {self.mail}'

#print(Biz_Card.contact('name',))       

a = Biz_Card(name="jarek", surname="czaplicki", company="ursus", position="traktorzysta", mail="trak.czap")
b = Biz_Card(name="maniak", surname="benek", company="urzad pracy", position="bezrobotnz", mail="ben.bez")
c = Biz_Card(name="franek", surname="pagowski", company="toi-toi", position="sprzatacz", mail="pag.toi")
d = Biz_Card(name="darek", surname="mruz", company="iglotex", position="lodziarz", mail="mruz.chlod")
e = Biz_Card(name="marek", surname="galaks", company="sex-shop", position="model", mail="gal.sex")

# Cwiczenie 7.2.1 z uzyciem __str__
lista=[a,b,c,d]
contact("name")
for x in lista:
    if contact("name") == name:
        print(x)
        



#print(Biz_Card.contact('name',))