import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="kalk_2.log")
print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

i=int(input())
i != int
while True:
    i != int(input())
    print ("podaj cyfre")
    if i == int:
        print

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

i=int(input())
i != int
while True:
    i != int(input())
    print ("podaj cyfre")
    if i == int:
        print("Podaj pierwsza liczbe: ")

a=int(input())

print("Podaj druga liczbe: ")
b=int(input())


typ=None
if i == 1:
    typ="Dodawanie"
    r=a+b
    
if i == 2:
    typ="Odejmowanie"
    r=a-b
    
if i == 3:
    typ="Mnozenie"
    r=a*b

if i == 4:
    typ="Dzielenie"
    r=0
    if b == 0:
        print("Błąd: nie można dzielić przez 0")
    r=a/b

logging.info("Wybrana liczba 1 to: %s" %a)
logging.info("Wybrana liczba 2 to: %s" %b)
logging.info("%s" %typ)
logging.info("Wynik działania to: %s" %r)

print("Wybrana liczba 1 to: %s" %a)
print("Wybrana liczba 2 to: %s" %b)
print("%s" %typ, "liczb", "%s" %a,"i", "%s" %b)
print("Wynik to: %s" %r)
print("hello")
print("hello3")