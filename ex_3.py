sair=False
n1=int(input('informe o primeiro numero..:'))
n2=int(input('informe o segundo numero..:'))

while sair==False:
    opcao=int(input('''    1- somar
    2- multiplicar
    3- maior
    4- novos numeros
    5- sair do programa
    informe a opcao desejada-->'''))
    if opcao==1:
        som=n1+n2
        print('{} + {} = {}'.format(n1,n2,som))
    elif opcao==2:
        mult=n1*n2
        print("{} x {} = {}".format(n1,n2,mult))
    elif opcao==3:
        if n1>n2:
            maior=n1
            print('maior valor é: {}'.format(maior))
        if n2>n1:
            maior=n2
            print('maior valor é: {}'.format(maior))
    elif opcao==4:
        print('informe novos numeros...')
        n1=int(input('informe o primeiro numero'))
        n2=int(input('informe o segundo numero'))
    elif opcao==5:
        print('saindo...')
        sair=True       
    else:
        print('opcão invalida !!!')