# SER O MAIOR NÚMERO

lista = [] #Lista vazia criada para receber os valores de 'num'
for c in range(1,4): #criado para não ter que criar variáveis iguais ex: num1,num2 e num3
    num = int(input('\033[1:4:33mdigite um número:\033[m '))
    lista.append(num)
print(f'O maior número da sequência é {max(lista)}')
