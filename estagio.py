'''
O que o sistema deverá fazer:

Este sistema deverá permitir que um usuário, ao rodar o código, configure um carrinho de compras que permite o cadastro de até 10 produtos por carrinho. Ao fechar o carrinho o sistema deverá exibir todos os itens comprados, o valor total da compra e qual o mínimo de notas que será necessário para pagar este total. Ou seja, este carrinho de compras deve funcionar da seguinte forma:


1- Ao rodar o sistema já estamos no carrinho de compras aguardando o primeiro produto ser cadastrado.

2- Para cadastrar um produto o usuário deve definir o nome e o valor do produto.

3- Após cadastrar o primeiro produto o sistema deve permitir que o usuário cadastre um novo produto ou permitir que o usuário finalize o carrinho.

4- Se o usuário decidir cadastrar mais um produto, o mesmo processo do item 3 se repete.

5- Se o usuário decidir finalizar o carrinho o sistema deve exibir todos os produtos comprados, o valor total do carrinho e o mínimo de notas necessário para pagar a conta deste carrinho. (Devem ser consideradas apenas as notas: 100, 50, 20, 10, 5, 2 e 1)
Gustavo Storithont Mudri
'''
soma = 0
valortotal = 0
produtos=dict() # produtos = {nome do produto:[quantidade,valor_total]}

def valorproduto():
    try:
        produto_valor =  int(input("Valor:"))
    except ValueError:
        print("O valor precisa ser um numero inteiro")
        recursividade = input("1-Continuar | Saír")
        if recursividade == 1:
            valorproduto()
        else:
            quit()
        produto_valor = valorproduto()
    return produto_valor
def finalizar():
    finalizado = int(input("comprar mais produtos? 1-Sim|2-Finalizar Compra:"))
    if finalizado == 2:
        return
    elif finalizado == 1: 
        entrada_de_produtos(produtos,soma)
    else: 
        finalizar()
def entrada_de_produtos(produtos,soma):
    produto_nome =  input("Nome do produto:")
    if produtos.get(produto_nome) == None:
        produto_valor = valorproduto()
        produtos.update({produto_nome:[1,produto_valor]})
    else:
        quantidade = produtos.get(produto_nome)[0] + 1
        produtos.update({produto_nome:[quantidade,produtos[produto_nome][1]]})
    soma += 1
    if soma == 10:
        print("Limite de 10 compras atingido")
        return produtos    
    finalizar()

entrada_de_produtos(produtos,soma)

print("Produtos do carrinho:")

for key in produtos.keys():
    if produtos[key][0] == 1:
        print(key)
        valortotal += produtos[key][1]
    else:
        print(f'{produtos[key][0]} {key}')
        valortotal += produtos[key][1]*produtos[key][0]

print("Valor total:")
print(valortotal)

print("Deve ser no mínimo em:")

notas=[100,20,5]
for i,nota in enumerate(notas):
    if (int(valortotal/nota))==1:
        print(f'{int(valortotal/nota)} nota de {nota} reais')
        valortotal %= nota 
    if (valortotal/nota)>1:
        print(f'{int(valortotal/nota)} notas de {nota} reais')
        valortotal %= nota

if valortotal == 1:     
    print(f'{int(valortotal)} nota de 1 real')  
if valortotal > 1:
    print(f'{int(valortotal)} notas de 1 real') 
       # SolveLight
