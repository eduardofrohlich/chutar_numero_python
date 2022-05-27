import random

def gerar():
    return random.randint(0, 100)

def fim_jogo():
    print('-- FIM DE JOGO --')
    exit()

def perguntar():
    pergunta = input(f'\nDeseja continuar o jogo?(s/n) ')
    if pergunta == 's':
        adivinhar()
    if pergunta == 'n':
        fim_jogo()
        # print('\n--FIM DE JOGO--')
        #     break
    else:
        print('Ei, seu vacilão, digite apenas "s" ou "n", não sabe ler?')
        perguntar()



def adivinhar():
    resposta = gerar()
    tentativas = 0
    chute = 0
    print('\n-- JOGO INICIADO, SEU NÚMERO FOI GERADO! CHUTE DE 0 A 100 --')

    while chute is not resposta:
        try:
            tentativas += 1
            chute = int(input('Adivinhe o número: '))
            if chute < 0:
                print('\nO número deve ser maior ou igual a 0.')
                continue

            elif chute > 100:
                print('\nO número deve ser menor ou igual a 100.')
                continue

            if chute < resposta:
                print('\nResposta incorreta, o número é maior. Tente novamente.')

            elif chute > resposta:
                print('\nResposta incorreta, o número é menor. Tente novamente.')

            else:
                print('\nParabéns, você acertou! O número é {}. Acertou em {} tentativas.'.format(resposta, tentativas))
                perguntar()
        except ValueError:
            print('\nDIGITE APENAS NÚMEROS')


            # def perguntar():
            #         pergunta = input(f'\nDeseja continuar o jogo?(s/n) ')
            #         if pergunta == 's':
            #            adivinhar()
            #         if pergunta == 'n':
            #             print('\n--FIM DE JOGO--')

if __name__ == '__main__':
    adivinhar()
# while True:
#     adivinhar()
# while True:
#     perguntar()
# def fim_jogo():
#     print('Jogo encerrado')
#
# while perguntar() == 1:
#     fim_jogo()
# while perguntar() == 0:
#     adivinhar()