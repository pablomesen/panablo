#Ejercicio número 1------------------------------------------------------------------------------------------
def eliminar_elemento(elemento, lista):
    '''Funcion que elimina un elemento dado de una lista por lo que retorna la lista sin ese elemento'''
    if type(lista)!=list:
        return "Error 01"
    else:
        return eliminar_elemento_aux(elemento, lista, 0, len(lista), [])
    
def eliminar_elemento_aux(elemento, lista, indice, largo, respuesta):
    '''Funcion Auxiliar'''
    if indice==largo:
        return respuesta
    elif lista[indice]==elemento:
        return eliminar_elemento_aux(elemento, lista, indice+1, largo, respuesta)
    else:
        return eliminar_elemento_aux(elemento, lista, indice+1, largo, respuesta + [lista[indice]])
    
print ("La respuesta del ejercicio 1 es: ")
respuesta1 = eliminar_elemento("Hola", [1,2,"Hola",3])
print (respuesta1)

#Ejercicio número 2------------------------------------------------------------------------------------------
def contar_pares(lista):
    '''Funcion que cuenta la cantidad de pares que hay en una lista'''
    if type(lista)!=list:
        return "Error 01"
    elif lista==[]:
        return 0 
    elif verificar_elementos(lista)==False:
        return "Error 02"
    else:
        return contar_pares_aux(lista, 0, len(lista), 0)
def contar_pares_aux(lista, indice, largo, respuesta):
    '''Funcion Auxiliar'''
    if indice==largo:
        return respuesta
    elif lista[indice]%2 == 0:
        return contar_pares_aux(lista, indice+1, largo, respuesta+1)
    else:
        return contar_pares_aux(lista, indice+1, largo, respuesta)
def verificar_elementos(lista):
    '''Funcion que verifica que todos los elementos de una lista sean numeros'''
    if type(lista)!=list:
        return "Error 03"
    else:
        return verificar_elementos_aux(lista, 0, len(lista))
def verificar_elementos_aux(lista, indice, largo):
    '''Funcion Auxiliar'''
    if indice==largo:
        return True 
    elif type(lista[indice])!=int:
        return False
    else:
        return verificar_elementos_aux(lista, indice+1, largo)
    
print ("La respuesta del ejercicio 2 es: ")
respuesta2 = contar_pares([3,5,7])
print (respuesta2)

#Ejercicio número 3-----------------------------------------------------------------------------------------
def intercalar_elementos(lista1, lista2):
    '''Funcion que toma dos listas y devuelve una unica lista con los elementos de las listas de entrada intercalados'''
    if type(lista1)!=list:
        return "Error 01"
    elif type(lista2)!=list:
        return "Error 02"
    elif lista1==[]:
        return lista2
    elif lista2==[]:
        return lista1
    else:
        return intercalar_elementos_aux(lista1, lista2, 0, len(lista1), 0, len(lista2), [])
def intercalar_elementos_aux(lista1, lista2, Indice1, Largo1, Indice2, Largo2, resultado):
    '''Funcion Auxiliar'''
    if Indice1==Largo1:
        return resultado + lista2[Indice2:]
    if Indice2==Largo2:
        return resultado + lista1[Indice1:]
    else:
        return intercalar_elementos_aux(lista1, lista2, Indice1+1, Largo1, Indice2+1, Largo2, resultado + [lista1[Indice1]] + [lista2[Indice2]])
    
print ("La respuesta del ejercicio 3 es: ")
respuesta3 = intercalar_elementos([1,2,3,7,8],[4,5,6])
print (respuesta3)

#Ejercicio número 4------------------------------------------------------------------------------------------
def sumatoria(num1, num2):
    '''Funcion que recibe dos numeros y hace una suma de todos los numeros que esten entre ellos'''
    if type(num1)!=int:
        return "Error 01"
    elif num1<0:
        return "Error 02"
    elif type(num2)!=int:
        return "Error 03"
    elif num2<0:
        return "Error 04"
    elif num1>num2:
        return "Error 05"
    elif num1==num2:
        return num1
    else:
        return sumatoria_aux(num1, num2, 0)
def sumatoria_aux(num1,num2, respuesta):
    '''Funcion Auxiliar'''
    if num1>num2:
        return respuesta
    else:
        return sumatoria_aux(num1+1, num2, respuesta+num1)
    
print ("La respuesta del ejercicio 4 es: ")
respuesta4 = sumatoria(2,7)
print(respuesta4)

#Ejercicio número 5------------------------------------------------------------------------------------------
def elemento_mayor(lista):
    '''Funcion que determina cual es el mayor elemento presente en una lista'''
    if type(lista)!=list:
        return "Error 01"
    elif lista==[]:
        return "Error 02"
    elif verificar_elementos(lista)==False:
        return "Error 03"
    else:
        return elemento_mayor_aux(lista, 0, len(lista), 0)
def elemento_mayor_aux(lista, indice, largo, respuesta):
    '''Funcion Auxiliar'''
    if indice==largo:
        return respuesta
    elif lista[indice]>respuesta:
        return elemento_mayor_aux(lista, indice+1, largo, lista[indice])
    else:
        return elemento_mayor_aux(lista, indice+1, largo, respuesta)
    
print ("La respuesta del ejercicio 5 es: ")
respuesta5 = elemento_mayor([2,4,6,7,5,99])
print (respuesta5)

#Ejercicio número 6------------------------------------------------------------------------------------------
def ordemaniento_insercion(lista):
    '''Funcion que realiza un ordenamiento de numeros en una lista mediante comparaciones'''
    if type(lista)!=list:
        return "Error 01"
    elif verificar_elementos(lista)==False:
        return "Error 02"
    elif lista==[]:
        return "Error 03"
    else:
        return ordenamiento_insercion_aux(lista, 0, 0, len(lista), [])
def ordenamiento_insercion_aux(lista, indice, indiceaux, largo, resultado):
    '''Funcion Auxiliar'''
    if resultado==[]:
        return ordenamiento_insercion_aux(lista, indice+1, indiceaux, largo, resultado+[lista[indice]])
    elif len(resultado)==largo:
        return resultado
    elif lista[indice]>resultado[indiceaux]:
        return ordenamiento_insercion_aux(lista, indice+1, indiceaux+1, largo, resultado+[lista[indice]])
    else:
        return ordenamiento_insercion_aux(lista, indice+1, indiceaux+1, largo, insertar_elemento(resultado,lista[indice]))
def insertar_elemento(resultado, elemento):
    '''Funcion que inserta un elemento de manera ordenada en una lista'''
    if type(resultado)!=list:
        return "Error 1.0"
    elif type(elemento)!=int:
        return "Error 2.0"
    else:
        return insertar_elemento_aux(resultado, elemento, 0, len(resultado), [])
def insertar_elemento_aux(resultado, elemento, indice, largo, resultadoo):
    '''Funcion Auxiliar'''
    if indice==largo:
        return resultadoo + [elemento]
    elif resultado[indice] < elemento:
        return insertar_elemento_aux(resultado, elemento, indice+1, largo, resultadoo+[resultado[indice]])
    else:
        return resultadoo+[elemento]+resultado[indice:]
    
respuesta6 = ordemaniento_insercion([44,625,2,55,7])
print ("La respuesta del ejercicio 6 es: ")
print (respuesta6)
#Fin:D------------------------------------------------------------------------------------------------------------------------------------