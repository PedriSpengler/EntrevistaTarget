# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

conta = 0
contA = 0

def verificaA(stringe):
    global conta, contA
    for i in range(len(stringe)):
        if stringe[i] == 'a':
            conta+=1
        if stringe[i] == 'A':
            contA+=1


stringe = str(input("Informe uma string para verificar se há ou não presença de 'a' e 'A':"))

verificaA(stringe)

print(f"O número de 'a' encontrado foi de: {conta}")
print(f"O número de 'A' encontrado foi de: {contA}")        