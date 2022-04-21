import random

# Variáveis
rows = []
m = 0
n = 0
final_row = []

"""

--> MATRIZ MENSAGEM: MATRIZ CONTENDO A MENSAGEM A 
SER CRIPTOGRAFADA

***ATENÇÃO*** NÃO USE NÚMEROS NA MATRIZ MENSAGEM, POIS OS
ELEMENTOS DA MATRIZ MENSAGEM SERÃO AUTOMÁTICAMENTE TRANSFORMADOS
EM NÚMEROS COM A TABELA ALFA-NUMÉRICA! DIGITE SOMENTE A
MENSAGEM A SER CRIPTOGRAFADA, LETRA POR LETRA COM ESPAÇOS.

EXEMPLO: A MENSAGEM É "HACKEANDO GA"; PARA COLOCÁ-LA NO
PROGRAMA, CRIE UMA MATRIZ COM TAMANHO I*J DEFINIDO POR VOCÊ
E DIGITE A MENSAGEM. SE A MATRIZ FOR 2*6, POR EXEMPLO:

|H A C K E A|
|N D O # G A|

PERCEBA QUE O ESPAÇO ENTRE PALAVRAS É EQUIVALENTE À "#"

"""


# Tradução Matriz Mensagem para tabela alfa-numérica
def to_alfa_n(l):
    mAlfa = []
    mAlfa_row = []
    alfa_n = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,        
        "f": 6,        
        "g": 7,        
        "h": 8,        
        "i": 9,        
        "j": 10,        
        "k": 11,        
        "l": 12,        
        "m": 13,        
        "n": 14,        
        "o": 15,        
        "p": 16,        
        "q": 17,        
        "r": 18,        
        "s": 19,        
        "t": 20,        
        "u": 21,        
        "v": 22,        
        "w": 23,        
        "x": 24,        
        "y": 25,        
        "z": 26,        
        ".": 27,
        "!": 28,
        "#": 29,
        "-": 30
    }
    try:
        for _ in range(len(l)):
            for a in l[_]:
                n = int(alfa_n.get(a))
                mAlfa_row.append(n)
            mAlfa.append(mAlfa_row)
            mAlfa_row = []
        return mAlfa
    except TypeError:
        print("ERRO: Digite somente letras na matriz codificadora!")
    return "ERROR"


# Função que pega números aleatórios
def randomness(i):
    random_k = []
    random_k_row = []
    n = i**2
    for a in range(i):
        for _ in range(i):
            random_n = (random.random()+random.random())*random.random()
            random_n = "{:.2f}".format(random_n)
            random_n = float(random_n)*100
            random_n = int(random_n)
            random_k_row.append(random_n)
        random_k.append(random_k_row)
        random_k_row = []
    return random_k


# Função que multiplica matrizes
def somatorio(a, b, k1, k2):
    s = 0
    for n in range(len(a[0])):
        s += int(a[k1][n])*int(b[n][k2])
    return s

def matrix_X(a, b):
    sum = []
    sum_row = []
    for k1 in range(len(a)):
        for k2 in range(len(b[0])):
            sum_row.append(somatorio(a, b, k1, k2))
            sum.append(sum_row)
            sum_row = []
    return sum


i = input("\nTamanho da matriz mensagem: ").split()
print("-"*(int(i[1])+10))
for _ in range(int(i[0])):
    row = input(f"linha {_}: ").split()
    if len(row) == int(i[1]):
        rows.append(row)
    else:
        print("\nNúmero de colunas incorreto!\n")
        break
print("-"*(int(i[1])+10))

mA_n = to_alfa_n(rows)
if type(mA_n) == list and mA_n != []:
    print("\nSua matriz em alfa-numérico:")
    print("-"*2*len(mA_n[0]))
    for _ in range(len(mA_n)):
        for a in mA_n[_]:
            print(a, end = " ")
        print("")
    print("-"*2*len(mA_n[0]))
    a = input("\nGerar matriz codificadora aleatória? Digite S ou N: ")
    if a == "S":
        random_k = randomness(int(i[0]))
        print("\n\nSua matriz codificadora aleatória: ***IMPORTANTE***")
        print("-"*2*len(random_k))
        for _ in range(len(random_k)):
            for a in random_k[_]:
                print(a, end = " ")
            print("")
        print("-"*2*len(random_k))

        mCript = matrix_X(random_k, mA_n)
        mCriptografada = []
        t = 0
        e = 0
        while t<=int(i[0])*int(i[1]):
            if final_row == []:
                pass
            else:
                mCriptografada.append(final_row)
                final_row = []
                e = 0
                if t == int(i[0])*int(i[1]):
                    break
                else:
                    pass
            while e<(int(i[0])*int(i[1])/len(mA_n)) and t<int(i[0])*int(i[1]):
                final_row.append(mCript[t][0])
                e += 1
                t += 1

        print("\nSua mensagem criptografada está pronta e está logo abaixo!:")
        print("-"*2*len(mCriptografada))
        for _ in range(len(mCriptografada)):
            for a in mCriptografada[_]:
                print(a, end = " ")
            print("")
        print("-"*2*len(mCriptografada))
        print(" \n\nATENÇÃO: GUARDE SUA MATRIZ CODIFICADORA ALEATÓRIA!")
    elif a == "N":
        print(f"Digite sua matriz codificadora: (DIMENSÕES: {i[0]}x{i[0]}, ENTRADAS: NÚMEROS)")
        codificador = []
        for a in range(int(i[0])):
            cod_row = []
            cod_row = input(f"Linha {a}: ").split()
            try:
                cod_row = [int(x) for x in cod_row]
                codificador.append(cod_row)
                cod_row = []
            except:
                print("Digite apenas números na matriz codificadora")
        print("\nS\nua matriz codificadora:\n")
        print("-"*2*len(codificador))
        for _ in range(len(codificador)):
            for a in codificador[_]:
                print(a, end = " ")
            print("\n")
        print("-"*2*len(codificador))

        mCript = matrix_X(codificador, mA_n)
        mCriptografada = []
        t = 0
        e = 0
        while t<=int(i[0])*int(i[1]):
            if final_row == []:
                pass
            else:
                mCriptografada.append(final_row)
                final_row = []
                e = 0
                if t == int(i[0])*int(i[1]):
                    break
                else:
                    pass
            while e<(int(i[0])*int(i[1])/len(mA_n)) and t<int(i[0])*int(i[1]):
                final_row.append(mCript[t][0])
                e += 1
                t += 1

        print("\nSua mensagem criptografada está pronta!:\n")
        print("-"*2*len(mCriptografada))
        for _ in range(len(mCriptografada)):
            for a in mCriptografada[_]:
                print(a, end = " ")
            print("")
        print("-"*2*len(mCriptografada))
else:
    pass    
