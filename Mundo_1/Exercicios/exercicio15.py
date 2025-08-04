#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
valor_dia = (dias * 60) 
valor_km = km * 0.15
total = valor_dia + valor_km


print(f'O carro foi alugado por {dias} e percorreu {km} km')
print(f'O valor a ser pago pelo aluguel do carro é R${total}')