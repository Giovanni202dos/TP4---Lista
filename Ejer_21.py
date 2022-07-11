"""
Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
nombre, valoración del público es un valor comprendido entre 0-10, año de estreno y recaudación.
Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
    a. permitir filtrar las películas por año es decir mostrar todas las películas de un determinado
año;
    b. mostrar los datos de la película que más recaudo;
    c. indicar las películas con mayor valoración del público, puede ser más de una;
    d. mostrar el contenido de la lista en los siguientes criterios de orden solo podrá utilizar una
lista auxiliar:
I. por nombre,
II. por recaudación,
III. por año de estreno,
IV. por valoración del público.
"""
from lista import Lista
class Pelicula:

    def __init__(self, nombre, v_p, anio,recaudacion):
        self.nombre = nombre
        self.v_p = v_p
        self.anio = anio
        self.recaudacion = recaudacion
    
    def __str__(self):
        return f"{self.nombre},{self.v_p},{self.anio},{self.recaudacion}"

lista_de_peliculas= Lista()

lista_de_peliculas.insertar(Pelicula('Spider-man',10,2020,10000),'nombre')
lista_de_peliculas.insertar(Pelicula('Iron-man',1,2020,14000),'nombre')
lista_de_peliculas.insertar(Pelicula('Superman',10,2021,20000),'nombre')

#funcion para mostra una pelicula estrenada en un anio x
def mostrar_peli_estrenada_en_anio_x(lista,anio):
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if dato.anio==anio:
            print('la pelicula:', dato.nombre,'se estreno en el anio: ', anio)
        i+=1

#para mostrar la pelicula que mas recaudo
def mostrar_peli_con_mas_recaudacion(lista):
    i=0
    recaudacion_mayor=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if dato.recaudacion>recaudacion_mayor:
            recaudacion_mayor=dato.recaudacion
            peli_de_mayor_recaudacion=dato
        i+=1
    print('la pelicula que mayor recaudacion produjo fue: ', peli_de_mayor_recaudacion.nombre,' con una totalidad de: ', recaudacion_mayor,'$')
    print('sus datos son: ')
    print('nombre: ',peli_de_mayor_recaudacion.nombre)
    print('valoracion publica: ',peli_de_mayor_recaudacion.v_p)
    print('anio de estreno: ',peli_de_mayor_recaudacion.anio)

#para mostrar la pelicula que mayor valoracion del publico(pueden haber varias con el mismo nivel)
def mostrar_peli_con_mayor_valoracion_del_publico(lista):
    i=0
    valoracion_mayor=0
    vec_de_peli=[]
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if dato.v_p>valoracion_mayor:
            valoracion_mayor=dato.v_p
            peli_mayor=dato
        elif dato.v_p==valoracion_mayor:
            vec_de_peli.append(dato)
        i+=1
    vec_de_peli.append(peli_mayor)
    i=0
    if len(vec_de_peli)>1:
        print('las peliculas que mayor valoraciones del publico obtuvieron fueron: ')
        for i in range(0,len(vec_de_peli)):
            print(vec_de_peli[i].nombre)
    else:
        print('la pelicula que mayor valoracion del publico obtuvo fue: ')
        print(vec_de_peli[0].nombre)

#funcion para mostra la la lista en el suguiente orden(nombre, recaudacion, anio de estreno y por valoracion del publico)
def mostrar_peli_en_el_siguiente_orden_nombre_recau_anio_v_p(lista):
    i=1
    lista_aux=Lista()
    orden={1:'nombre',2:'recaudacion',3:'anio',4:'v_p'}
    while i<=len(orden):    #para mostrar en orden  lo paso a una lista auxiliar
        text=orden.get(i)
        lista_aux.insertar2_sin_ordenar(text)
        i+=1 
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i) #obtengo la pelicula
        i2=0
        while i2<lista_aux.tamanio(): #lo guardo en la sublista auxiliar(de acuerdo a que orden mostrar)
            el_contenido=lista_aux.obtener_elemento(i2)
            ubi=lista_aux.busqueda(el_contenido)
            ubi.sublista.insertar(dato,el_contenido)
            i2+=1
        i+=1
    print()
    lista_aux.barrido_lista_lista()

print('A')
mostrar_peli_estrenada_en_anio_x(lista_de_peliculas,2020)
print('B')
mostrar_peli_con_mas_recaudacion(lista_de_peliculas)
print('C')
mostrar_peli_con_mayor_valoracion_del_publico(lista_de_peliculas)
print('D')
mostrar_peli_en_el_siguiente_orden_nombre_recau_anio_v_p(lista_de_peliculas)



