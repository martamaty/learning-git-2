#Cwiczenie-rozne typy argumentow

"""def fun_default(coffee, milk='soya',sugar='brown'):

def fun_positional(coffee, /milk):
    print(coffee)
def fun_keyword(coffee, *, milk='soya', sugar='brown'):
    pass"""


"""def count_them_all(*sratom):
    positional_args_count = len(sratom)
    print(f"I have received {positional_args_count} positional arguments")

count_them_all(1, 2, 3, "A")

def count_them_all(**kwargs):
    positional_kwargs_count = len(kwargs)
    print(f"i have recived {positional_kwargs_count} named")
count_them_all(pay='card',shop='local')

def count_them_all(*args, **kwargs):
    print(count_them_all)"""

"""shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]
def get_index_1_tuple_element(given_tuple):
    return given_tuple[1]

sorted_items = sorted(shopping_items, key=get_index_1_tuple_element)
print(sorted_items)

def get_index_2_tuple_element(given_tuple):
    return given_tuple[2]

sorted_items = sorted(shopping_items, key=get_index_2_tuple_element)
print(sorted_items)"""

shopping_items=["jajka","bulka","ser feta","maslo","pomidor","cynamon","arbus"]
shopping_items.append("chusteczki")
shopping_items.append("papier")
def shopping(items):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart


basket = shopping(shopping_items)
print(basket)

