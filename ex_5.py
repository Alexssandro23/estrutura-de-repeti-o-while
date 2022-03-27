sair=0
count=0
while sair!=999:  
    sair=int(input("digite 999 para sair..:"))
    if sair!=999:
        count+=1

print("fim...")
print("numeros digitados..:{}".format(count))