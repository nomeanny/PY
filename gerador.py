#Como criar um gerador
def contador(max):
    """Um gerador que conta até um número m´qximo."""
    contador = 1
    while contador <= max:
        yield contador #Pausa a função e retorna o valor
        contador += 1 #Retoma a execução na próxima chamada
    
#Criando o gerador
meu_contador = contador(5)

#Iterando sobre os valores gerados
for numero in meu_contador:
    print(numero)