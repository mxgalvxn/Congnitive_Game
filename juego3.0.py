import random
def elementos(nivel,num):
    if nivel ==1:
        elementos=[["Aluminio","Al"] ,["Argon","Ar"],["Bario","Ba"],["Berilio","Be"],["Boro","B"],["Bromo","Br"],["Calcio","Ca"],["Carbono","C"] , ["Cesio","Cs"],["Cloro","Cl"],["Cobre","Cu"],["Fluor","F"],["Fosforo","P"],["Francio","Fr"],["Galio","Ga"],["Helio","He"],["Hidrogeno","H"],["Litio","Li"],["Magnesio","Mg"] ,["Mercurio","Hg"],["Neon","Ne"],["Nitrogeno","N"],["Oro","Au"],["Oxigeno","O"],["Plata","Ag"],["Potasio","K"],["Radio","Ra"],["Silicio","Si"], ["Sodio","Na"]]
    else:
        elementos=[["Actinio","Ac"],["Americio","Am"],["Berkelio","Bk"],["Bohrio","Bh"],["Californio","Cf"],["Circonio","Zr"],["Copernicio","Cn"],["Curio","Cm"],["Darmstadtio","Ds"],["Dubnio","Db"],["Einstenio","Es"],["Escandio","Sc"],["Estroncio","Sr"],["Fermio","Fm"],["Flerovio","Fl"],["Hafnio","Hf"],["Hassio","Hs"],["Itrio","Y"],["Kriptón","Kr"],["Lantano","La"],["Laurencio","Lr"],["Livermorio","Lv"],["Meitnerio","Mt"],["Mendelevio","Md"],["Moscovio","Mc"],["Neptunio","Np"],["Nihonio","Nh"],["Niobio","Nb"],["Nobelio","No"],["Oganesón","Og"],["Plutonio","Pu"],["Prometio","Pm"],["Radón","Rn"],["Roentgenio","Rg"],["Rubidio","Rb"],["Rutherfordio","Rf"],["Seaborgio","Sg"],["Tantalio","Ta"],["Tecnecio","Tc"],["Teneso","Ts"],["Titanio","Ti"],["Vanadio","V"],["Xenón","Xe"]]
    return elementos[num]

def preguntas(elemento,simbolo,puntaje,juego,incorrecto):
    
    if juego ==1:
        print("¿Cual es el simbolo quimico del siguiente elemento?")
    elif juego ==2:
         print("¿A que elemento pertenece este simbolo?")
    print(elemento)
    print()
    respuesta=input("Simbolo: ").lower()
    if respuesta == simbolo.lower():
        puntaje+=1
        print("Correcto")
        print()
        print("______________________________________________________")
    else:
        print("Incorrecto")
        print(f"La respuesta era {simbolo}")
        incorrectos(incorrecto,elemento,0)
        print()
        print("______________________________________________________")    
    return puntaje

def incorrectos(incorrecto,elemento,imprimir):
    if imprimir ==0:
        incorrecto.append(elemento)
    else:
        n=0
        for i in range(5):
            for j in range(4):
                n+=1
                if n<=len(incorrecto):
                    print(incorrecto[n-1], end="  ")
                                    
            print()
    return incorrecto       

    
print("""Opcion 1:Aidvinar el simbolo
Opcion 2:Adivinar el elemento
Opcion 3: Modo Random""")
print("Selecciona el tipo de juego: 1,2 o 3")
juego = int(input())        
puntaje=0
vistos=[]
incorrecto=[]
num = random.randint(0,28)
mal=[]
if juego == 1:
    print("Nivel 1")
    print()
    for j in range(2):
        if puntaje>7:
            print("Pasaste al nivel 2")
            print()
            nivel=2
        elif puntaje<7 and j!=1:
                nivel=1
        else:
            break
        for i in range(10):
            while num in vistos:
                num = random.randint(0,28)
            vistos.append(num)
            ele=elementos(nivel,num)
            elemento=ele[0]
            simbolo=ele[1]
            puntaje=preguntas(elemento,simbolo,puntaje,juego,incorrecto)
    incorrecto=incorrectos(incorrecto,"",0)       
elif juego ==2:
    print("Nivel 1")
    print()
    for j in range(2):
        if puntaje>7:
            print("Pasaste al nivel 2")
            print()
            nivel=2
        elif puntaje<7 and j!=1:
                nivel=1
        else:
            break  
        for i in range(10):
            while num in vistos:
                num = random.randint(0,28)
            vistos.append(num)
            ele=elementos(nivel,num)
            elemento=ele[0]
            simbolo=ele[1]
            puntaje=preguntas(simbolo,elemento,puntaje,juego,incorrecto)
    incorrecto=incorrectos(incorrecto,"",0)         
elif juego==3:
    print("Nivel 1")
    print()
    for j in range(2):
        if puntaje>=7:
            print("Pasaste al nivel 2")
            print()
            nivel=2
        elif puntaje<7 and j!=1:
                nivel=1
        else:
            break
        for i in range(10):
            juego=random.randint(1,2)
            while num in vistos:
                num = random.randint(0,28)
            vistos.append(num)
            ele=elementos(nivel,num)
            elemento=ele[0]
            simbolo=ele[1]
            if juego ==1:
                puntaje=preguntas(elemento,simbolo,puntaje,juego,incorrecto)
            else:
                puntaje=preguntas(simbolo,elemento,puntaje,juego,incorrecto)
    incorrecto=incorrectos(incorrecto,"",0)                     
if puntaje>15:
    print("Felicidades ganaste")
    print(f"Tu puntaje es {puntaje}")
    print("Recuerda practicar los siguientes elementos")

    incorrectos(incorrecto," ",1)
else:
    print("Fin del juego")
    print(f"Tu puntaje es {puntaje}")
    print("Recuerda practicar los siguientes elementos")
    incorrectos(incorrecto," ",1)  
    

    