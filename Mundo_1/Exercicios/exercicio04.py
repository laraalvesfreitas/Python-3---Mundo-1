#Desafio 04

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

a = input('Digite algo: ')

print(f" O tipo primitivo deste valor é {type(a)}")
print(f" Só tem espaço? {a.isspace()}")
print(f" É um número? {a.isnumeric()}")
print(f" É Maisculo? {a.isupper()}")
