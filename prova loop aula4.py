soma = 0
qnt_num = 0

while True:
    num = int(input('Digite um numero (digite 0 para encerrar): '))
    if num == 0:
        break
    
    soma += num
    qnt_num += 1

if qnt_num > 0:
    print(f'A quantidade de numeros digitada foi {qnt_num}')
    print(f'A soma dos numeros é {soma}')
    print(f'A média doa numeros é', soma / qnt_num )
else:
    print('Nenhum numero foi digitado')