print('VAMOS CALCULAR O GASTO ENERGÉTICO!!')

sexo = int(input('Você e Homem [1] ou Mulher [2]?'))

while sexo not in [1, 2]:
    print("Modo de dificuldade inválido. Escolha novamente:")
    sexo = int(input('Você é Homem [1] ou Mulher [2]?'))

#Verifica o peso e tranformar strg em float
peso = str(input('Digite o seu peso em Kg:'))
peso = str(peso).replace(',','.')
numeric_transformer = float(peso)

altura = int(input('Dgite a sua altura em cm:'))

idade = int(input('Digite a sua idade:'))

if sexo == 1:
    caloric_expenditure = 66 + (13.7 * numeric_transformer) + (5 * altura) - (6.5 * idade)
    print(f'O seu gasto energético e de {caloric_expenditure} calorias.')

else:
    caloric_expenditure = 655 + (9.6 * numeric_transformer) + (1.8 * altura) - (4.7 * idade)
    print(f'O seu gasto energético e de {caloric_expenditure} calorias.')

