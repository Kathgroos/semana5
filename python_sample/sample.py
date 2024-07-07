def menu_principal():
    while True:
        print('Por favor seleccione el proceso que desea realizar.')
        print('1: Ingrese puntos de evaluación y comentarios.')
        print('2: Comprueba los resultados hasta el momento.')
        print('3: Terminar.')
        num = input()  # Leer la opción del usuario

        if num.isdecimal():  # Verificar si la opción es un número decimal
            num = int(num)  # Convertir la opción a entero
            if num == 1:
                ingresar_puntuacion_y_comentario()  # Llamar a la función para ingresar puntuación y comentario
            elif num == 2:
                comprobar_resultados()  # Llamar a la función para comprobar los resultados
            elif num == 3:
                finalizar()  # Llamar a la función para terminar el programa
            else:
                print('Ingrese un valor de 1 a 3')  # Mensaje de error si la opción no está en el rango válido
        else:
            print('Ingrese un valor de 1 a 3')  # Mensaje de error si la opción no es un número

def ingresar_puntuacion_y_comentario():
    while True:
        print("Por favor ingresa tu calificación del 1 a 5.")
        point = input()  # Leer la puntuación del usuario
        if point.isdecimal():  # Verificar si la puntuación es un número decimal
            point = int(point)  # Convertir la puntuación a entero
            if 1 <= point <= 5:  # Verificar si la puntuación está en el rango válido
                print("Por favor ingresa tu comentario.")
                comment = input()  # Leer el comentario del usuario
                post = f'punto: {point} comentario: {comment}'  # Formatear la puntuación y el comentario
                with open("data.txt", 'a') as file_pc:  # Abrir el archivo en modo de agregar (append) y escribir la entrada del usuario
                    file_pc.write(f'{post} \n')
                break  # Salir del bucle si la entrada es válida
            else:
                print('Ingrese un valor de 1 a 5')  # Mensaje de error si la puntuación no está en el rango válido
        else:
            print('Ingrese los puntos de valoración como números')  # Mensaje de error si la puntuación no es un número

def comprobar_resultados():
    print('Resultados hasta la fecha.')
    try:
        with open("data.txt", "r") as read_file:  # Intentar abrir el archivo en modo de lectura
            print(read_file.read())  # Imprimir el contenido del archivo
    except FileNotFoundError:  # Manejar la excepción si el archivo no se encuentra
        print("No se encontraron datos.")

def finalizar():
    print('Finalizar.')
    exit()  # Salir del programa



if __name__ == "__main__":
    menu_principal()  # Llamar a la función del menú principal
