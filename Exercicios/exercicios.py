import minhasfuncoes
import random

# Crie uma função para pedir um número inteiro ao usuário e retornar ele. Toda vez que você precisar de um número informado pelo usuário, 
# utilize ela. Ela não tem parâmetro e o retorno é o valor digitado pelo usuário já com o tipo inteiro.


# print ( minhasfuncoes.numeroInteiro() )


# Faça uma função para gerar números aleatórios. Esta função deve receber um número inteiro num e retornar um número aleatório entre 1 e 
# num. Assim, toda vez que você precisar de um número qualquer pode usar a função do exercício 1 ou esta.


# print( minhasfuncoes.aleatorio() )


# Faça uma função que receba um número inteiro por parâmetro e retorne o mês correspondente ao número. Por exemplo, 2 corresponde a 
# "Fevereiro". Se o número informado não corresponder a um mês (1 a 12), retorne a mensagem “Mês inválido”.

# x =  minhasfuncoes.numeroInteiro()

# minhasfuncoes.calendario(x)

# Faça funções para resolver as equações de área:
# do quadrado = x²  
# y = minhasfuncoes.numeroInteiro()
# x = minhasfuncoes.quadrado(y)

# print(f"{y} ao quadrado é {x}")

# do retângulo = b . h 	(base x altura)

# y = minhasfuncoes.numeroInteiro()
# z = minhasfuncoes.numeroInteiro()
# x = minhasfuncoes.retangulo(y, z)

# print(x)

# do triângulo= (b . h)2

# y = minhasfuncoes.numeroInteiro()
# z = minhasfuncoes.numeroInteiro()
# x = minhasfuncoes.triangulo(y, z)
# print(x)

# do trapézio = (B + b) . h2

# y = minhasfuncoes.numeroInteiro()
# z = minhasfuncoes.numeroInteiro()
# c = minhasfuncoes.numeroInteiro()
# x = minhasfuncoes.trapezio(y, z, c)

# print(x)


# Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que n! depende de (n-1)!; 
# este por sua vez depende de (n-2)!; e, assim por diante, até que n seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo.
#  Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial
#  deste número, também do tipo inteiro.

# minhasfuncoes.fatorial(7)

# Crie uma função para calcular o fatorial, mas não utilize laço de repetição.


# print(minhasfuncoes.fatorial(4))

# Faça uma função que recebe um vetor de números inteiros como 
# parâmetro. Esta função deve calcular o dobro de cada valor do 
# vetor e retornar um vetor inteiro atualizado com o dobro de 
# cada número. Dica: crie outro vetor dentro da função com o
#  mesmo tamanho para preencher com o dobro. 


# tamanho = 5
# vetor = [0] * tamanho

# for i in range(0, len(vetor)):
#     vetor[i] = random.randint(1,100)
#     print("Vetor Original:",vetor[i])


# minhasfuncoes.dobro(vetor)

# Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato DD de Mês Por Extenso de AAAA.
# Para pegar o mês por extenso, utilize a função criada no 
# exercício 3. Por exemplo: 18/09/2019 retorna 18 de Setembro 
# de 2019.

dataE = input("Digite a data no formato DD/MM/AAAA:")

minhasfuncoes.mesdata(dataE)