soma=0
count=0
sair='S'
maior=0
menor=0
while sair=='S':
    n=int(input('digite um numero..:'))
    soma+=n
    count+=1
    if count==1:
        menor=n
        maior=n
    if n>maior:
        maior=n
    if n<menor:
        menor=n        
    sair=input('\nquer continuar? ').upper()
print('\nmedia dos valores lidos..:{}'.format(soma/count))
print('maior valor..:{}'.format(maior))   
print('menor valor...:{}'.format(menor)) 