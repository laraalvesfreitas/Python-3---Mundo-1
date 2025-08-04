#Desafio 13
#Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário com 15% de aumento

salario_antigo =  float(input('Digite seu salário: R$ '))
salario_novo = salario_antigo + (salario_antigo * 15 /100)

print(f'Seu salário com aumento será de R${salario_novo :.2f}')
