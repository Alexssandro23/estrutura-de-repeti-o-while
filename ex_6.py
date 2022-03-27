count=0
sair=0
som=0
while sair!=999:
    n=int(input('digite um número...:'))    
    if sair!=999:
        som+=n
        count+=1
    sair=int(input('digite qualquer valor diferente de 999 para continuar?....:'))
print('total de numeros digitados--> {}'.format(count))
print('soma dos numeros digitados--> {}'.format(som))