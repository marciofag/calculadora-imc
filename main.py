# Calculo de IMC - Índice de Massa Corporal

altura = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print('Magreza')
elif 18.5 <= IMC < 24.9:
    print('Normal')
elif 25.0 <= IMC < 29.9:
    print('Sobrepeso')
elif 30.0 <= IMC < 39.9:
    print('Obesidade')
else:
    print('Obesidade grave')
