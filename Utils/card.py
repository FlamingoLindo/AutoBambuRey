from faker import Faker

fake = Faker('pt_BR')
"""
MASTERCARD [0]
NOME [1]
CODIGO [2]
EXP [3]
CVV [4]
"""
def create_card():
    while True:
        card = fake.credit_card_full()
        lines = card.splitlines()

        if lines[0] == 'Mastercard':
            master_card = lines[0]
            
            nome = lines[1]
            
            codigo, exp = lines[2].split(' ', 1)

            cvv = lines[3].split('CVV: ')[1].strip()

            return master_card, nome, codigo, exp, cvv
        
