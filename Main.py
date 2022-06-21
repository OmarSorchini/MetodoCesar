#Situacion Problema I.2 
#Autores: Iris Camp Mussa - A01750477 y Omar Rodrigo Sorchini Puente - A01749389

import matplotlib.pyplot as plt
import numpy as np

abc = "abcdefghijklmnopqrstuvwxyz"
tabEstandar = [12.53,1.42,4.68,5.86,13.68,0.69,1.01,0.70,6.25,0.44,0.02,4.97,3.15,6.71,8.68,2.51,0.88,6.87,7.98,4.63,3.93,0.90,0.01,0.22,0.90,0.52]

def grafTabEst():
    plt.title("Tabla de frecuencias estándar")
    plt.bar(range(26),tabEstandar)
    plt.xlabel("Letras")
    plt.ylabel("Porcentajes")
    plt.xticks(range(27),["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"])
    plt.yticks(np.arange(0,15,step = 2),["0%","2%","4%","6%","8%","10%","12%","14%"])
    plt.savefig("TablaEstandar.png")

def let2int(c):
    num = abc.index(c)
    return num

def int2let(n):
    let = abc[n%len(abc)]
    return let

def shift(n,c):
    num = let2int(c) + n
    let = int2let(num)
    return let

def encode(n,c):
    code = ""
    c = c.lower()
    for i in c:
        if i not in abc:
            code += i
        else:
            code += shift(n,i)
    return code

def getkey(frase):
    frase = frase.lower()
    letras = ""
    vec = []
    for i in frase:
        if i not in " ":
            if i not in letras:
                letras += i
                vec.append(frase.count(i))
        
    letMax = max(vec)
    pos = vec.index(letMax)
    let = letras[int(pos)]
    posABC = let2int(let)
    return posABC
    
def crack1(frase):
    key = 4-getkey(frase)
    code = encode(key,frase)
    return code

def crack2(frase,let):
    key = let2int(let)-getkey(frase)
    code = encode(key,frase)
    return code

def frag_table(texto):
    texto2 = ""
    apar = []
    for i in texto:
        if i in abc:
            texto2 += i
    for j in abc:
        apar.append(texto2.count(j)/len(texto2)*100)
    return apar


#####Bloque para chi cuadrada
def chsqr(lista1,lista2):
    chi = 0
    conta = 0
    listaTot = unirListas(lista1,lista2)
    sumaFil1,sumaFil2,sumaFils = sumarFilas(lista1,lista2)
    frecTeo1,frecTeo2 = frecTeor(lista1,lista2,sumaFil1,sumaFil2,sumaFils)
    frecTot = unirListas(frecTeo1,frecTeo2)
    
    for i in listaTot:
        chi += ((i-frecTot[conta])**2)/frecTot[conta]
        conta += 1
    return chi
    
    
def unirListas(lista1,lista2):
    listaTot = []
    conta = 0
    
    for x in lista1:
        listaTot.append(x)
        conta += 1
    conta = 0
    for y in lista2:
        listaTot.append(y)
        conta += 1
    conta = 0
    
    return listaTot

def sumarFilas(lista1,lista2):
    sumaFil1 = 0
    sumaFil2 = 0
    
    for j in lista1:
        sumaFil1 += j
    for k in lista2:
        sumaFil2 += k
        
    sumaFils = sumaFil1 + sumaFil2
    return sumaFil1,sumaFil2,sumaFils

def frecTeor(lista1,lista2,sumaFil1,sumaFil2,sumaFils):
    
    frecTeo1 = []
    frecTeo2 = []
    conta = 0

    for a in lista1:
        frec = ((a+lista2[conta])*sumaFil1)/sumaFils
        frecTeo1.append(frec)
        conta += 1
    conta = 0
        
    for b in lista2:
        frec = ((b+lista1[conta])*sumaFil2)/sumaFils
        frecTeo2.append(frec)
        conta += 1
        
    return frecTeo1,frecTeo2
#####Bloque para chi cuadrada

def crack(frase):
    encript = []
    key = []
    valMin = 100
    for i in range(26):
        encript.append(encode(i,frase))

    for j in range(26):
        key.append(chsqr(frag_table(encript[j]),tabEstandar))
        
    for k in key:
        if k < valMin:
            valMin = k
    pos = key.index(valMin)
    desencrip = encode(pos,frase)
    return desencrip
    
crack('fyirsw hmew iwxvippmxe pe xmivve hi psw ipjsw qmwxmgsw xi hmgi lspe')

input("Click enter para cerrar")