from random import randint
print("BIENVENIDO AL CAMPEONATO DE CICLISMO")
#---------------Matriz 1

comp1=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas1=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz1 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz1.append(a)
    for j in range(10):
        matriz1[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp1[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas1[i]+"|\t"
    for j in range(10):
        cad+=str(matriz1[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo1 = 100
cadena1 = "Tiempo1:\t\t"
for j in range(10):
        sumacolumna1 = 0
        for i in range(5):
                sumacolumna1 = sumacolumna1 + matriz1[i][j]
        if sumacolumna1 < tiempo1:
                tiempo1 = sumacolumna1
                competidor1 = comp1[j]
        cadena1+=str(sumacolumna1)+"\t"
print(cadena1+"\nCompetidor que gano en la etapa 1 es: "+ competidor1)
#----------------Matriz 2

comp2=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas2=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz2 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz2.append(a)
    for j in range(10):
        matriz2[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp2[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas2[i]+"|\t"
    for j in range(10):
        cad+=str(matriz2[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo2 = 100
cadena2 = "Tiempo2:\t\t"
for j in range(10):
        sumacolumna2 = 0
        for i in range(5):
                sumacolumna2 = sumacolumna2 + matriz2[i][j]
        if sumacolumna2 < tiempo2:
                tiempo2 = sumacolumna2
                competidor2 = comp2[j]
        cadena2+=str(sumacolumna2)+"\t"
print(cadena2+"\nCompetidor que gano en la etapa 2 es: "+ competidor2)
#----------------Matriz 3

comp3=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas3=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz3 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz3.append(a)
    for j in range(10):
        matriz3[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp3[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas3[i]+"|\t"
    for j in range(10):
        cad+=str(matriz3[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo3 = 100
cadena3 = "Tiempo3:\t\t"
for j in range(10):
        sumacolumna3 = 0
        for i in range(5):
                sumacolumna3 = sumacolumna3 + matriz3[i][j]
        if sumacolumna3 < tiempo3:
                tiempo3 = sumacolumna3
                competidor3 = comp3[j]
        cadena3+=str(sumacolumna3)+"\t"
print(cadena3+"\nCompetidor que gano en la etapa 3 es: "+ competidor3)
#----------------Matriz 4

comp4=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas4=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz4 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz4.append(a)
    for j in range(10):
        matriz4[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp4[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas4[i]+"|\t"
    for j in range(10):
        cad+=str(matriz4[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo4 = 100
cadena4 = "Tiempo4:\t\t"
for j in range(10):
        sumacolumna4 = 0
        for i in range(5):
                sumacolumna4 = sumacolumna4 + matriz4[i][j]
        if sumacolumna4 < tiempo4:
                tiempo4 = sumacolumna4
                competidor4 = comp4[j]
        cadena4+=str(sumacolumna4)+"\t"
print(cadena4+"\nCompetidor que gano en la etapa 4 es: "+ competidor4)
#----------------Matriz 5

comp5=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas5=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz5 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz5.append(a)
    for j in range(10):
        matriz5[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp5[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas5[i]+"|\t"
    for j in range(10):
        cad+=str(matriz5[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo5 = 100
cadena5 = "Tiempo5:\t\t"
for j in range(10):
        sumacolumna5 = 0
        for i in range(5):
                sumacolumna5 = sumacolumna5 + matriz5[i][j]
        if sumacolumna5 < tiempo5:
                tiempo5 = sumacolumna5
                competidor5 = comp5[j]
        cadena5+=str(sumacolumna5)+"\t"
print(cadena5+"\nCompetidor que gano en la etapa 5 es: "+ competidor5)
#----------------Matriz 6

comp6=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas6=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz6 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz6.append(a)
    for j in range(10):
        matriz6[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp6[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas6[i]+"|\t"
    for j in range(10):
        cad+=str(matriz6[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo6 = 100
cadena6 = "Tiempo6:\t\t"
for j in range(10):
        sumacolumna6 = 0
        for i in range(5):
                sumacolumna6 = sumacolumna6 + matriz6[i][j]
        if sumacolumna6 < tiempo6:
                tiempo6 = sumacolumna6
                competidor6 = comp6[j]
        cadena6+=str(sumacolumna6)+"\t"
print(cadena6+"\nCompetidor que gano en la etapa 6 es: "+ competidor6)
#----------------Matriz 7
comp7=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas7=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz7 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz7.append(a)
    for j in range(10):
        matriz7[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp7[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas7[i]+"|\t"
    for j in range(10):
        cad+=str(matriz7[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo7 = 100
cadena7 = "Tiempo7:\t\t"
for j in range(10):
        sumacolumna7 = 0
        for i in range(5):
                sumacolumna7 = sumacolumna7 + matriz7[i][j]
        if sumacolumna7 < tiempo7:
                tiempo7 = sumacolumna7
                competidor7 = comp7[j]
        cadena7+=str(sumacolumna7)+"\t"
print(cadena7+"\nCompetidor que gano en la etapa 7 es: "+ competidor7)
#----------------Matriz 8

comp8=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas8=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz8 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz8.append(a)
    for j in range(10):
        matriz8[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp8[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas8[i]+"|\t"
    for j in range(10):
        cad+=str(matriz8[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo8 = 100
cadena8 = "Tiempo8:\t\t"
for j in range(10):
        sumacolumna8 = 0
        for i in range(5):
                sumacolumna8 = sumacolumna8 + matriz8[i][j]
        if sumacolumna8 < tiempo8:
                tiempo8 = sumacolumna8
                competidor8 = comp8[j]
        cadena8+=str(sumacolumna8)+"\t"
print(cadena8+"\nCompetidor que gano en la etapa 8 es: "+ competidor8)
#----------------Matriz 9

comp9=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas9=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz9 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz9.append(a)
    for j in range(10):
        matriz9[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp9[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas9[i]+"|\t"
    for j in range(10):
        cad+=str(matriz9[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo9 = 100
cadena9 = "Tiempo9:\t\t"
for j in range(10):
        sumacolumna9 = 0
        for i in range(5):
                sumacolumna9 = sumacolumna9 + matriz9[i][j]
        if sumacolumna9 < tiempo9:
                tiempo9 = sumacolumna9
                competidor9 = comp9[j]
        cadena9+=str(sumacolumna9)+"\t"
print(cadena9+"\nCompetidor que gano en la etapa 9 es: "+ competidor9)
#----------------Matriz 10
comp10=["Com 1","Com 2","Com 3","Com 4","Com 5","Com 6","Com 7","Com 8","Com 9","Com 10",]
etapas10=["Etapa 1: ","Etapa 2: ","Etapa 3: ","Etapa 4: ","Etapa 5: "]
matriz10 = []
#Generamos el tiempo aleatorio para los competidores
for i in range(5):
    a=[0]*10
    matriz10.append(a)
    for j in range(10):
        matriz10[i][j] = randint(0,20)
#Cabecera
cad2="          "
for i in range(10):
    cad2+="\t"+comp10[i]
cad2+="\n\t\t----------------------------------------------"
print(cad2)
for i in range(5):
    cad=etapas10[i]+"|\t"
    for j in range(10):
        cad+=str(matriz10[i][j])+"\t"
    print(cad)
print("\n\t\t----------------------------------------------")
tiempo10 = 100
cadena10 = "Tiempo10:\t\t"
for j in range(10):
        sumacolumna10 = 0
        for i in range(5):
                sumacolumna10 = sumacolumna10 + matriz10[i][j]
        if sumacolumna10 < tiempo10:
                tiempo10 = sumacolumna10
                competidor10 = comp10[j]
        cadena10+=str(sumacolumna10)+"\t"
print(cadena10+"\nCompetidor que gano en la etapa 10 es: "+ competidor10)
print()