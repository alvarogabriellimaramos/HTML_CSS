from random import randint 
nome = str(input('Digite seu nome - '))
print(f'Olá {nome},bem vindo ao jogo da advinhação')
print('-'*10)
print('Tente advinha o numero que o computador (de 1 até 10 ) pensou,Você terá cinco tentativas para acertar ')
lista = [1,2,3,4,5,6,7,8,9,10]
def jogo():
    for cont in range(1,6):
        computador = randint(1,10)
        print(computador)
        try:
            usuario = int(input('Digite um numero - '))
        except:
            print('Valor Invalido ')
        else:
            if usuario == computador:
                print('Você aCERTOU!!!')
                print('-'*10)
                print('Você Ganhou mais 6 tentativas ')
                jogo() 
print(jogo())
