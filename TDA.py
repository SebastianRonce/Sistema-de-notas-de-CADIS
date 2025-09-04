# Lista de calificaciones
calificaciones_Calculo = [4.0, 3.0]
calificaciones_Fisica = [2.0, 4.5]
calificaciones_Arquitectura = [3.0, 5.0]
calificaciones_Fundamentos = [4.0, 4.2]
calificaciones_Lenguje = [3.0, 4.0]
calificaciones_Estructuras = []

# Esta es la Tupla
cadis = ("Calculo Multivariado", 
        "Física III", 
        "Arquitectura de Computadores", 
        "Fundamentos Administrativos", 
        "Lengua Extranjera", 
        "Estructuras de Información",
        )

# Funcion para agregar una nota Nueva
def agregar(lista, nota):
    lista.append(nota)
    print(f"Se agrego la nota: {lista}")
# Funcion para modificar una Nota ya existente por medio del indice
def modificar(lista, cambio, notaNew):
    lista[cambio] = notaNew
    print(lista)
# Funcion que elimina una nota pidiendo el indice
def eliminar(lista, borrar):
    lista.pop(borrar)
    print(f"Se elimino la nota: {lista}")

def motrar_menu():
    print("¿Que opcion vas a realizar? ")
    print("1. Agregar una nota. ")
    print("2. Modificar una nota. ")
    print("3. Eliminar una nota. ")

estudiante = str(input("Ingrese el nombre del estudiante. "))
print(f"CADIS del estudiante: {estudiante}. ")

print("-----------------------------------------")
for curso in cadis:
    print("-", curso)
print("-----------------------------------------")

print("Elija que CADI deseas calificar. ")
print("1. Calculo Multivariado. ")
print("2. Física III. ")
print("3. Arquitectura de Computadores. ")
print("4. Fundamentos Administrativos. ")  
print("5. Lengua Extranjera. ")
print("6. . ")

opcion = str(input("¿Qué CADI vas a calificar? "))
print("-----------------------------------------")

if opcion == "1":
    motrar_menu()
    opcion1 = str(input("- "))
    if opcion1 == "1":
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
    else:
        print("Opcion no valida. ")

elif opcion == "2":
    motrar_menu()
    opcion2 = str(input("- "))
    if opcion2 == "1":
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
    else:
        print("Opcion no valida. ")

elif opcion == "3":
    motrar_menu()
    opcion3 = str(input("- "))
    if opcion3 == "1":
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
    else:
        print("Opcion no valida. ")

elif opcion == "4":
    motrar_menu()
    opcion4 = str(input("- "))
    if opcion4 == "1":
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
    else:
        print("Opcion no valida. ")

elif opcion == "5":
    motrar_menu()
    opcion5 = str(input("- "))
    if opcion5 == "1":
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
    else:
        print("Opcion no valida. ")