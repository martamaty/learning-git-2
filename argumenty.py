def fun_default(breakfast_english,b='coffee'):
    print(breakfast_english,b)
fun_default('cont',)

def fun_positional(breakfast_english,drink_coffee):
    print('english','tea')
fun_positional('1','2')

def fun_keyword(x,a='english', b='coffee'):
    print(x,a,b)
fun_keyword(0,'conti','tea')

def customized_hello(first_name, last_name):
    print("Hello Mr ",first_name, last_name,"are yoiu ok?")

customized_hello("adi", "sov")

items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor"
]
payment='reka'
def shopping(items, payment='card', shop='local', bag='plastic', transport='own'):
    print(items,payment,shop,transport,bag)
shopping(items, shop='supermaket')
shopping(items, payment='cash',transport='delivery')
shopping(items,'cash',bag='paper',transport='delivery')
shopping(items,'cash','paper',transport='delivery')

def count_them_all(*args):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")

count_them_all(1, 2, 3,4,5,8,9, "A")

def count_them_all(*args, **kwargs):
    positional_args_count = len(args)
    named_kwargs_count = len(kwargs)
    print(f"I have received {positional_args_count} positional arguments and {named_kwargs_count} named argumrnts")

count_them_all(1, 2, 3, "A", a=1, b=2,c=3,f=10)