notas_Finales = [4.0,
                  4.5,
                  3.9,
                  4.0,
                  4.3,
                  3.8
                  ]

cadis = ("Calculo Multivariado", 
        "Física III", 
        "Arquitectura de Computadores", 
        "Fundamentos Administrativos", 
        "Lengua Extranjera", 
        "Estructuras de Información",
        )

def agregar(lista, nota):
    lista.append(nota)
    print(f"Lista actualizada: {lista} ")

def modificar(lista, cambio, notaNew):
    lista[cambio] = notaNew
    print(f"Lista actualizada: {lista}")

def eliminar(lista, borrar):
    lista.pop(borrar)
    print(f"Lista actualizada: {lista}")

def promedio(lista):
    if len(lista) == 0:
        print("No hay notas para calcular el promedio.")
        return
    suma = sum(lista)
    promedio = suma / len(lista)
    print(f"El promedio final del estudiante es: {promedio:.2f}")

def mostrar_Menu():
    print("¿Que opcion vas a realizar? ")
    print("1. Agregar una nota. ")
    print("2. Modificar una nota. ")
    print("3. Eliminar una nota. ")
    print("4. Calcular promedio final.")

estudiante = str(input("Ingrese el nombre del estudiante: "))
print(f"CADIS del estudiante: {estudiante}. ")

print("-----------------------------------------")
for curso in cadis:
    print("-", curso)

X = str(input("Deseas continuar? S/N "))
x = X.lower()

if x == "s" or x == "si" :
    print("Iniciando...")
    print("-----------------------------------------")
    mostrar_Menu()
    opcion = str(input("- "))
    print("-----------------------------------------")
    if opcion == "1":
        print(f"Notas actuales: {notas_Finales}")
        nota = float(input("Ingrese la nota: "))
        agregar(notas_Finales, nota)
        
    elif opcion == "2":
        print(f"Notas actuales: {notas_Finales}")
        cambiar = int(input("Ingrese el indice de la nota que desea cambiar. (0 a 5): "))
        newNota = float(input("Ingrese la nueva nota: "))
        modificar(notas_Finales, cambiar, newNota)

    elif opcion == "3":
        print(f"Notas actuales: {notas_Finales}")
        borrar = int(input("Ingrese el indice de la nota que desea eliminar. (0 a 5): "))
        eliminar(notas_Finales, borrar)

    elif opcion == "4":
        print(f"Notas actuales: {notas_Finales}")
        promedio(notas_Finales)

    else:
        print("Opción no valida. ")
else:
    print("Saliendo...")

