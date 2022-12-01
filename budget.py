from itertools import zip_longest

class Category:
    
    def __init__(self, nome):
        self.nome = nome
        self.ledger = []
            
    def __str__(self):
        str_nome = '{:*^30}'.format(self.nome)
        str_ledge = ''
        str_total = 0
        for i in self.ledger:
            formata = '{:7.2f}'.format(i['amount'])
            str_amount = str(formata)
            qtd = 30-len(i['description'])
            str_amount = str_amount.rjust(qtd,' ')
            #str_desc = '{:''>espaços}'.format(i['description'])
            str_ledge += f'{i["description"][:23]}'+str_amount+'\n'
            str_total += i['amount']
        str_ledge += f'Total: {str_total}'  
        return f'{str_nome}\n'+str_ledge

    def deposit(self, valor, descricao=''):
        self.ledger.append({'amount':valor,'description':descricao})
    def withdraw(self, valor, descricao=''):
        if self.check_funds(valor):
            self.ledger.append({'amount':-valor,'description':descricao})
            return True
        else:
            return False
        
    def get_balance(self):
        balanço = 0
        for i in self.ledger:
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
    lista_porc = []
    for i in categories:
        l = i.ledger
        soma_dep = 0
        soma_ret = 0
        for i in l:
            if i['amount'] > 0: 
                soma_dep += i['amount']
            elif i['amount'] < 0 and 'Transfer' not in i['description']:
                soma_ret += i['amount']
        #print(soma_dep, soma_ret)
        porcentagem_gastos = (abs(soma_ret) * 100)/soma_dep
        lista_porc.append(round(porcentagem_gastos,-1))
        #print('Porcentagem:', porcentagem_gastos)
    tam_lista_porce = 10 - len(lista_porc)
    #for i in range(0, tam_lista_porce):
    #    lista_porc.append(0)    
    print('lista porcentagem:',lista_porc)
    string_cat = ''
    string_cat_temp = ''
    maior = 0
    l_cat_n = []
    num_cat = 4 - len(categories)
    for i in categories:
        if len(i.nome)> maior:
            maior = len(i.nome)
        l_cat_n.append(i.nome)
    if num_cat >=1:
        for i in range(0,num_cat):
            l_cat_n.append(' ')
    
    #print('O maior é ',maior)
    #print('Lista de nomes:', l_cat_n) 
    d = ''
    for i,j,k,m in zip_longest(l_cat_n[0],l_cat_n[1],l_cat_n[2], l_cat_n[3], fillvalue=' '):
        d += f'     {i}  {j}  {k}  {m} \n'
    #print(d)
    '''
    cont_cat = 0
    while cont_cat < maior:
        for i in categories:
            string_cat_temp += i.nome[cont_cat] +' '
        string_cat += string_cat_temp+'\n'
        string_cat_temp = ''
        cont_cat += 1 
    '''
    lista_porc.sort(reverse=True)
    
    grafico = 'Percentage spent by category\n'
    for i in range(100,-1,-10):
        cont = 0
        cont_o = 0
        while cont < len(lista_porc):
            if i <= lista_porc[cont]:
                cont_o += 1 
            
            cont +=1
        if cont_o == 0:
            temp = str(i).rjust(3, ' ')+'|\n'
        bola = 'o  '*cont_o
        #bola = bola[:len(categories*3)]        
        temp = str(i).rjust(3, ' ')+'| '+bola+'\n'
        grafico +=temp 
           
    grafico +='    ----------\n'
    grafico += d
    #matriz de nomes das categorias
     
    return grafico
    print(len(grafico))
    #print(lista_porc)
    #print(string_cat)
    


    
c1 = Category('Comidas')
c2 = Category('Bebidas')
c3 = Category('Remedios')

print(c1.nome)
print(c2.nome)
c1.deposit(50,'compra de peixe')
c1.deposit(50,'compra de carne')
c1.deposit(30,'compra de sal')
c1.withdraw(20,'retirada')

c2.deposit(10, 'cocacola')
c2.deposit(30,'leite')
c2.deposit(50, 'agua')
c2.withdraw(50,'retirada')

c3.deposit(50,'amoxilina')
c3.deposit(50,'cimegripe')
c3.withdraw(30,'qualquer')



print(c1.ledger)
print(c2.ledger)
print(c1.get_balance())
print(c2.get_balance())
print('--------------------')
c1.transfer(10, c2)

print(c1.ledger)
print(c2.ledger)
print(c1.get_balance())
print(c2.get_balance())

print(c1)
print(c2)

lista = [c1,c2,c3]
print(create_spend_chart(lista))