class Category:
    
    def __init__(self, nome):
        self.nome = nome
        self.ledge = []
            

    def deposit(self, valor, descricao=''):
        self.ledge.append({'amount':valor,'description':descricao})
    def withdraw(self, valor, descricao=''):
        if self.check_funds(valor):
            self.ledge.append({'amount':-valor,'description':descricao})
        
    def get_balance(self):
        balanço = 0
        for i in self.ledge:
            balanço += i['amount']
        return balanço
        
    def transfer(self, valor, categoria):
        if self.check_funds(valor):
            self.withdraw(valor, f"Transfer to {categoria.nome}")
            categoria.deposit(valor,f"Transfer from {self.nome}")
            return True
        else:
            return False
        
    def check_funds(self, valor):
        if valor > self.get_balance():
            return False
        elif valor <= self.get_balance():
            return True
         
def create_spend_chart(categories):
    pass
    
c1 = Category('Comidas')
c2 = Category('Bebidas')
print(c1.nome)
print(c2.nome)
c1.deposit(50,'compra de peixe')
c1.deposit(50,'compra de carne')
c1.deposit(30,'compra de arroz')
c1.withdraw(20,'retirada')

c2.deposit(10, 'cocacola')
c2.deposit(30,'leite')

print(c1.ledge)
print(c2.ledge)
print(c1.get_balance())
print(c2.get_balance())
print('--------------------')
c1.transfer(10, c2)

print(c1.ledge)
print(c2.ledge)
print(c1.get_balance())
print(c2.get_balance())