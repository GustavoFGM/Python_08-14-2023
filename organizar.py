# Aula python 08/14/2023

'''
 Exercicio 12 - Crie um codigo completo e detalhado que retorne as duas raizes de 
 uma equaÃ§Ã£o de segundo grau usando a formula de bascara
'''

import math

# DefiniÃ§ao de funÃ§Ã£o

def calcular_raizes(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2

    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz, raiz

    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2

# Solicita os coeficientes da equaÃ§Ã£o de segundo grau ao usuÃ¡rio
coeficiente_a = float(input("Digite o coeficiente a: "))
coeficiente_b = float(input("Digite o coeficiente b: "))
coeficiente_c = float(input("Digite o coeficiente c: "))

# Calcula as raÃ­zes
raiz1, raiz2 = calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c)

# Exibe as raÃ­zes
print("As raÃ­zes da equaÃ§Ã£o sÃ£o:")
print("Raiz 1:", raiz1)
print("Raiz 2:", raiz2)



#  Exercicio 13 - Crie um codigo para calcular o mudulo de um vetor... em N dimensÃµes

import math

#definiÃ§Ã£o de funÃ§Ã£o

def calcular_modulo_vetor(vetor):
    soma_quadrados = 0
    for componente in vetor:
        soma_quadrados += componente**2
    modulo = math.sqrt(soma_quadrados)
    return modulo

# Solicita as componentes do vetor ao usuÃ¡rio
dimensoes = int(input("Digite o nÃºmero de dimensÃµes do vetor: "))
vetor = []
for i in range(dimensoes):
    componente = float(input(f"Digite a componente {i+1} do vetor: "))
    vetor.append(componente)

# Calcula o mÃ³dulo do vetor
modulo = calcular_modulo_vetor(vetor)

# Exibe o resultado
print("O mÃ³dulo do vetor Ã©:", modulo)

'''
Exercicio 14 - Crie um codigo utilizando funÃ§Ã£o para criar a sequencia de Fibonacci para os 
primeiro n elementos. Apresente-os e a seguir informe quais desses sÃ£o numeros primo

'''

# importa modulo sys
import sys

# DefiniÃ§Ã£o de funÃ§Ã£o

 # Inicializa a sequÃªncia de Fibonacci com os dois primoiros nÃºmeros
def fibonacci(n):
    Sequencia_Fibonacci = [1, 1] 

    while len(Sequencia_Fibonacci) < n:
        proximo_numero = Sequencia_Fibonacci[-1] + Sequencia_Fibonacci[-2]  # Calcula o prÃ³ximo nÃºmero da sequÃªncia
        Sequencia_Fibonacci.append(proximo_numero)  # Adiciona o prÃ³ximo nÃºmero Ã  lista da sequÃªncia

    return Sequencia_Fibonacci


def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

n = int(input("Digite o valor de 'n': "))
fibonacci_seq = fibonacci(n)

# Mostra a sequÃªncia de Fibonacci
print("SequÃªncia de Fibonacci:")
print(fibonacci_seq)

# Mostra quais nÃºmeros sÃ£o primos
primos = [numero for numero in fibonacci_seq if eh_primo(numero)]
print("NÃºmeros primos na sequÃªncia de Fibonacci:")
print(primos)



# Exercicio 15 - entendendo parÃ¢metros, argumentos, *args e **kwargs

def calculadora_salario(valor, horas=220):
    return horas * valor

valor_total = calculadora_salario(299.25)

print(valor_total)

'''
Exercicios envolvendo args e kwargs
'''

'''
exercicio 15 - Crie uma funÃ§Ã£o chamada soma que recebe argumentos posicionais 
variÃ¡veis e retorna a soma de todos os nÃºmeros passados como argumentos.
'''

#DefiniÃ§Ã£o de funÃ§Ã£o

def soma(*args):
    return sum(args)

resultado = soma(2, 4, 6, 8)
print(resultado)  # Deve imprimir 20


'''
ExercÃ­cio 16: Calculadora AvanÃ§ada

Crie uma funÃ§Ã£o chamada calculadora que aceita argumentos nomeados 
variÃ¡veis para realizar operaÃ§Ãµes matemÃ¡ticas bÃ¡sicas. 
Os argumentos possÃ­veis sÃ£o: num1, num2, e operacao. 
As operaÃ§Ãµes possÃ­veis sÃ£o: "soma", "subtracao", "multiplicacao" e "divisao".
'''

#DefiniÃ§Ã£o de funÃ§Ã£o

def calculadora(**kwargs):
    num1 = kwargs.get('num1', 0)
    num2 = kwargs.get('num2', 0)
    operacao = kwargs.get('operacao', 'soma')

    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisÃ£o por zero"

resultado = calculadora(num1=10, num2=5, operacao='subtracao')
print(resultado)  # Deve imprimir 5


'''
ExercÃ­cio 17: MÃ©dia simples

Crie uma funÃ§Ã£o que recebe um nÃºmero indeterminado de argumentos nomeados 
representando as notas 
'''

#Definicao de funÃ§Ã£o

def calcula_media(*args):
    return sum(args) / len(args)

numeros = [float(x) for x in input("Digite uma lista de nÃºmeros separados por espaÃ§o: ").split()]
resultado = calcula_media(*numeros)
print(f"A mÃ©dia Ã©: {resultado}")


'''