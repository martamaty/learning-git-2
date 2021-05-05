print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
text=int(input())


print("Podaj pierwsza liczbe: ")
a=int(input())


print("Podaj druga liczbe: ")
b=int(input())


if text == 1:
    r=a+b
    print("Dodaje", a , "i", b)
    print("Wynik to", r)

if text == 2:
    r=a-b
    print("Odejmuje", a , "i", b)
    print("Wynik to", r)

if text == 3:
    r=a*b
    print("Mnoze", a , "i", b)
    print("Wynik to", r)

if text == 4:
    r=a/b
    print("Dziele", a , "i", b)
    print("Wynik to", r)