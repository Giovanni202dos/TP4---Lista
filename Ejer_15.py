"""
Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
    a. obtener la cantidad de Pokémons de un determinado entrenador;
    b. listar los entrenadores que hayan ganado más de tres torneos;
    c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
    d. mostrar todos los datos de un entrenador y sus Pokémos;
    e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
    f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
    g. el promedio de nivel de los Pokémons de un determinado entrenador;
    h. determinar cuántos entrenadores tienen a un determinado Pokémon;
    i. mostrar los entrenadores que tienen Pokémons repetidos;
    j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
o Wingull;
    k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;
"""
from lista import Lista
from random import choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_ganadas,batallas_perdidas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
    
    def __str__(self):
        return f"{self.nombre},{self.torneos_ganados},{self.batallas_ganadas},{self.batallas_perdidas}"

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre}, {self.nivel},{self.tipo},{self.subtipo}"

lista_de_entrenadores= Lista()
#un vector de diccionario con los datos de los entrenadores
entrenadores=[
    {'name':'Entrenador1','tg':15,'bg':2,'bp':10},
    {'name':'Entrenador2','tg':3,'bg':10,'bp':12},
    {'name':'Entrenador3','tg':20,'bg':3,'bp':1},
    {'name':'Entrenador4','tg':1,'bg':40,'bp':20},
]
#le cargo los datos a los entrenadores y los agrego a la lista
for i in entrenadores:
    lista_de_entrenadores.insertar(Entrenador(i['name'],i['tg'],i['bg'],i['bp']),'nombre')

lista_de_entrenadores.barrido()

#un vector de diccionario con los datos de los pokemos
pokemones=[
    {'name': 'pok1', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'pok2', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'pok3', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
    {'name': 'pok4', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
    {'name': 'pok5', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'pok6', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]

#le cargo los datos a los pokemones y los agrego a la sublista de los entrenadores
for i in entrenadores:  #este for tomara los nombres del vector de entrandores(para luego acceder a su posicion guardada en la lista)
    for i2 in range(3): #les cargo 3 pokemos a cada uno
        pokemon=choice(pokemones)   #esto tomara una posicion del vector(aleatoriamente)
        posicion=lista_de_entrenadores.busqueda(i['name'],'nombre')
        posicion.sublista.insertar(Pokemon(pokemon['name'],pokemon['nivel'],pokemon['tipo'],pokemon['subtipo'],),'nombre')
lista_de_entrenadores.barrido_lista_lista()

#funcion para mostrar todos los pokemos de un entrenador x(osea mostra la sublista de un entrenador x)
def mostrar_todos_los_pokemones_de_un_entrenador_x(lista,nombre):
    i=0
    ubi_entrenador=lista.busqueda(nombre,'nombre')     #aca saco la ubi del entrenador(de esta manera accedo a la sublista)
    if ubi_entrenador!=None:             #si encuentra el entrnador 
        while i<ubi_entrenador.sublista.tamanio():     #barrido q recorre los pokemones(en la sublista)
            dato2=ubi_entrenador.sublista.obtener_elemento(i)
            print('los pokemones del entrenador: ',nombre,'son')
            print(dato2)
            i+=1
    else:
        print('ese entrenador no existe')

#funcion para mostrar los entrenadores que hayan ganado mas de un determinado numeros de torneos
def mostrar_entrenadores_q_hayan_ganado_mas_de_x_torneos(lista,numero):
    i=0
    i2=0
    while i<lista.tamanio():    #barrido q recorre todos los entrenadores
        dato=lista.obtener_elemento(i)      #obtengo el dato(del cual saco su nombre)
        if dato.torneos_ganados>numero:
            print('los que ganaron mas de: ', numero,' de torneos son:')
            print(dato)
        i+=1
        
#funcion para mostrar al entrenador con mayor torneos ganados y mostra su pokemon de mayor nivel
def mostrar_el_pokemon_de_mayor_nivel_del_entrenador_con_mayor_torneos_ganados(lista):
    i=0
    i2=0
    mayor=0
    while i<lista.tamanio():    #barrido q recorre todos los entrenadores para saber quien gano mas torneos
        dato=lista.obtener_elemento(i)      #obtengo el dato(del cual saco su nombre)
        if dato.torneos_ganados>mayor:
            mayor=dato.torneos_ganados
            nombre_del_mayor=dato.nombre
        i+=1
    ubi=lista.busqueda(nombre_del_mayor,'nombre')
    pokemon_nivel_mayor=0
    while i2<ubi.sublista.tamanio():    #me muevo por la sublista de pokemones
        dato_pokemon=ubi.sublista.obtener_elemento(i2)
        print(dato_pokemon)
        if dato_pokemon.nivel > pokemon_nivel_mayor:
            pokemon_nivel_mayor=dato_pokemon.nivel
            dato_del_pokemon_mayor=dato_pokemon
        i2+=1
    print('el entrenador con mas torneos ganados es:', nombre_del_mayor)
    print('su pokemon de mayor nivel es: ', dato_del_pokemon_mayor)

#funcion para mostrar el porecentaje de batllas ganadas de cada entrenador 
def mostrar_aquellos_entrenadores_cuyo_porcentaje_de_batallas_ganadas_sea_mayor_a_x_(lista,porcentaje):
    i=0
    batallas_en_total=0
    while i<lista.tamanio():    #barrido q recorre todos los entrenadores 
        dato=lista.obtener_elemento(i)      #obtengo el dato(del cual saco las batallas)
        batallas_en_total+=dato.batallas_ganadas
        batallas_en_total+=dato.batallas_perdidas
        porcentaje_aux=(dato.batallas_ganadas*100)/batallas_en_total
        if porcentaje_aux>porcentaje:
            print('el porcentaje de batllas ganadas mayor a:',porcentaje,'%'' es del entrenador: ', dato.nombre,' es:')
            print(porcentaje_aux,'%')
        i+=1
        batallas_en_total=0

#funcion para mostrar los entrenadores que tengan un pokemon de tipo x o subtipo x
def mostrar_los_entrenadores_que_tengan_un_pokemon_de_tipo_x_o_subtipo_x(lista,a_buscar):
    i=0
    i2=0
    while i<lista.tamanio():    #barrido q recorre todos los entrenadores
        dato=lista.obtener_elemento(i)      #obtengo el dato
        ubi=lista.busqueda(dato.nombre,'nombre')     #aca saco la ubi del nombre(de esta manera accedo a la sublista)
        while i2<ubi.sublista.tamanio():     #barrido q recorre los pokemones(en la sublista)
            dato2=ubi.sublista.obtener_elemento(i2)
            tiene=False
            if dato2.tipo==a_buscar or dato2.subtipo==a_buscar:
                tiene=True
            i2+=1
        if tiene:
            print('el entrenador: ', dato.nombre,' tiene uno o varios pokemones de tipo/subtipo: ',a_buscar)
        i+=1
        i2=0

#funcion para mostrar el promedio de nivel de los pokemones de un x entrenador
def mostrar_elpromedio_de_vivel_de_los_pokemones_de_un_x_entrenador(lista, nombre):
    i2=0
    ubi=lista.busqueda(nombre,'nombre')     #aca saco la ubi del nombre(de esta manera accedo a la sublista)
    if ubi!=None:
        cantidad_de_pokemones=ubi.sublista.tamanio()
        total=0
        while i2<ubi.sublista.tamanio():     #barrido q recorre los pokemones(en la sublista)
            dato2=ubi.sublista.obtener_elemento(i2)
            total=total+dato2.nivel
            i2+=1
        resultado=total/cantidad_de_pokemones
        print('el entranador:',nombre,' tiene un promedio de novel de sus pokemones de: ', resultado)
        i2=0
    else:
        print('no existe entrenador')

#funcion para mostrar cuantos entrenadores tienen determinado pokemon
def mostrar_cuantos_entrenadores_tienen_un_pokemon_x(lista,pokemon_a_buscar):
    i=0
    i2=0
    contador=0
    while i<lista.tamanio():    #barrido q recorre todos los entrenadores
        dato=lista.obtener_elemento(i)      #obtengo el dato
        ubi=lista.busqueda(dato.nombre,'nombre')     #aca saco la ubi del nombre(de esta manera accedo a la sublista)
        tiene=False
        while i2<ubi.sublista.tamanio():     #barrido q recorre los pokemones(en la sublista)
            dato2=ubi.sublista.obtener_elemento(i2)
            if dato2.nombre==pokemon_a_buscar:
                tiene=True
            i2+=1
        if tiene:
            contador+=1
        i+=1
        i2=0
    if contador!=0:
        print('la cantidad de entrenadores que tiene el pokemon: ', pokemon_a_buscar,' es de: ', contador)
    else:
        print('ningun entrenador tiene el pokemon: ', pokemon_a_buscar)

#funcion para mostrar los entrenadores que tienen pokemonones repetidos
def mostrar_los_entrenadores_q_tienen_pokemones_repetidos_v2(lista):
    i=0
    i3=0
    while i<lista.tamanio():    #barrido q recorre todos los entrenadores
        dato=lista.obtener_elemento(i)      #obtengo el dato
        ubi=lista.busqueda(dato.nombre,'nombre')     #aca saco la ubi del nombre(de esta manera accedo a la sublista)
        i2=0
        encontro=False
        while i2<ubi.sublista.tamanio():     #barrido q recorre los pokemones(en la sublista)
            dato2=ubi.sublista.obtener_elemento(i2)
            ubi.sublista.eliminar(dato2.nombre,'nombre')
            i3=0
            while i3<ubi.sublista.tamanio():
                dato3=ubi.sublista.obtener_elemento(i3)
                if dato3.nombre==dato2.nombre:
                    encontro=True
                i3+=1
            i2+=1
            ubi.sublista.insertar(dato2,'nombre')   #lo guardo otra vez
        if encontro:
            print('el entrenador: ',dato.nombre,' tiene al menos un pokemon repetido')
        else:
            print('el entrenador: ',dato.nombre,' no tiene ningun pokemon repetido') 
        i+=1

#funcion para mostrar a los entrenadores q tienen un pokemon x
def mostrar_a_los_entrenadores_q_tienen_un_pokemon_x(lista,pokemon):
    i=0
    i2=0
    while i<lista.tamanio():    #barrido q recorre todos los entrenadores
        dato=lista.obtener_elemento(i)      #obtengo el dato(del cual saco su nombre)
        ubi=lista.busqueda(dato.nombre,'nombre')     #aca saco la ubi del nombre(de esta manera accedo a la sublista)
        contador=0
        while i2<ubi.sublista.tamanio():     #barrido q recorre las pokemones(en la sublista)
            dato2=ubi.sublista.obtener_elemento(i2)
            if dato2.nombre.upper()==pokemon.upper():
                contador+=1
            i2+=1
        if contador!=0:
            print('el entrenador: ',dato.nombre,' tiene el pokemon: ',pokemon)
        else:
            print('el entrenador: ',dato.nombre,' no tiene el pokemon',pokemon)
        i+=1
        i2=0

#funcion para mostrar si un entrenador x tiene un pokemon x
def mostrar_si_entrenador_x_tiene_un_pokemon_x(lista,nombre,pokemon):
    i2=0
    ubi=lista.busqueda(nombre,'nombre')     #aca saco la ubi del nombre(de esta manera accedo a la sublista)
    contador=0
    if ubi!=None:
        while i2<ubi.sublista.tamanio():     #barrido q recorre las pokemones(en la sublista)
            dato2=ubi.sublista.obtener_elemento(i2)
            if dato2.nombre.upper()==pokemon.upper():
                contador+=1
                pokemon_encontrado=dato2
            i2+=1
        if contador!=0:
            print('el entrenador: ',nombre,' tiene el pokemon: ',pokemon,' y sus datos son:')
            print('Los datos del entrenador:')
            print(ubi.info)
            print('Los datos del pokemon son: ')
            print(pokemon_encontrado)
        else:
            print('el entrenador: ',nombre,' no tiene el pokemon',pokemon)
        i2=0
    else:
        print('el entrenador no existe')

#funcion para mostrar los datos de un entrenador x y su pokemones (osea mostra la sublista de un entrenador x)
def mostrar_todos_los_datos_de_entrenador_x_y_sus_pokemones(lista,nombre):
    i=0
    ubi_entrenador=lista.busqueda(nombre,'nombre')     #aca saco la ubi del entrenador(de esta manera accedo a la sublista)
    if ubi_entrenador!=None:             #si encuentra el entrnador 
        print('los datos del entrenador son: ')
        print('Nombre:',ubi_entrenador.info.nombre)
        print('Torneos ganados:',ubi_entrenador.info.torneos_ganados)
        print('Batallas ganadas:',ubi_entrenador.info.batallas_ganadas)
        print('Batallas perdidas:',ubi_entrenador.info.batallas_perdidas)
        while i<ubi_entrenador.sublista.tamanio():     #barrido q recorre los pokemones(en la sublista)
            dato2=ubi_entrenador.sublista.obtener_elemento(i)
            print('los pokemones del entrenador: ',nombre,'son')
            print(dato2)
            i+=1
    else:
        print('ese entrenador no existe')

print()
print('A')  
mostrar_todos_los_pokemones_de_un_entrenador_x(lista_de_entrenadores,'Entrenador1')  
print()
print('B') 
mostrar_entrenadores_q_hayan_ganado_mas_de_x_torneos(lista_de_entrenadores,3)
print()  
print('C')
mostrar_el_pokemon_de_mayor_nivel_del_entrenador_con_mayor_torneos_ganados(lista_de_entrenadores)
print('D')
mostrar_todos_los_datos_de_entrenador_x_y_sus_pokemones(lista_de_entrenadores,'Entrenador4')
print('E')
mostrar_aquellos_entrenadores_cuyo_porcentaje_de_batallas_ganadas_sea_mayor_a_x_(lista_de_entrenadores,50)
print('F')
mostrar_los_entrenadores_que_tengan_un_pokemon_de_tipo_x_o_subtipo_x(lista_de_entrenadores,'agua')
print('G')
mostrar_elpromedio_de_vivel_de_los_pokemones_de_un_x_entrenador(lista_de_entrenadores,'Entrenador4')
print('H')
mostrar_cuantos_entrenadores_tienen_un_pokemon_x(lista_de_entrenadores,'pok3')
print('I')
mostrar_los_entrenadores_q_tienen_pokemones_repetidos_v2(lista_de_entrenadores)
print('J')
mostrar_a_los_entrenadores_q_tienen_un_pokemon_x(lista_de_entrenadores,'pok4')
print('k')
mostrar_si_entrenador_x_tiene_un_pokemon_x(lista_de_entrenadores,'Entrenador3','pok3')