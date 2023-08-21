'''
8) Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo.
'''

num = 1
while(num <= 20):
    div = num %2
    if(div == 1):
        print(f"{num} é ímpar")
    num = num +1