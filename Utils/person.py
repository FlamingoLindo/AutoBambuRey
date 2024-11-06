from faker import Faker
import random

fake = Faker('pt_BR')

def create_random_full_name():
    name = fake.name()
    
    return name

def create_random_first_name():
    name = fake.name().split(' ')[0]
    
    return name

def create_random_surname():
    name = fake.name().split(' ')[1]
    
    return name

def create_random_email():
    email = fake.email()
    
    return email

def create_cnpj():
    cnpj = fake.cnpj()
    
    return cnpj

def create_cpf():
    cpf = fake.cpf()
    
    return cpf

def create_phone():
    phone = random.randint(1111111111,99999999999)
    
    return phone

def create_password():
    password = fake.password()
    
    return password

def create_birth_day():
    while True:
        birth_day = fake.date_of_birth()
        
        if birth_day.year <= 2003:
            break

    birth_day_br = birth_day.strftime("%d/%m/%Y")
    
    return birth_day_br