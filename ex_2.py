from random import randint
from time import sleep

# computador=randint(0,10)
# print(computador)
# tentativas=0
# n=-1
# while computador!=n:
#     n=int(input("digite um numero entre 0 e 10 --> "))
#     if n==computador:
#         sleep(2)
#         print("acertou !!!")
#         tentativas+=1
#     else:
#         sleep(2)
#         print('tente novamente !!!')
#         sleep(2)
#         tentativas+=1
# print('numero de tentativas {}'.format(tentativas))

#c_v
count=0
computador=randint(0,10)
print(computador)
acertou=False

while not acertou:
    eu=int(input('tente adivinhar o  numero que o computador escolheu..:'))
    count+=1    
    if eu==computador:
        acertou=True
    else:
        if eu>computador:
            print('menos !!!')
        elif eu<computador:
            print('mais')  
print('parabéns, voçê acertou com {} palpites'.format(count))        