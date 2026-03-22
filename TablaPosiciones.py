# Sección de procedimientos:

def agregar_equipo(equipos_puntos):
    equipo_seleccionado = input("Ingrese el equipo que quiera agregar: ")
    if (equipo_seleccionado not in equipos_puntos):
        print("Agregando equipo")
        equipos_puntos[equipo_seleccionado] = 0 
        print("Equipo agregado al diccionario")
    else:
        print("No se puede agregar un equipo que ya existía")


def eliminar_equipo(equipos_puntos):
    equipo_seleccionado = input("Ingrese el equipo que quiera eliminar: ")
    if (equipo_seleccionado in equipos_puntos):
        print("Eliminando equipo")
        eliminado = equipos_puntos.pop(equipo_seleccionado)
        print(f"Equipo {eliminado} eliminado del diccionario")
    else:
        print("No se puede eliminar el equipo ya que no existía")

def registrar_resultado(equipos_puntos):
    equipo_local = input("Inserte el equipo local: ")
    equipo_visitante = input("Inserte el equipo visitante: ")
    if equipo_local not in equipos_puntos or equipo_visitante not in equipos_puntos:
        print("Alguno/s de los equipos ingresados no existe")
    else:
        resultado_partido = input("Inserte el resultado del partido: ")
        goles = resultado_partido.split("-")
        goles_local = goles[0]
        goles_visitante = goles[1]
        if (goles_local>goles_visitante):
            equipos_puntos[equipo_local]+=3
            print(f"Se registro la victoria del equipo: {equipo_local}")
        elif (goles_local<goles_visitante):
            equipos_puntos[equipo_visitante]+=3
            print(f"Se registro la victoria del equipo: {equipo_visitante}")
        else:
            equipos_puntos[equipo_local]+=1
            equipos_puntos[equipo_visitante]+=1
            print(f"Se registro el empate")


def consultar_posiciones(equipos_puntos):
    tabla_posiciones = []
    for equipo in equipos_puntos:
        puntos = equipos_puntos[equipo]
        tabla_posiciones.append([puntos,equipo])
    tabla_posiciones.sort(reverse=True)
    print(f"--- TABLA DE POSICIONES ---\n")
    for elemento in tabla_posiciones:
        print(f"{elemento} \n")


# Definición de variables

opciones = ["1. Agregar Equipo","2. Eliminar Equipo","3. Registrar Resultado","4. Consultar Posiciones","5. Salir"]

equipos_puntos = {}

# Lógica principal

seguir =True
while seguir==True:
    print("Selecciones una de las opciones del menú: ")
    print(f"--- TORNEO DE FÚTBOL ---\n{'\n'.join(opciones)}")
    seleccion = int(input("Ingrese el numero correspondiente a la acción que quiera realizar: "))
    match seleccion:
        case 1:
            agregar_equipo(equipos_puntos)
        case 2:
            eliminar_equipo(equipos_puntos)
        case 3:
            registrar_resultado(equipos_puntos)
        case 4:
            consultar_posiciones(equipos_puntos)
        case 5:
            print("Saliendo")
            break
        case _:
            print("Opción no válida")

print("Finalizando el programa")
