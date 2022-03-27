# x= False
# while x == False :    
#     sexo=input("informe seu sexo: ").upper()
#     if sexo=='M':
#         x=True
#     elif sexo=='F':
#         x=True
#     else:
#         print("digite novamente !!!")    
        
#print("concluido !!!")
    
#curso em video


sexo=str(input('sexo [M/F]:')).upper().strip()[0]
while sexo not in "FM":
    sexo=str(input('digite um valor valido..:')).upper()
print('sexo {} cadastrado com sucesso !!!'.format(sexo))