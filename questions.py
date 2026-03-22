import random
import string

def caracter_valido (letra):
    """Esta función evalúa que el usuario usuario NO ingresa más de una letra, un número o
    cualquier otro carácter inválido"""
    resultado = False
    let_lower = string.ascii_lowercase
    if (letra in let_lower):
        resultado = True
    return resultado

# Se cambiará la estructura de "words" para que pase a ser un diccionario
# Se usarán las palabras actuales para la cateogría informática y se crearán 2 nuevas categorías

words = {
        "informatica":["python","programa","variable","funcion","bucle","cadena","entero","lista",],
        "bandas_rock":["acdc","metallica","muse","slipknot","airbag"],
        "deportes":["futbol","basquet","hockey","natacion","atletismo","voleyball"]
        }

categorias = list(words.keys())

print(f"Selecciona una de las siguientes categorías para jugar: {"-" .join(categorias)}")


categoria_elegida = input('Ingrese la categoría: ')

word = random.choice(words[categoria_elegida])
guessed = []
attempts = 6
puntaje_jugador = 0

print("¡Bienvenido al Ahorcado!")
print()


while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "

    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje_jugador+=6
        print(f'Tu puntaje final es de: {puntaje_jugador} puntos')
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()

    if (caracter_valido(letter)==False):
        print('Entrada no válida')
        continue
    else:
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            puntaje_jugador -= 1

    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje_jugador = 0
    print(f"Tu puntaje final es de: {puntaje_jugador} puntos")
