shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor"
]
forgotten_items = [
    "chusteczki",
    "papier toaletowy"
]

def shopping(items):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart

def x_shopping(items):
    x_cart = "Jesce dokupic: "
    for item in items:
        x_cart += item +'\n'
    return x_cart

basket = shopping(shopping_items)
x_basket = x_shopping(forgotten_items)
print(basket, x_basket)