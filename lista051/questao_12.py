'''
12) Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
'''


num = float(input("Digite um número (-1 encerra o programa):"))
maior = num
menor = num
total_respostas = 0 #contador
soma = 0 #acumulador

while( num != -1):
    total_respostas = total_respostas +1
    soma = soma + num

    if( maior < num):
        maior = num

    if(menor > num):
        menor = num


    num = float(input("Digite um outro número (-1 encerra o programa):"))
if( maior == -1):
    print("Você inseriu -1 na primeira resposta.\nPROGRAMA ENCERRADO")
else:
    print(f"Maior valor inserido : {maior}")
    print(f"Menor valor inserido : {menor}")
    print(f"Total de respostas {total_respostas}")
    print(f"Média {soma/total_respostas}")
    print("FIM DO PROGRAMA")