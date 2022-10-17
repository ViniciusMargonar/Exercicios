import random
import math
# 1

def numeroInteiro():
    numInt = int(input("Digite o numero inteiro:"))
    return numInt

# 2

def aleatorio():
    # aleat2 = int(input("Sortear de 1 a:"))
    aleat = random.randint(1, numeroInteiro())
    return aleat

# 3

def calendario(a):
    if ( a == 1):
        return "Janeiro"
    elif ( a == 2):
        return "Fevereiro"
    elif ( a == 3):
        return "Março"
    elif ( a == 4):
        return "Abril"
    elif ( a == 5):
        return "Maio"
    elif ( a == 6):
        return "Junho"
    elif ( a == 7):
        return "Julho"
    elif ( a == 8):
        return "Agosto"
    elif ( a == 9):
        return "Setembro"
    elif ( a == 10):
        return "Outubro"
    elif ( a == 11):
        return "Novembro"
    elif ( a == 12):
        return "Dezembro"
    else:
        return "Mês inválido!" 

# 4
# A
def quadrado(a):
    quad = a * a
    return quad

# B
def retangulo(b, h):
    retan = b * h
    return retan

# C
def triangulo(b, h):
    trian = (b * h)/2
    return trian

# D
def trapezio(a, b, h):
    trap = ((a + b) * h)/2
    return trap

#5

# Fatorial com laço:

def fatorial(n):
    cont = 1
    for i in range(n, 0, -1):
        cont *= i
    print(cont)

#6

# Fatorial sem laço:

def fatorial(n):
    if(n == 1):
        return 1
    return n * fatorial(n-1)

#10

def dobro(a):
    vetD = [0] * len(a)
    for i in range(0, len(a)):
        a[i] = a[i] * 2    
        vetD[i] = a[i]
        print("Vetor Dobrado:",vetD[i])

#11

def mesdata(a):
    teste = a.split("/")
    vetor = [0] * len(teste)

    # Verificar se tem 0 no inicio:
    if(len(teste[1]) == 2):
        vetor[1] = round(vetor[1]) 
    
    # Converter para int e salvar em vetor:
    for i in range(0, len(teste)):
        vetor[i] = int(teste[i]) 

    # Data é válida?
    if(vetor[0] > 31 or vetor[0] < 1):
        print("Dia Inválido, digite novamente!")
        
    else:
        dia = vetor[0]
        ano = vetor[2]
        print(f"{dia} de {calendario(vetor[1])} de {ano}")
    
