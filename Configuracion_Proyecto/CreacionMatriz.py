import random

def configuracion():
    sopa = []
    contador = 0
    tamano_sopa = int(input("Ingrese un numero, para el tamaño de la sopa de letras: "))
    abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    palabras_sopa = open('palabras.txt')
    palabras = []
    for p in palabras_sopa:
        palabras.append(p.strip().upper())
    palabras_random = []
    while contador < tamano_sopa - 1:
        palabra_random = palabras[random.randint(0, 99)]
        if len(palabra_random) < tamano_sopa and palabra_random not in palabras_random:
            palabras_random.append(palabra_random)
            contador += 1
    print(f'Busca las siguientes palabras: {", ".join(palabras_random)}')
    for i in range(tamano_sopa):
        sopa.append([])
        for e in range(tamano_sopa):
            sopa[i].append(abecedario[random.randint(0, 25)])
    for i in sopa:
        for j in i:
            print(j,end = " ")
        print()
configuracion()




