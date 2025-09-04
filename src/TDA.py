# Lista de calificaciones
# Listas que almacenan las calificaciones de cada materia
# Cada lista representa las notas de un CADI (Curso de Aprendizaje Dirigido)
calificaciones_Calculo = [4.0, 3.0]
calificaciones_Fisica = [2.0, 4.5]
calificaciones_Arquitectura = [3.0, 5.0]
calificaciones_Fundamentos = [4.0, 4.2]
calificaciones_Lenguje = [3.0, 4.0]
calificaciones_Estructuras = [5.0, 3.0]

# Esta es la Tupla
cadis = ("Calculo Multivariado", 
        "Física III", 
        "Arquitectura de Computadores", 
        "Fundamentos Administrativos", 
        "Lengua Extranjera", 
        "Estructuras de Información",
        )
# Estas funciones aseguran que el usuario ingrese datos válidos
# y repiten la pregunta hasta obtener una entrada correcta

def validar_opcion_menu():
    """
    Valida que la opción del menú sea válida (1-4)
    Retorna: string con la opción válida
    """
    while True:
        try:
            opcion = input("- ")
            if opcion in ["1", "2", "3", "4"]:
                return opcion
            else:
                print("Opción no válida. Por favor ingrese 1, 2, 3 o 4.")
        except:
            print("Error en la entrada. Intente nuevamente.")

def validar_nota():
    """
    Valida que la nota sea un número flotante válido entre 0 y 5
    Retorna: float con la nota válida
    """
    while True:
        try:
            nota = float(input("Ingresa la nota: "))
            if 0.0 <= nota <= 5.0:
                return nota
            else:
                print("La nota debe estar entre 0.0 y 5.0. Intente nuevamente.")
        except ValueError:
            print("Por favor ingrese un número válido. Intente nuevamente.")

def validar_indice(lista):
    """
    Valida que el índice sea válido para la lista
    Parámetros: lista - la lista de calificaciones
    Retorna: int con el índice válido
    """
    while True:
        try:
            indice = int(input("Ingresa el índice de la nota (empezando desde 0): "))
            if 0 <= indice < len(lista):
                return indice
            else:
                print(f"El índice debe estar entre 0 y {len(lista)-1}. Intente nuevamente.")
        except ValueError:
            print("Por favor ingrese un número entero válido. Intente nuevamente.")

def validar_continuar():
    """
    Valida la respuesta de continuar (S/N)
    Retorna: boolean - True si quiere continuar, False si no
    """
    while True:
        respuesta = input("Deseas continuar? S/N ").lower().strip()
        if respuesta in ["s", "si", "n", "no"]:
            return respuesta in ["s", "si"]
        else:
            print("Por favor responda S o N. Intente nuevamente.")

def validar_cadi():
    """
    Valida la selección de CADI (1-6)
    Retorna: string con la opción válida del CADI
    """
    while True:
        try:
            opcion = input("¿Qué CADI vas a calificar? ")
            if opcion in ["1", "2", "3", "4", "5", "6"]:
                return opcion
            else:
                print("Opción no válida. Por favor ingrese un número del 1 al 6.")
        except:
            print("Error en la entrada. Intente nuevamente.")
# Funcion para agregar una nota Nueva
def agregar(lista, nota):
    lista.append(nota)
    print(f"Se agrego la nota: {lista}")
# Funcion para modificar una Nota ya existente por medio del indice
def modificar(lista, cambio, notaNew):
    lista[cambio] = notaNew
    print (f"Se actualizo la lista: {lista}")
# Funcion que elimina una nota pidiendo el indice
def eliminar(lista, indice):
    nota_eliminada = lista.pop(indice)
    print(f"Se elimino la nota {nota_eliminada}. Lista actial: {lista}")
# Funcion para calcular el promedio de cada uno de los CADIS
def promedio(lista):
    if len(lista) == 0:
        print("No hay notas para calcular el promedio.")
        return
    suma = sum(lista)
    promedio = suma / len(lista)
    print(f"El promedio final del estudiante es: {promedio:.2f}")

# Aqui mostramos el menu para modificar las listas  
def motrar_menu():
    print("¿Que opcion vas a realizar? ")
    print("1. Agregar una nota. ")
    print("2. Modificar una nota. ")
    print("3. Eliminar una nota. ")
    print("4. Calcular promedio.")
# Validación del nombre del estudiante
# Se repite hasta que el usuario ingrese un nombre válido (no vacío)
while True:
    estudiante = input("Ingrese el nombre del estudiante: ").strip()
    if estudiante:
        break
    else:
        print("El nombre no puede estar vacío. Intente nuevamente.")

# Mostrar información del estudiante y materias disponibles
print(f"CADIS del estudiante: {estudiante}. ")

print("-----------------------------------------")
for curso in cadis:
    print("-", curso)
print("-----------------------------------------")

if x == "s" or x == "si" :
        print("Elija que CADI deseas calificar. ")
        print("1. Calculo Multivariado. ")
        print("2. Física III. ")
        print("3. Arquitectura de Computadores. ")
        print("4. Fundamentos Administrativos. ")  
        print("5. Lengua Extranjera. ")
        print("6. Estructuras de Información ")
        
        opcion = str(input("¿Qué CADI vas a calificar? "))
        print("-----------------------------------------")
        
        if opcion == "1":
            #Calculo Multivariado 
            motrar_menu()
            opcion1 = str(input("- "))
            if opcion1 == "1":
                print(f"Lista actual: {calificaciones_Calculo}")      
                new = float(input("Ingresa la nota: "))
                agregar(calificaciones_Calculo, new)
            elif opcion1 == "2":
                print(f"Notas: {calificaciones_Calculo}")
                cambiar = int(input("Ingresa el area de la nota que desea modificar: "))
                nuevaNota = float(input("Ingrese la nueva nota: "))
                modificar(calificaciones_Calculo, cambiar, nuevaNota)
            elif opcion1 == "3":
                print(f"Notas: {calificaciones_Calculo}")
                borrar = int(input("ingresa el area de la nota que vas a eliminar. "))
                eliminar(calificaciones_Calculo, borrar)
            elif opcion1 == "4":
                print(f"Lista actual: {calificaciones_Calculo}")
                promedio(calificaciones_Calculo)
            else:
                print("Opcion no valida. ")
        
        elif opcion == "2":
             #Fisica III   
            motrar_menu()
            opcion2 = str(input("- "))
            if opcion2 == "1":
                print(f"Lista actual: {calificaciones_Fisica}")    
                new = float(input("Ingresa la nota: "))
                agregar(calificaciones_Fisica, new)
            elif opcion2 == "2":
                print(f"Notas: {calificaciones_Fisica}")
                cambiar = int(input("Ingresa el area de la nota que desea modificar: "))
                nuevaNota = float(input("Ingrese la nueva nota: "))
                modificar(calificaciones_Fisica, cambiar, nuevaNota)
            elif opcion2 == "3":    
                print(f"Notas: {calificaciones_Fisica}")
                borrar = int(input("ingresa el area de la nota que vas a eliminar. "))
                eliminar(calificaciones_Fisica, borrar)
            elif opcion2 == "4":
                print(f"Lista actual: {calificaciones_Fisica}")
                promedio(calificaciones_Fisica)
            else:
                print("Opcion no valida. ")
        
        elif opcion == "3":
            #Arquictectura de computadores
            motrar_menu()
            opcion3 = str(input("- "))
            if opcion3 == "1":
                print(f"Lista actual: {calificaciones_Arquitectura}")
                new = float(input("Ingresa la nota: "))
                agregar(calificaciones_Arquitectura, new)
            elif opcion3 == "2":
                print(f"Notas: {calificaciones_Arquitectura}")
                cambiar = int(input("Ingresa el area de la nota que desea modificar: "))
                nuevaNota = float(input("Ingrese la nueva nota: "))
                modificar(calificaciones_Arquitectura, cambiar, nuevaNota)
            elif opcion3 == "3":
                print(f"Notas: {calificaciones_Arquitectura}")
                borrar = int(input("ingresa el area de la nota que vas a eliminar. "))
                eliminar(calificaciones_Arquitectura, borrar)
            elif opcion3 == "4":
                print(f"Lista actual: {calificaciones_Arquitectura}")
                promedio(calificaciones_Arquitectura)
            else:
                print("Opcion no valida. ")
        
        elif opcion == "4":
                #Fundamentos Administrativos
            motrar_menu()
            opcion4 = str(input("- "))
            if opcion4 == "1":
                print(f"Lista actual: {calificaciones_Fundamentos}")
                new = float(input("Ingresa la nota: "))
                agregar(calificaciones_Fundamentos, new)
            elif opcion4 == "2":
                print(f"Notas: {calificaciones_Fundamentos}")
                cambiar = int(input("Ingresa el area de la nota que desea modificar: "))
                nuevaNota = float(input("Ingrese la nueva nota: "))
                modificar(calificaciones_Fundamentos, cambiar, nuevaNota)
            elif opcion4 == "3":
                print(f"Notas: {calificaciones_Fundamentos}")
                borrar = int(input("ingresa el area de la nota que vas a eliminar. "))
                eliminar(calificaciones_Fundamentos, borrar)
            elif opcion4 == "4":
                print(f"Lista actual: {calificaciones_Fundamentos}")
                promedio(calificaciones_Fundamentos)
            else:
                print("Opcion no valida. ")
                
        elif opcion == "5":
                #Lengua Estrangera
            motrar_menu()
            opcion5 = str(input("- "))
            if opcion5 == "1":
                print(f"Lista actual: {calificaciones_Lenguje}")
                new = float(input("Ingresa la nota: "))
                agregar(calificaciones_Lenguje, new)
            elif opcion5 == "2":
                print(f"Notas: {calificaciones_Lenguje}")
                cambiar = int(input("Ingresa el area de la nota que desea modificar: "))
                nuevaNota = float(input("Ingrese la nueva nota: "))
                modificar(calificaciones_Lenguje, cambiar, nuevaNota)
            elif opcion5 == "3":
                print(f"Notas: {calificaciones_Lenguje}")
                borrar = int(input("ingresa el area de la nota que vas a eliminar. "))
                eliminar(calificaciones_Lenguje, borrar)
            elif opcion5 == "4":
                print(f"Lista actual: {calificaciones_Lenguje}")
                promedio(calificaciones_Lenguje)
            else:
                print("Opcion no valida. ")
                    
        elif opcion == "6":
                     # Estructuras de Información
            motrar_menu()
            opcion6 = str(input("- "))
            if opcion6 == "1":
                print(f"Lista actual: {calificaciones_Estructuras}")
                new = float(input("Ingresa la nota: "))
                agregar(calificaciones_Estructuras, new)
            elif opcion6 == "2":
                print(f"Notas: {calificaciones_Estructuras}")
                cambiar = int(input("Ingresa el area de la nota que desea modificar: "))
                nuevaNota = float(input("Ingrese la nueva nota: "))
                modificar(calificaciones_Estructuras, cambiar, nuevaNota)
            elif opcion6 == "3":
                print(f"Notas: {calificaciones_Estructuras}")
                borrar = int(input("ingresa el area de la nota que vas a eliminar. "))
                eliminar(calificaciones_Estructuras, borrar)
            elif opcion6 == "4":
                print(f"Lista actual: {calificaciones_Estructuras}")
                promedio(calificaciones_Estructuras)
            else:
                print("Opcion no valida. ")
else:
    print("Saliendo...")
        
