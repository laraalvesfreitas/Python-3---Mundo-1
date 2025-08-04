#Desafio 11

#Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m2

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'A sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m2')
print(f'Para pintar a parede você vai precisar de {tinta} litros de tinta')