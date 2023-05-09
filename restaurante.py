class Mesa:
    def __init__(self):
        self.comanda = []
    def add_item(self, nome):
        self.comanda.append(nome)
    def acionar_comanda(self):
        return self.comanda
    def limpar_comanda(self):
        self.comanda = []

class Produto:
    
    def __init__(self, nome, preco = 0.0, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def exibir_produto(self):
        print(f'{self.nome}. R$ {self.preco}. Quantidade: {self.quantidade}')
    def exibir_quantidade(self):
        print(f'{self.nome}. Quantidade: {self.quantidade}')
    def exibir_preco(self):
        print(f'{self.nome}. R$ {self.preco}.')
    def exibir_nome(self):
        print(f'{self.nome}.')
    def mudar_estoque(self, quantidade):
        self.quantidade = quantidade
    def mudar_preco(self, preco):
        self.preco = preco
    def retirar(self):
        self.quantidade -= 1

class Caixa:
    def __init__(self, renda_bruta = 0, despesas = 0, lucro="0"):
        self.renda_bruta = renda_bruta
        self.despesas = despesas
        self.lucro = lucro
    def visualizar_renda(self):
        print(f'R$ {self.renda_bruta}')
    def visualizar_despesas(self):
        print(f'- R$ {self.despesas}')
    def visualizar_lucro(self):
        print(f'+ R$ {self.lucro}')
    def recebe(self, valor):
        self.renda_bruta += valor
    def debito(self, valor):
        self.despesas += valor
    def lucro_met(self):
        self.lucro = self.renda_bruta - self.despesas



m1 = Mesa()
m2 = Mesa()
m3 = Mesa()
m4 = Mesa()
m5 = Mesa()
m6 = Mesa()
m7 = Mesa()
m8 = Mesa()
m9 = Mesa()
m10 = Mesa()
mesas = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]


p1 = Produto('Strogonoff', 15)
p2 = Produto('Feijoada', 20)
p3 = Produto('X-salada', 22)
p4 = Produto('X-pernil', 23)
p5 = Produto('Água 600mL', 2)
p6 = Produto('Coca-Cola 600mL', 6)
p7 = Produto('Coca-Cola 1L', 9)

estoque = [p1, p2, p3, p4, p5, p6, p7]

caixa = Caixa()


def prompt():
    print('PROMPT')
    print('1 - Adicionar item a comanda') #Adiciona item a uma comanda, e retira um item do estoque.
    print('2 - Exibir comanda') #exibe a comanda, com os produtos consumidos e o valor final.
    print('3 - limpar comanda') #limpa a comanda, e contabiliza o valor no caixa.
    print('4 - Gerenciar estoque') #Modifica o valor do item no estoque.
    print('5 - Exibir estoque') #Exibe o estoque, listando os produtos com as suas quantidades.
    print('6 - Mudar preço') #Modifica o preço de um item.
    print('7 - Exibir lucro') #Exibe o lucro
    print('8 - Exibir renda bruta') #Exibe a renda bruta
    print('9 - Exibir despesas') #Exibe o valor das despesas
    print('10 - Adicionar despesa') #Adiciona despesa
    print('11 - Adicionar produto') #Adiciona novo produto
    print('12 - Adicionar mesa') #Adiciona novo mesa
    print('13 - Remover produto') #Remove produto
    print('14 - Remover mesa') #Remove mesa
    print('15 - Exibir mesas disponiveis') #Exibe mesas disponiveis

    print('\n')
    numero = int(input('Escolha uma opção: '))
    return numero

while True:
    caixa.lucro_met()
    print('\n')
    print('AVISOS: ')
    for c in estoque:
        if c.quantidade <= 0:
            print(f'{c.nome.upper()} EM FALTA!')
        elif c.quantidade <= 10:
            print(f'{c.nome.upper()} ACABANDO!')
    print('\n')
    opcao = prompt()

    if opcao == 1:
        print('\n')
        print('ADICIONAR ITEM A COMANDA')
        numero_comanda = int(input('Escolha o numero da mesa: '))
        cont = 0
        for c in estoque:
            cont += 1
            print(f'{cont} - ', end='')
            c.exibir_preco()
        item = int(input('Qual item você quer adicionar: '))
        mesas[numero_comanda - 1].add_item(estoque[(item - 1)])
        estoque[item - 1].retirar()
        print('Produto Adicionado com sucesso!')
    elif opcao == 2:
        print('\n')
        print('EXIBIR COMANDA')
        numero_comanda = int(input('Escolha o numero da mesa: '))
        comanda = mesas[numero_comanda - 1].acionar_comanda()
        preco_total = 0
        print('\n')
        print(f'COMANDA {numero_comanda}')
        for c in comanda:
            preco_total += c.preco
            c.exibir_preco()
        print(f'PREÇO FINAL: R${preco_total}')
    elif opcao == 3:
        print('\n')
        print('LIMPAR COMANDA')
        numero_comanda = int(input('Escolha o numero da mesa: '))
        comanda = mesas[numero_comanda - 1].acionar_comanda()
        preco_total = 0
        for c in comanda:
            preco_total += c.preco
        caixa.recebe(preco_total)
        mesas[numero_comanda - 1].limpar_comanda()
    elif opcao == 4:
        print('\n')
        print('GERENCIAR ESTOQUE')
        cont = 0
        for c in estoque:
            cont += 1
            print(f'{cont} - ', end='')
            c.exibir_nome()
        item = int(input('Qual item você quer gerenciar: '))
        qnt = int(input('Coloque a nova quantidade: '))
        estoque[item - 1].mudar_estoque(qnt)
    elif opcao == 5:
        print('\n')
        print('ESTOQUE')
        for c in estoque:
            c.exibir_produto()
    elif opcao == 6:
        print('\n')
        print('MUDAR PREÇO')
        cont = 0
        for c in estoque:
            cont += 1
            print(f'{cont} - ', end='')
            c.exibir_preco()
        item = int(input('Qual item você quer gerenciar: '))
        novo_preco = int(input('Coloque o novo preço: '))
        estoque[item - 1].mudar_preco(novo_preco)
    elif opcao == 7:
        print('\n')
        print('LUCRO')
        caixa.visualizar_lucro()
    elif opcao == 8:
        print('\n')
        print('RENDA BRUTA')
        caixa.visualizar_renda()
    elif opcao == 9:
        print('\n')
        print('DESPESAS')
        caixa.visualizar_despesas()
    elif opcao == 10:
        print('\n')
        print('ADICIONAR DESPESA')
        numero = int(input('Valor da despesa: '))
        caixa.debito(numero)
    elif opcao == 11:
        print('\n')
        print('ADICIONAR NOVO PRODUTO')
        nome = input('Nome do novo produto: ')
        preco = int(input('preço do novo produto: '))
        quantidade = int(input('quantidade do novo produto: '))
        estoque.append(Produto(nome, preco, quantidade))
    elif opcao == 12:
        print('\n')
        print('ADICIONAR MESA')
        mesas.append(Mesa())
    elif opcao == 13:
        print('\n')
        print('REMOVER PRODUTO')
        numero = int(input('Escolha o numero do produto: '))
        estoque.pop(numero - 1)
    elif opcao == 14:
        print('\n')
        print('REMOVER MESA')
        mesas.pop()
    elif opcao == 15:
        print('\n')
        print('MESAS DISPONIVEIS')
        print(f'Mesas totais: {len(mesas)}')
        cont = 0
        cont2 = 0
        for c in mesas:
            cont += 1
            comanda = c.acionar_comanda()
            if len(comanda) == 0:
                cont2 += 1
                print(f'Mesa {cont} Disponivel.')
        print(f'Mesas disponiveis: {cont2}')

    else:
        break