# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(num):
    a, b = 0, 1
    
    # Verifica se o número informado é 0 ou 1, que são os dois primeiros números da sequência
    if num == 0 or num == 1:
        return True
    
    # Itera até encontrar um número maior ou igual a 'n'
    while b < num:
        # Gera o próximo número da sequência
        a, b = b, a + b
    
    # Verifica se o número é igual ao informado
    return b == num

# Solicita ao usuário para informar um número
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Chama a função e exibe o resultado
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
