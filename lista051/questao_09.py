'''
9) Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2.
'''
cont = 1
soma = 0

while(cont <= 500):
    div = cont %2
    soma = soma + cont
    if(div == 0):
        print(f"{cont} é par")
    cont = cont + 1
    print(f"{soma} é a soma ")