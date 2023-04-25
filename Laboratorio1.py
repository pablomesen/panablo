#Primer ejercicio
def eliminar_impares(num):
    '''Funciòn que recibe un nùmero y lo retorna sin sus digìtos impares'''
    if type(num)!=int:
        return "Error 01"
    elif num<0:
        return "Error 02"
    else:
        return eliminar_impares_aux(num,0,0,0)
def eliminar_impares_aux (num,resultado,indice, potencia):
    '''Funciòn Auxiliar'''
    if num==0:
        return resultado
    elif num%2!=0:
        return eliminar_impares_aux(num//10, resultado, indice+1, potencia)
    else:
        return eliminar_impares_aux(num//10, resultado + (num%10*10**potencia), indice+1, potencia+1)
respuesta1 = eliminar_impares(123456)
print (respuesta1)
#Segundo ejericio
def eliminar_vocales(texto, vocal):
    '''Funcion que elimina todas las apariciones de una vocal en un texto'''
    if type(texto)!=str:
        return "Error 01"
    elif type(vocal)!=str:
        return "Error 02"
    elif len(vocal)!=1:
        return "Error 03"
    elif vocal=="a" or vocal=="e" or vocal=="i" or vocal=="o" or vocal=="u" or vocal=="A" or vocal=="E" or vocal=="I" or vocal=="U" or vocal=="O":
        return eliminar_vocales_aux(texto, vocal, 0, len(texto), "")
    else:
        return "Error 04"
def eliminar_vocales_aux(texto,vocal,indice,largo,resultado):
    '''Función Auxiliar'''
    if indice==largo:
        return resultado
    elif texto[indice]==vocal:
        return eliminar_vocales_aux(texto, vocal, indice+1,largo, resultado)
    else: 
        return eliminar_vocales_aux(texto, vocal, indice+1, largo, resultado+texto[indice])
respuesta2 = eliminar_vocales("Hola mundo", "o")
print (respuesta2)
#Tercer ejercio
def validar_limpiar(lista):
    '''Función que verifica si todos los elementos de una lista son tipo números enteros o flotantes'''
    if type(lista)!=list:
        return "Error 01"
    else:
        return validar_limpiar_aux(lista, 0, len(lista), [])
def validar_limpiar_aux(lista, indice, largo, resultado):
    '''Función auxiliar'''
    if indice==largo:
        return True
    elif type(lista[indice])==int or type(lista[indice])==float:
        return validar_limpiar_aux(lista, indice+1, largo, resultado)
    else:
        return validar_limpiar_secundaria(lista)
def validar_limpiar_secundaria(lista):
    '''Funcion que aplana la lista y elimina las sublistas dentro de esta'''
    if type(lista)!=list:
        return "No es una lista"
    else:
        return validar_limpiar_secundaria_aux(lista, 0, len(lista), [])
def validar_limpiar_secundaria_aux (lista, indice, largo, resultado):
    '''Función Auxiliar'''
    if indice==largo:
        return resultado
    elif type(lista[indice])!=list:
        return validar_limpiar_secundaria_aux (lista, indice+1, largo, resultado+[lista[indice]])
    else: 
        return validar_limpiar_secundaria_aux (lista, indice+1, largo, resultado)
respuesta3 = validar_limpiar([1,2,3,[4]])
print (respuesta3)
#Cuarto ejercicio
def aplanar_lista_1(lista):
    '''Función que aplana una lista si es que esta cuenta con sublistas dentro de ella'''
    if type(lista)!=list:
        return "Error 01"
    elif len(lista)<=1:
        return lista
    else: 
        return aplanar_lista_1_aux(lista, 0, len(lista), [])
def aplanar_lista_1_aux(lista, indice, largo, resultado):
    '''Función Auxiliar'''
    print
    if indice==largo:
        return resultado
    elif type(lista[indice])==list:
        return aplanar_lista_1_aux(lista, indice+1, largo, resultado+ lista[indice])
    else:
        return aplanar_lista_1_aux(lista, indice+1, largo, resultado+[lista[indice]])
respuesta4 = aplanar_lista_1([1,2,3,[4,5]])
print (respuesta4)
#Quinto ejercicio
def aplanar_lista(lista):
    '''Función que aplana una lista si es que esta cuenta con sublistas dentro de ella'''
    if type(lista)!=list:
        return "Error 01"
    elif len(lista)<=1:
        return lista
    else: 
        return aplanar_lista_aux(lista, 0, len(lista), [])
def aplanar_lista_aux(lista, indice, largo, resultado):
    '''Función Auxiliar'''
    print
    if indice==largo:
        return resultado
    elif type(lista[indice])==list:
        return aplanar_lista_aux (lista, indice+1, largo, resultado+aplanar_lista_aux(lista[indice], 0, len(lista[indice]), []))
    else:
        return aplanar_lista_aux(lista, indice+1, largo, resultado+[lista[indice]])
respuesta5 = aplanar_lista([1,2,3,[4,5],[6,7]])
print (respuesta5)
#Sexto ejercicio
def registrar_persona(lista, nombre, edad, universidad):
    '''Función que mete la información de una persona dentro de una lista'''
    if type(nombre)!=str:
        return "Error 01"
    elif type(edad)!=int:
        return "Error 02"
    elif edad < 0:
        return "Error 03"
    elif type(universidad)!=str:
        return "Error 04"
    elif len(universidad)!=3:
        return "Error 05"
    else:
        return registrar_persona_aux(lista, nombre, edad, universidad)
def registrar_persona_aux(lista, nombre, edad, universidad):
    '''Funcion Auxiliar'''
    return [lista] + [[nombre, edad, universidad]]
respuesta6 = registrar_persona(["Pablo", 17, "TEC"], "Hilary", 17, "UCR")
print(respuesta6)
#----------------------------------------------------------------------------------------------------------------------------------------


