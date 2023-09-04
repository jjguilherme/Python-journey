# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_hora_trampada = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalha no mês? "))

salario = valor_hora_trampada * horas_trabalhadas

print("Salario: " + str(salario))
