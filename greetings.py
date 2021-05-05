import sys
def customized_hello(sex, first_name, last_name):
    print("Hello %s %s %s!" % (sex, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit(1)
    sex = sys.argv[3]
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    
    
    customized_hello(sex ,first_name, last_name)
    """
    print(sys.argv[1:])
    customized_hello("John", "Cleese")
    """
