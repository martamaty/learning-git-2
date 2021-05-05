def shopping(items, payment='card', shop='local shop'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

if __name__ == "__main__":
    items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
    items = items_text.split(',')
    payment_method=input("Placisz card lub cash")
    shop=input("sklep lokalny,supermarket: ")
    shopping_result = shopping(items,payment_method,shop)
    print(shopping_result)