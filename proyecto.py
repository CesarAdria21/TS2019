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
cadena1 = "Tiempo:\t\t"
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
cadena2 = "Tiempo:\t\t"
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
cadena3 = "Tiempo:\t\t"
for j in range(10):
        sumacolumna3 = 0
        for i in range(5):
                sumacolumna3 = sumacolumna3 + matriz3[i][j]
        if sumacolumna3 < tiempo3:
                tiempo3 = sumacolumna3
                competidor3 = comp3[j]
        cadena3+=str(sumacolumna3)+"\t"
print(cadena3+"\nCompetidor que gano en la etapa 2 es: "+ competidor3)
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
cadena4 = "Tiempo:\t\t"
for j in range(10):
        sumacolumna4 = 0
        for i in range(5):
                sumacolumna4 = sumacolumna4 + matriz4[i][j]
        if sumacolumna4 < tiempo4:
                tiempo4 = sumacolumna4
                competidor4 = comp4[j]
        cadena4+=str(sumacolumna4)+"\t"
print(cadena4+"\nCompetidor que gano en la etapa 2 es: "+ competidor4)
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
cadena5 = "Tiempo:\t\t"
for j in range(10):
        sumacolumna5 = 0
        for i in range(5):
                sumacolumna5 = sumacolumna5 + matriz5[i][j]
        if sumacolumna5 < tiempo5:
                tiempo5 = sumacolumna5
                competidor5 = comp5[j]
        cadena5+=str(sumacolumna5)+"\t"
print(cadena5+"\nCompetidor que gano en la etapa 2 es: "+ competidor5)
#----------------Matriz 6
#----------------Matriz 7
#----------------Matriz 8
#----------------Matriz 9
#----------------Matriz 10