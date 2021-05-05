def Card():
    import time
    t0=time.time()

    from faker import Faker
    fake = Faker()
    for _ in range(10):
        class Biz_Card:
            def __init__(self, name, company,address, position, mail):
                self.name = name
                self.address = address
                self.position = position
                self.company = company
                self.mail = mail
                    
        contact=Biz_Card(name=fake.name(), address=fake.address(), company=fake.company(),position=fake.job(), mail=fake.email())
        print(contact.name," ",contact.mail," ",contact.company,"")
        
    t1=time.time() - t0
    print("time elapsed:",t1)

Card()