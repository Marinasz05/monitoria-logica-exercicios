# Exercício 3: Par ou ímpar
# Complete a condição para verificar se o número é par ou ímpar

"""
    - O programa deve pedir ao usuário que digite um número inteiro.
    - Após isso, o programa deve verificar se o número digitado é
      par ou ímpar.
"""
numero = int(input('Digite um número inteiro: '))

if numero % 2 ==0 :
    print('Esse número é par')

else :
    print('Esse número é ímpar')
