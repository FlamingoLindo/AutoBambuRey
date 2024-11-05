from faker import Faker

fake = Faker('pt_BR')

"""
RUA [0]
NUMERO [1]
CIDADE [2]
CEP [3]
ESTADO [4]
"""

def create_address():
    while True:
        address = fake.address()
        lines = address.splitlines()
        
        try:
            rua, numero = lines[0].split(',', 1)
        except ValueError:
            continue  
        
        cidade = lines[1]
        
        try:
            cep, estado = lines[2].split(' ', 1)
        except ValueError:
            continue  

        estado = estado.split('/')[1]

        if not numero.strip():
            continue

        return rua.strip(), numero.strip(), cidade.strip(), cep.strip(), estado.strip()