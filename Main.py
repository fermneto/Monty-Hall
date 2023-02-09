

###Importa a biblioteca do random###


import random


###Criação das listas nescessárias###


num = [1, 2, 3]
fn = [1, 2, 3]
pn = [1, 2, 3]


###Escolhe a porta correta e à deleta da lista fn###


xx = random.randint(0,2)
crt = num[xx]
del fn[xx]


###Escolhe a porta do usuário###


pe1 = int(input('Qual porta você acha que é a certa? '))
print()


###Caso em que a porta escolhida é a correta###


if pe1 == crt  :
    del fn[random.randint(0,1)]                                 ###Remove uma porta errada da lista, sobrando apenas uma(errada)###
    pn.remove(fn[0])                                            ###Utiliza a unica porta (errada) da lista fn e à remove###
    print('A porta', fn[0],'não é a certa')
    print('Ainda restam as portas', pn[0],'e',pn[1])            ###Mostra as portas restantes###
    print()
    pe2 = int(input('Qual porta deseja escolher? '))            ###Escolhe a porta final###
    print()
    
    if pe2 == crt :                                             ###Informa o resultado###
        print('Você ganhou, a porta certa era a',crt)
    else :
        print('Você perdeu, a porta certa era a',crt)


###Caso em que a porta escolhida não é a correta###


else :
    fn.remove(pe1)                                              ###Remove a porta escolhida da lista, sobrando apenas uma(errada)###
    pn.remove(fn[0])                                            ###Utiliza a unica porta (errada) da lista fn e à remove###
    print('A porta', fn[0],'não é a certa')
    print('Ainda restam as portas', pn[0],'e',pn[1])            ###Mostra as portas restantes###
    print()
    pe2 = int(input('Qual porta deseja escolher? '))            ###Escolhe a porta final###
    print()
    
    if pe2 == crt :                                             ###Informa o resultado###
        print('Você ganhou, a porta certa era a',crt)
    else :
        print('Você perdeu, a porta certa era a',crt)
