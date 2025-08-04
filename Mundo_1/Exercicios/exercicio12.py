#Desafio 12
#Faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto 

preco_antigo = float(input('Digite o valor do produto: '))
preco_novo = preco_antigo - (preco_antigo  * 5/100)
print(f'O novo preço do produto é de R${preco_novo}')
