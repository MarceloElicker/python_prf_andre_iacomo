
'''
velocidade = 100

if (velocidade > 110):
    print(f'Sua velocidade é de {velocidade} km/h esta acima do limite permitido')
elif (velocidade >= 40):
    print(f'Sua velocidade é de {velocidade} km/h e vc esta dentro do permitido pela via')
else:
    print(f'Sua velocidade é de {velocidade} km/h e vc esta com uma velocidade muito baixa para a via')



#Valores lógicos

renda_mais_5mil = True
nome_limpo = False

if (renda_mais_5mil and nome_limpo):
    print('aprovado')
else:
    print('reprovado')


#for loops
for numero in range(1, 11):
    print(numero)

letras = 'Macelo'

for letra in letras:
    print(letras)



for numero1 in range(1,6):
    print(f'Produto {numero1}')
    for numero2 in range(5):
        print(numero1, numero2)


#for loops criando colunas
linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print('')


#While loop

valor = 100

while valor > 20:
    print(valor)
    valor -=5

'''

valor = int(input('Digite o valor do seu produto em R$; '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do produto sera de R${valor}')
    break