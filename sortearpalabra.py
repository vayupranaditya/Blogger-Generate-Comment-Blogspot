import random
#Busca la palabra en la lista, si esta devuelve la poscicion, si no False
def coincidencia(palabra,dic):
    coincidencia = False
    pos = 0
    while pos < len(dic[0]) and not(coincidencia):
        if dic[0][pos] == palabra: #Si el texto es igual a un numero lo devuelvo
            return (pos+1)
        pos = pos + 1
    return coincidencia  #Si no esta la palabra devuelve false
	
#Agrega la palabra al diccionario o aumenta las aparicioes en caso que ya este
def agregar(palabra,dic):
    pos = coincidencia(palabra,dic) 
    if not(pos):
        dic[0].append(palabra)
        dic[1].append(1)
    else:  
        dic[1][pos-1] = dic[1][pos-1] + 1
    return dic

def creardiccionario(palabra,texto):
    dic = [[],[]]
    apariciones = 0
    for i in range(0,len(texto)-1):
        if palabra == texto[i]:
            dic = agregar(texto[i+1],dic)
            apariciones = apariciones + 1
    #Halla probabilidad condicional de cada palabra
    for i in range(0,len(dic[1])):
        dic[1][i] = dic[1][i]/apariciones
    return dic

def sortear_palabra(palabra,text):
    dic = creardiccionario(palabra,text)
    dic = random.choices(dic[0],dic[1])
    return dic

def generar_texto(palabra,text,largo):
    texto = palabra
    for i in range(0,largo):
        palabra = sortear_palabra(palabra,text)[0]
        texto = texto + " " + palabra
    return texto
