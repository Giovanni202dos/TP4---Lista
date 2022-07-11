"""
Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
actividades enumeradas a continuación:
    a. listado ordenado por nombre y por especie;
    b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
    c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
    d. mostrar los Jedi de especie humana y twi'lek;
    e. listar todos los Jedi que comienzan con A;
    f. mostrar los Jedi que usaron sable de luz de más de un color;
    g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
    h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
"""
#                   USO ARCHIVOS PARA CARGAR LOS DATOS DE LOS JEDIS
from lista import Lista
class Jedi:

    def __init__(self, nombre, maestros, sable_de_luz,especie):
        self.nombre = nombre
        self.maestros = maestros
        self.sable_de_luz = sable_de_luz
        self.especie = especie
    
    def __str__(self):
        return f"{self.nombre},{self.maestros},{self.sable_de_luz},{self.especie}"
print()
#abro el archivo de texto
file=open('C:/Users/daniel milesi/Documents/Programación/Segundo Año/Algoritmo/Ejer_lista/jedis.txt')
lineas=file.readlines()

#------------------------------------------------------------------------------------

#CARGO LOS JEDIS A LA LISTA_JEDI1 PARA ORDENARLO POR NOMBRE Y HACER EL PUNTO A
lista_jedi1=Lista()
lineas.pop(0)   #le quito la cabezera q solo mostrabrab como estaba organizado el archivo
for i in lineas:
    dato=i.split(';')                       #tengo el vector creado con las separcaion de ";"
    #print(dato)
    dato.pop(-1)
    lista_jedi1.insertar(Jedi(dato[0].title(),dato[3],dato[4],dato[2]),'nombre')    #aca no pongo dato[1] por que esa informacion no la necesito cargar

#CARGO LOS JEDIS A LA LISTA_JEDI2 PARA ORDENARLO POR ESPECIE Y HACER EL PUNTO A
lista_jedi2=Lista()
for i in lineas:
    dato=i.split(';')                       #tengo el vector creado con las separcaion de ";"
    dato.pop(-1)
    lista_jedi2.insertar(Jedi(dato[0],dato[2],dato[3],dato[4]),'especie') 

#-----------------------------------------------------------------------------------   

#funcion para mostrar los datos de un jedi x (lo encuentra si esta ingresado tal cual como esta guardado)
def mostrar_informacion_de_jedi_x(lista,nombre):
    dato=lista.busqueda(nombre,'nombre')
    if dato!= None:
        print(dato.info)
    else:
        print('el jedi no existe')

#barrido para mostrar los datos de un jedi x  sin tener en cuenta la mayuscula o minuscula
def mostrar_informacion_de_jedi_x_sin_tener_en_cuenta_mayus_o_minus(lista,nombre):
    i=0
    encontrado=False
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if dato.nombre.upper()==nombre.upper():
            encontrado=True
            break       #el break para el bucle
        else:                       
            i+=1    #aca si aumento i para q apunte al otro dato
    if encontrado:
        print(dato)
    else:
        print('el jedi no existe')

#funcion para mostrar los padawans(los aprendices)de un maestro x
def mostrar_los_aprendices_de_un_maestro_x(lista,maestro):
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        #print('maestro.upper(): ',maestro.upper(),' in ',dato.maestros.upper(),' ?')
        if maestro.upper() in dato.maestros.upper():
            #print('yes')
            print(dato)          
        i+=1    #aca si aumento i para q apunte al otro dato


#barrido para mostrar todos los jedi de una espcie x
def mostrar_todos_jedis_de_especie_x(lista,especie):
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        #print('dd', dato.especie.upper())
        if dato.especie.upper()==especie.upper():
            print(dato)          
        i+=1    #aca si aumento i para q apunte al otro dato

#barrido para mostrar todos los jedis que empiezen con una letra x
def mostrar_todos_jedis_de_q_empiezen_con_letra_x(lista,letra):
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        #print('dd', dato.especie.upper())
        if dato.nombre.upper()[0]==letra.upper():
            print(dato)          
        i+=1    #aca si aumento i para q apunte al otro dato

#funcion para mostrar los jedis q usaron mas de un sable de luz
def mostrar_todos_jedis_q_usaron_mas_de_un_sable_de_luz(lista):
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        vec=dato.sable_de_luz.split('/')
        if len(vec)>1:
            print(dato)          
        i+=1    #aca si aumento i para q apunte al otro dato

#funcion para mostrar los jedis que usaron un sable de luz de un color x
def mostrar_todos_jedis_q_usaron_un_sable_de_luz_de_color_x(lista,color):
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        #vec=dato.sable_de_luz.split('/')
        if color.upper() in dato.sable_de_luz.upper():
            print(dato)          
        i+=1    #aca si aumento i para q apunte al otro dato

#funcion para mostrar solo los nombres de los padawans(los aprendices)de un maestro x
def mostrar_los_nombres_de_los_aprendices_de_un_maestro_x(lista,maestro):
    i=0
    encontro=False
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        #print('maestro.upper(): ',maestro.upper(),' in ',dato.maestros.upper(),' ?')
        if maestro.upper() in dato.maestros.upper():
            encontro=True
            print(dato.nombre)          
        i+=1    #aca si aumento i para q apunte al otro dato
    if encontro==False:
        print('el maestro: ', maestro,' no tiene ningun padawan')
#-----------------------------------------------------------------------------------
print('A')
print('ordenado por nombre:')
lista_jedi1.barrido()   #ordenado por nombre
print()
print('ordenado por especie:')
lista_jedi2.barrido()   #ordenado por especie
print('B')
mostrar_informacion_de_jedi_x(lista_jedi1,'Ahsoka Tano')
#sin tener en cunta las mayusculas
mostrar_informacion_de_jedi_x_sin_tener_en_cuenta_mayus_o_minus(lista_jedi1,'ahsoka Tano')
print('C')
mostrar_los_aprendices_de_un_maestro_x(lista_jedi1,'Luke Skywalker')
print('D')
mostrar_todos_jedis_de_especie_x(lista_jedi1,'togruta')
print('E')
mostrar_todos_jedis_de_q_empiezen_con_letra_x(lista_jedi1,'A')
print('F')
mostrar_todos_jedis_q_usaron_mas_de_un_sable_de_luz(lista_jedi1)
print('G')
mostrar_todos_jedis_q_usaron_un_sable_de_luz_de_color_x(lista_jedi1,'green')
print('H')
mostrar_los_nombres_de_los_aprendices_de_un_maestro_x(lista_jedi1,'Luke Skywalker')



