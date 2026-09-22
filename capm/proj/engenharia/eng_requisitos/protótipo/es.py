import sys
import os
import time

def tela_entrada():
    while True:
        os.system('cls')
        print('\nBem vindo ao módulo CAPM\n')
        print('\nVocê pode calcular as seguintes opções: alfa de Jensen e beta\n')
        grandeza = input("Digite 'a' para alfa e 'b' para beta e 'x' para encerrar\n")

        if grandeza == 'a':
            print('Você quer calcular o alfa')
            break
        elif grandeza == 'b':
            print('Você quer calcular o beta')
            break
        elif grandeza.upper() == 'X':
            print('Você pediu para encerrar. Muito obrigado por usar nossa aplicação')
            break
        else:
            print('Você não digitou uma alternativa válida. Tente novamente')
            time.sleep(5)

    sys.exit()


