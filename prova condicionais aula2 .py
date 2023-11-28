#variaveis 
vel = int(input('Digite a velocidade do carro: '))
limite_vel = 80
#calculo velocidade excedida 
vel_excesso = vel - limite_vel
#calculo valor da multa
valor_multa = vel_excesso * 20

if vel_excesso > 0:
    print(f'Você foi multado em {valor_multa} reais, pois excedeu {vel_excesso} km')
else:
    print('Você esta no limite de velocidade então não foi multado')