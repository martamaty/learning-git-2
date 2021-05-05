import time
t0=time.time()
from faker import Faker
fake = Faker()
for _ in range(100):
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

"""
for _ in range(3):
    viz=[]
    viz.append(fake.name())
    viz.append(fake.address())
    viz.append(fake.job())
    viz.append(fake.email())
    print(viz)
    print(viz[0],viz[3])
"""

# ***************






# ***************

"""
    print(fake.address())
    print(fake.job())
    print()
"""
# 'Lucy Cechtelar'

"""
print(fake.address())
print(fake.job())
"""

# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

"""
print(fake.text())
"""
"""
for _ in range(3):
    print(fake.name())
    print(fake.address())
"""
