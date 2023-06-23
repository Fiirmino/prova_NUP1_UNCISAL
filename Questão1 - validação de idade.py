idade = int(input('\033[1:4:33mInforme a idade da pessoa:\033[m'))
if idade>=0 and idade<=12:
    print(f'A pessoa tem {idade} anos, logo, ela é uma criança.')
elif idade>12 and idade<=17:
    print(f'A pessoa tem {idade} anos, logo, ela é adolescente.')
elif idade>17 and idade <=59:
    print(f'A pessoa tem {idade} anos, logo, ela é adulta.')
else:
    print(f'A pessoa tem {idade} anos, logo, ela e idosa.')
print('------------------------------------------------------')