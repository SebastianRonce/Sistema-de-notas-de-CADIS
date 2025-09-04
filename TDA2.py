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
    if 0 <= cambio < len(lista):
        lista[cambio] = notaNew
        print(f"Lista actualizada: {lista}")
    else:
        raise IndexError(f"Índice {cambio} fuera de rango. Debe estar entre 0 y {len(lista)-1}")

def eliminar(lista, borrar):
    if 0 <= borrar < len(lista):
        lista.pop(borrar)
        print(f"Lista actualizada: {lista}")
    else:
        raise IndexError(f"Índice {borrar} fuera de rango. Debe estar entre 0 y {len(lista)-1}")

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

# Función para validar entrada de números
def obtener_numero(mensaje, tipo="float"):
    while True:
        try:
            if tipo == "float":
                return float(input(mensaje))
            else:
                return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido. Intente nuevamente.")

# Función para validar opción del menú
def obtener_opcion():
    while True:
        try:
            opcion = input("- ")
            if opcion in ["1", "2", "3", "4"]:
                return opcion
            else:
                print("Error: Opción no válida. Debe ser 1, 2, 3 o 4. Intente nuevamente.")
        except:
            print("Error: Entrada inválida. Intente nuevamente.")

# Función para validar índice
def obtener_indice(mensaje, lista):
    while True:
        try:
            indice = int(input(mensaje))
            if 0 <= indice < len(lista):
                return indice
            else:
                print(f"Error: Índice fuera de rango. Debe estar entre 0 y {len(lista)-1}. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

# Programa principal
estudiante = str(input("Ingrese el nombre del estudiante: "))
print(f"CADIS del estudiante: {estudiante}. ")

print("-----------------------------------------")
for curso in cadis:
    print("-", curso)

# Validar si desea continuar
while True:
    X = str(input("Deseas continuar? S/N "))
    x = X.lower()
    if x in ["s", "si", "n", "no"]:
        break
    else:
        print("Error: Debe responder S/N o Si/No. Intente nuevamente.")

if x == "s" or x == "si":
    print("Iniciando...")
    
    while True:
        print("-----------------------------------------")
        mostrar_Menu()
        opcion = obtener_opcion()
        print("-----------------------------------------")
        
        if opcion == "1":
            print(f"Notas actuales: {notas_Finales}")
            nota = obtener_numero("Ingrese la nota: ")
            agregar(notas_Finales, nota)
            
        elif opcion == "2":
            if len(notas_Finales) == 0:
                print("Error: No hay notas para modificar.")
                continue
            print(f"Notas actuales: {notas_Finales}")
            cambiar = obtener_indice(f"Ingrese el índice de la nota que desea cambiar (0 a {len(notas_Finales)-1}): ", notas_Finales)
            newNota = obtener_numero("Ingrese la nueva nota: ")
            try:
                modificar(notas_Finales, cambiar, newNota)
            except IndexError as e:
                print(f"Error: {e}")
                continue

        elif opcion == "3":
            if len(notas_Finales) == 0:
                print("Error: No hay notas para eliminar.")
                continue
            print(f"Notas actuales: {notas_Finales}")
            borrar = obtener_indice(f"Ingrese el índice de la nota que desea eliminar (0 a {len(notas_Finales)-1}): ", notas_Finales)
            try:
                eliminar(notas_Finales, borrar)
            except IndexError as e:
                print(f"Error: {e}")
                continue

        elif opcion == "4":
            print(f"Notas actuales: {notas_Finales}")
            promedio(notas_Finales)
        
        # Preguntar si desea continuar con otra operación
        while True:
            continuar = str(input("¿Desea realizar otra operación? S/N "))
            continuar = continuar.lower()
            if continuar in ["s", "si", "n", "no"]:
                break
            else:
                print("Error: Debe responder S/N o Si/No. Intente nuevamente.")
        
        if continuar == "n" or continuar == "no":
            print("Saliendo del programa...")
            break
            
else:
    print("Saliendo...")