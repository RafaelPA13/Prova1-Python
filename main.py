#Código Prova
print('Boas vindas a vinheria Agnello!')

ano_nascimento = int(input('Por favor informe seu ano de nascimento: '))
ano_permitido = 2024 - ano_nascimento

vinho1 = 'Vinho do Porto R$150'
vinho2 = 'Uva do Vale R$50'
vinho3 = 'Seu Uvão R$250'

if ano_permitido < 18:
    print('Não é permitida a venda de bebidas alcoólicas para pessoas menores de idade. Tenha um bom dia!')
else:
    endereco = input('Por favor informe o seu endereço: ')
    print(f'Qual vinho você gostaria de comprar:\n 1: {vinho1}\n 2: {vinho2}\n 3: {vinho3}')
    escolha = int(input('Digite o número do vinho de sua escolha: '))
    preco_vinho = 0
    if escolha == 1:
        preco_vinho = 150
    elif escolha == 2:
        preco_vinho = 50
    else:
        preco_vinho = 250
    qtd_garrafas = int(input('Por favor informe a quantidade de garrafas: '))
    if preco_vinho > 100:
        taxa = 0
    else:
        taxa = preco_vinho * 0.3
    print(f'Agradeçemos a confiança! O valor total é de R${preco_vinho * qtd_garrafas} com taxa de R${taxa}. Sua entrega será enviada para {endereco} em breve.')
