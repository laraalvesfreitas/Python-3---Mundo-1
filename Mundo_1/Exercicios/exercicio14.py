#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperatura = float(input('Informe a temperatura em c°: '))
converter = temperatura * 9/5 + 32
print(f'A temperatura {temperatura} convertida para fahrenheit é {converter}°F')


