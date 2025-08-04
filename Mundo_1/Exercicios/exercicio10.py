#Desafio 10

#Crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 
#Considerar dolar R$5.54

dinheiro_carteira = float(input('Qual o saldo da sua carteira? R$ '))
conveter = dinheiro_carteira  / 5.54
print(f'Com seu saldo atual R${dinheiro_carteira} você consegue comprar US${conveter :.2f} dolares ')



