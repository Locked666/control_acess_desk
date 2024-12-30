import random

def gerador_numeros(quantidade,x):
    n = []
    for i in range(x):
        numeros = [random.randint(0, 100) for _ in range(quantidade)]
        n.append(numeros)
    return n


if __name__ == "__main__":
    quantidade = int(input("Digite a quantidade de números a serem gerados: "))
    numeros_gerados = gerador_numeros(quantidade,3)
    print("Números gerados:", numeros_gerados)