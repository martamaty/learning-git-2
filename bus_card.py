"""
name_list=["janek czaplicki ursus traktorzysta czap.trak",
"maniek benek urzad pracy bezrobotny ben.bez",
"franek pagowski toi-toi sprzatacz pag.toi",
"darek mruz iglotex chlodziarz mruz.chlod",
"marek galaks sex-shop model gal.sex"]
"""

class Biz_Card:
    def __init__(self, name, surname,company, position, mail):
       self.name = name
       self.surname = surname
       self.company = company
       self.position = position
       self.mail = mail
       
# mozliwosc 1

a = Biz_Card(name="Jarek", surname="Czaplicki", company="ursus", position="traktorzysta", mail="czap.trak")
b = Biz_Card(name="maniak", surname="benek", company="urzad pracy", position="bezrobotnz", mail="ben.bez")
c = Biz_Card(name="franek", surname="pagowski", company="toi-toi", position="sprzatacz", mail="pag.toi")
d = Biz_Card(name="darek", surname="mruz", company="iglotex", position="lodziarz", mail="mruz.chlod")
e = Biz_Card(name="marek", surname="galaks", company="sex-shop", position="model", mail="gal.sex")

lista=[a,b,c,d]

for x in lista:
    print(x.name,x.position,x.mail)

# mozliwosc 2 niedziala bo  print(x.name,x.surname,x.mail) AttributeError: 'NoneType' object has no attribute 'name'
"""
jarek = Biz_Card(name="Jarek", surname="Czaplicki", company="ursus", position="traktorzysta", mail="czap.trak")
maniak = Biz_Card(name="maniak", surname="benek", company="urzad pracy", position="bezrobotnz", mail="ben.bez")
franek = Biz_Card(name="franek", surname="pagowski", company="toi-toi", position="sprzatacz", mail="pag.toi")
darek = Biz_Card(name="darek", surname="mruz", company="iglotex", position="lodziarz", mail="mruz.chlod")
marek = Biz_Card(name="marek", surname="galaks", company="sex-shop", position="model", mail="gal.sex")

names=[
"jarek",
"maniak",
"franek",
"darek",
"marek"]

x=None
for word in names:
    x == word
    print(x.name,x.surname,x.mail)
"""

"""
name_list=[
"janek czaplicki ursus traktorzysta czap.trak",
"maniek benek urzad pracy bezrobotny ben.bez",
"franek pagowski toi-toi sprzatacz pag.toi",
"darek mruz iglotex lodziarz mruz.chlod",
"marek galaks sex-shop model gal.sex"]
print(name_list[3])
"""

"""
names=[
"jarek",
"maniak",
"franek",
"darek",
"marek"]

contact=None
for word in names:
    word += word + '\n'
"""

"""
print(jarek)
print(jarek.name,jarek.surname,jarek.mail)
"""