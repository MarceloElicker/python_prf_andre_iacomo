
# Meu primeiro código
'''
print('olá, Mundo!')
print('tudo Bem')
print('Que dia é hj?')

'''
'''
x= str(3)
y= int(4)
z= float(5)

print(x, y, z)

# O Marcelo tem 36 ano e mora em Floripa.

nome = 'Marcelo'
idade = 36
cidade = 'Floripa'


# Tratando valores
nome = input('Qual é teu nome? ')
idade = input('Que idade tu tem? ')
cidade = input('Mora onde? ')

print('O ' + nome + ' tem ' + str(idade) + ' anos e mora em ' + cidade)



anoNacimento = input('Em que ano vc nasceu? ')
idade = 2022 - int(anoNacimento)

print(idade)



#slice 'cortando'

fruta = 'Abacate'
print(fruta[3])
print(fruta[2:5])


#formatando strings
print(f'eu amo {fruta}')

'''
# Metodos para strings

mensagem = 'Eu AMO comida caseira'

print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.replace('caseira', 'da minha mãe'))

