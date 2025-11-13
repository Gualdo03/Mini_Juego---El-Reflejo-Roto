from colorama import *
import time
import pygame
import os
from PIL import Image
import shutil

puntos = 0
objetos = []

def leer_texto_lento(text, delay=0.03, sep=' '):
    for caracter in text:
        print(caracter, end="", flush=True)
        time.sleep(delay)
    return ""

def intro():
    os.system("cls")
    init()
    pygame.init()
    pygame.mixer.init()

    #Reproducir la cancion de la intro:
    pygame.mixer.music.load("musica\intro.mp3")
    pygame.mixer.music.play()

    #Intro juego:
    muestra_nombre_juego = """
    +===========================================================================+
    |   ______    __                                                            |
    |  /_____/\  /_/\                                                           |
    |  \::::_\/_ \:\ \                                                          |
    |   \:\/___/\ \:\ \                                                         |
    |    \::___\/_ \:\ \____                                                    |
    |     \:\____/\ \:\/___/\                                                   |
    |      \_____\/  \_____\/                                                   |
    | ______     ______    ______    __        ______    _________   ______     |
    |/_____/\   /_____/\  /_____/\  /_/\      /_____/\  /________/\ /_____/\    |
    |\:::_ \ \  \::::_\/_ \::::_\/_ \:\ \     \::::_\/_ \__.::.__\/ \:::_ \ \   |
    | \:(_) ) )_ \:\/___/\ \:\/___/\ \:\ \     \:\/___/\  /_\::\ \   \:\ \ \ \  |
    |  \: __ `\ \ \::___\/_ \:::._\/  \:\ \____ \::___\/_ \:.\::\ \   \:\ \ \ \ |
    |   \ \ `\ \ \ \:\____/\ \:\ \     \:\/___/\ \:\____/\ \: \  \ \   \:\_\ \ \|
    |    \_\/ \_\/  \_____\/  \_\/      \_____\/  \_____\/  \_____\/    \_____\/|
    | ______     ______    _________   ______                                   |
    |/_____/\   /_____/\  /________/\ /_____/\                                  |
    |\:::_ \ \  \:::_ \ \ \__.::.__\/ \:::_ \ \                                 |
    | \:(_) ) )_ \:\ \ \ \   \::\ \    \:\ \ \ \                                |
    |  \: __ `\ \ \:\ \ \ \   \::\ \    \:\ \ \ \                               |
    |   \ \ `\ \ \ \:\_\ \ \   \::\ \    \:\_\ \ \                              |
    |    \_\/ \_\/  \_____\/    \__\/     \_____\/                              |
    +===========================================================================+"""
    texto_introduccion = Fore.LIGHTCYAN_EX + """Despiertas en una casa y no recuerdas por qué estás ahí. El aire está cargado, como si el tiempo se hubiera detenido dentro de esas paredes. Cada paso resuena demasiado fuerte, cada sombra parece observarte. A tu alrededor, hay objetos que no deberían estar ahí…

    No sabes cómo llegaste, ni por qué. Pero hay alguien —o algo…— que intenta comunicarse contigo.

    Una voz lejana susurra tu nombre. No sabes si viene de tu mente… o de la habitación del fondo.

    🎮 Tu objetivo:
    Averigua dónde estás. Mantén la calma. Encuentra a tu amigo… y sal de ahí antes de que sea demasiado tarde.

    Presiona ENTER para comenzar tu aventura..""" + Style.RESET_ALL
    #Poner el texto en amarillo
    print(Fore.YELLOW + muestra_nombre_juego + Style.RESET_ALL)
    #Espera 3 segundos para lo siguiente
    time.sleep(3)
    #Hace que las letras salgan cada 0.03
    print("\n")
    for caracter in texto_introduccion:
        print(caracter, end="", flush=True)
        time.sleep(0.03)
    #Hacemos que si pulsa enter continue:
    input()
    os.system("cls")

def inicio_habitacion():
    print(leer_texto_lento(Fore.GREEN + "Noche cerrada. La lluvia dibuja surcos en la ventana. Las farolas del pueblo parpadean a lo lejos." + Style.RESET_ALL))
    print(leer_texto_lento(Fore.YELLOW+ "Sobre la mesa hay una nota con la letra de Mateo." + Style.RESET_ALL))
    
    while True:
        opcion_habitacion = input(leer_texto_lento( "\n"+ """   Opciones:
    |A Leer la nota
    |B Ignorar
Cual escoges: """)).lower()
        if opcion_habitacion == "b":
            print("\n"+ "Prefieres ignorar la nota… pero la inquietud crece.")
            print("Al final la abres con las manos temblando.")
        elif opcion_habitacion == "a":
            os.system("cls")
            print(Fore.GREEN + "Lees la nota:"+ Style.RESET_ALL)
            print(leer_texto_lento("\n"+"Si algo me ocurre, no busques en lo obvio. Ve a los lugares donde escondo los silencios."))
            print(leer_texto_lento(Fore.LIGHTWHITE_EX+ "Recuerdas los lugares donde Mateo solía perderse para pensar." +"\n"))
            input("Pulsa Enter para continuar..")
            os.system("cls")
            input(leer_texto_lento(Fore.LIGHTMAGENTA_EX+ "Ahora decides ir a los lugares donde solías perderte, con la esperanza de que algo te resulte familiar. No sabes qué buscas exactamente… pero sientes que las respuestas están esperándote allí." +"\n" +"\n"+ Fore.YELLOW +"Pulsa Enter para continuar.."+ Style.RESET_ALL))
            os.system("cls")
            break
        else:
            print("Error: tienes que elegir entre: a o b")

#Seccion faron abandonado:
def faro_abandonado():
    while True:
        print("El primer sitio que se te viene a la cabeza, donde solias perderte es el Faro Abandonado")
        decision_entrar_faro = input("¿Quieres ir al faro abandonado?"+ "\n" + "si o no: ").lower()
        if decision_entrar_faro == "si":
            while True:
                global puntos, objetos
                os.system("cls")
                print("""                                             
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████▓▒▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒░░░░░░░░░░░░░░█████████████▓░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒░░░░░░░░░░░░░░█░░█    ░  ▓░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒░░░░░░░░░░░░▒▒▒████▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓▓▓▓▓▓▓█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▒▒▒▒▒▒█▓▒▒░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████▒▒▒▒▒▒▒█▓▓▒░▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▓▓▓▒▒▓▒▒▒█▓▓▓▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█▓▓▓█░░▓▒▒▒▓▓▓▓▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█▓▓▓▓▒▒▒▓▓▓▓▓█▓▓████▓▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▓▓▓▓▒▒▓▓▓▒▓▓▓▒▓████▓▒▒▒▓██▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█▓▓▓▓█░▒▓▒▓█▓▓▓█▓▓██▓▓▓█████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓█▓▓▓▓█░░███▓▓▓▓████▓▓▓█▓▓▓████▓▓▓▓▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██████▒▒███▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓████▓▓▓▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██▓█▒▒▓█████████████▓▓▓▓▓▓▓███▓▓▓▓▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓█▓▓▓▓▓▓▒▒▒▓▓▓████▓▒█▓▓▓████▓▓█▓▓▓▓▓▓▓▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓█▒▒████▒▒▓▓▓▓█▓▓█▓▓█▓▓▓▓▓▓▓▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▓▓▓▓▓▓▓▓██████▓▓▓▓▓█▒▒▓██▓▒▒▓▓▓▓█▓▓█▓▓█▓▓▓▓▓▓▓▓▒▒▒▒▒▒
        ▒▒▒▒▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓▓▓▓▓███████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░░░▒░▒░░▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
                print(leer_texto_lento("\n" + Fore.CYAN + "Entras al Faro. El viento golpea las ventanas rotas, y una escalera metálica sube hacia la linterna."+ "\n"+ "Hay una caja de madera en el suelo manchada de sal." +Style.RESET_ALL))
                donde_ir_faro = int(input("""Opciones:
    1| Revisar la caja
    2| Subir la escalera
    3| Volver al pueblo
Cual eliges 1 | 2 | 3: """))
                
                if donde_ir_faro == 1:
                    print("\n"+"\n"+Fore.YELLOW + "Abres la caja. Dentro hay una linterna con dos pilas y un papel arrugado.")
                    print(Fore.BLUE + "El papel dice: Donde la luz se oculta, el recuerdo toma forma.")
                    print(Fore.CYAN + "💎 Has obtenido: Linterna (2 usos)")
                    print("✨ +10 puntos — Tu intuición brilla como el faro que guías.")
                    #sumamos puntos, y añadimos el objeto lintera, con 2 usos
                    puntos += 10
                    linterna = {"nombre": "linterna", "usos": 2}
                    objetos.append(linterna)
                    print(f"♦ Tienes: {puntos} puntos")
                    input("\n"+Fore.YELLOW +"Pulsa Enter para continuar..")
                
                elif donde_ir_faro == 2:
                    print("\n"+Fore.CYAN + "Subes y llegas a la plataforma. En la base de la vieja lámpara hay un papel con una pregunta: ")
                    acertijo1_faro = input(Fore.YELLOW + "Cual es la palabra que unen los faros en la noche: " + Style.RESET_ALL).lower()
                    while True:
                        if acertijo1_faro == "luz":
                            print("Respuesta Correcta..")
                            print(leer_texto_lento("\n"+Fore.BLUE + "La bruma se mueve. Una figura translúcida aparece, sus rasgos son borrosos pero su mirada parece reconocer el rastro de Mateo."+ Style.RESET_ALL))
                            input("Pulsa Enter para continuar.. ")
                            break
                        else:
                            print("\n"+ Fore.RED +"Esa no es la respuesta correcta."+ Style.RESET_ALL)
                            print("Pista: "+ Fore.CYAN +"¿Que enciendes por la noche, para poder ver?"+Style.RESET_ALL)
                            acertijo1_faro = input("Respuesta: ")
                
                elif donde_ir_faro == 3:
                    while True:
                        os.system("cls")
                        print("\n"+"Vuelves al Pueblo...")
                        time.sleep(2)
                        print(leer_texto_lento(Fore.MAGENTA + "Mientras te alejas del faro, una sombra cruza el suelo como un recuerdo roto en el viento." + Style.RESET_ALL))
                        print("""
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░▒████████▒░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░████████▓░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░▒████████▓░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░▒████████▓░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████▒░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█████▒░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░███████▓░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████████████▓░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░▒▓████████████████████▓░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░▒▓███████████████████████▓░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░▓████████████████████████▒░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░▒▓████████████████████████▓░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░▒█████████████████████████▓▒░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░▓██████████████████████████▒░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░▒▓██████████████████████████▓░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░▒███████████████████████████▓▒░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░▒████████████████████████████▓░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░▓█████████████████████████████▒░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░▒▓████▒▓█████████████████▓█████▓░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░▒▓███▓▒▒█████████████████▓▒▓████▓▒░░░░░░░░░░░░░""")
                        opcion_camino_pueblo = input("\n"+ """Opciones:
    1| Encender la linterna
    2| Ignorar y seguir
    3| Mantenerte quieto y observar
Cual eliges: """)
                        if opcion_camino_pueblo ==  "1": 
                            os.system("cls")
                            print(Fore.YELLOW +"Enciendes la lintera, la sombra huye y puedes seguir con tu camino perfectamente"+ " (-1 uso)"+ Style.RESET_ALL)
                            linterna = {"nombre": "linterna", "usos": 1}
                            objetos.append(linterna)
                            print("Te quedan: " + str(linterna["usos"])+ " uso de la linterna")
                            input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar.." + Style.RESET_ALL)
                            break

                        elif opcion_camino_pueblo == "2":
                            os.system("cls")
                            print(Fore.MAGENTA + "Ignoras la sombra y decides seguir, pero la sombra te sigue y a lo lejos escuchas:" + Fore.RED + " Porque te vas, si al fin y al cabo, soy tu parte más oscura;"+ Fore.MAGENTA +" decides marcharte, e ir al pueblo")
                            input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar.." + Style.RESET_ALL)
                            break

                        elif opcion_camino_pueblo == "3":
                            os.system("cls")
                            print(Fore.MAGENTA + "Decides observar la sombra, y empizas a ver que cada vez se acerca mas a ti. Y cuando ya esta muy cerca, te susurra:" + Fore.RED + " No tengas miedo, no puedes huir por siempre de tus miedos;"+ Fore.MAGENTA +" decides marcharte, e ir al pueblo")
                            input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar.." + Style.RESET_ALL)
                            break

                        else:
                            print("Lo siento, pero tienes que elegir una si o si")
                    break
                else:
                    print("error")
                    
            break
        elif decision_entrar_faro == "no":
            print(Fore.RED+ "Has decidido no entrar al faro abandonado, no podras entrar jamas"+ Style.RESET_ALL +"\n")
            input("Pulsa Enter para Continuar..")
            break
        else:
            print("Lo siento pero tienes que decir: si o no")



def biblioteca_municipal():
    while True:
        global puntos, objetos
        os.system("cls")
        print(leer_texto_lento(Fore.MAGENTA +"\n"+"El viento del faro se apaga tras de ti. La oscuridad del exterior contrasta con un nuevo brillo, a lo lejos… una luz cálida, intermitente. Caminas hacia ella, y ves un cartel cubierto de polvo, que pone: “Biblioteca Municipal”. El silencio del lugar te resulta conocido Y decides entrar para ver lo que hay"+"\n"+ Style.RESET_ALL))
        input("Pulsa Enter para Continuar..")
        os.system("cls")

        print(""" 
.........................::-=++--::.........................
.....................:::-=++++++++=-:::.....................
.................:::-=++++++++==++++++=-::..................
..............:::-=+++++++==------==+++++=-::...............
...........::-=+++++++==--------------=++++++=:::...........
.......:::-++++++++==+-++++=++--+-=++===-==++++++-:::.......
...:::-=+++++++=----=+-++=+=++-+=+=++-=------=++++++=-:::...
.::=++++++++=------------------------------------=++++++=::.
.:++++++++++++++++++++++++++++++++++++++++++++++++++++++++-:
.:::-*#########*+=====+*%###########*+=====+#%########*-::::
...:-***********+-:::-+*##***********+-:::-+###********-:...
...:-************::::=###*************-:::-##**********-:...
...:-******+*****::::=##*****++*******-:::-##****+*****-:...
...:-***+++**+***::::=##***+++**+*****-:::-##*+=++*****-:...
...:-+***++***#**::::=##**++++********-:::-##*=++***+**-:...
...:-***##****#**::::=##**+##*********-:::-##*+#****+**-:...
...::+**#%##**#**::::=##**+####*******-:::-##*+##*#*+**-:...
...:-****####*#**::::=##**+*#*##******-:::-##*+##*#*+**-:...
...::+***######**::::=###***#####*****-:::-##**#####***-:...
...:-************::::=**++++++++++++++-:::-##**********-:...
...:-************::::=#+-::::::::::-=*=:::-##**********-::::
...:-+===========::::-++==++++++++====---=+***##*++++**+====
...:-++===+++====::::-++-#@@@@@@@@#-===-=-==*++*+++++*#+====
...::====++***+==::::-++-#%++++++%#--=-:::-+*==+++**===-::::
.:-:-*+=**+***+==::::-++-#%***#**%#:---:::-++=+#++*+=+*=::::
.::::-==*%##**+==::::-++-#%*%*#%*%#:---:::-++=+%#***==-:::::
.:=:-*+=*%%%%#+==::::-++-#%******%#:---:::-++=+%%#%*=+*-:=::
.:=::-===++++++==::::-++-#%*#*##*%#:---:::-++==++++===-::-::
.:=:-*+===============++-#%*%##%*%#:-======+++=======+*-:-::
.:=:+***+=+***********+=-=+======++-=+******##****=+***+:-::
.:+-%%%%+-*%%%%%%%%#*+================+*#%%%%%%%%#-=#%%%-=-:
.:+-%%%%+-=#%%%%%#*+=====================+*%%%%%#+-=#%%%-=-:
**#*%%%%%*#%%%%#*++++++++++++++++++++++++++*#%%%%%*#%%%%***+""")
        while True:    
            print(leer_texto_lento("\n" + Fore.CYAN + "Entras a la Biblioteca Municipal. Estanterías altas, polvo y olor a papel viejo. Detrás del mostrador está el bibliotecario, mirada serena." +Style.RESET_ALL))
            donde_ir_biblioteca = int(input("""Opciones:
1| Hablar con el bibliotecario
2| Buscar en las mesas
3| Salir
    Cual eliges 1 | 2 | 3: """))
        
            if donde_ir_biblioteca == 1:
                #todo, continua aqui
                os.system("cls")
                print(leer_texto_lento(Fore.CYAN +"""Conversación con el bibliotecario:"""+"\n" +
Fore.RED +"""Tu: """ + Fore.MAGENTA + """Hola, Busco pistas sobre mi amigo Mateo… ¿vino aquí últimamente?"""+"\n" +
Fore.RED +"""Bibliotecario: """ + Fore.MAGENTA + """Mateo venía a buscar recortes de la costa. No te daré todo, pero puedo decirte esto: en sus notas repetía una advertencia corta, una palabra que dejó impresa en una imagen."""+ Style.RESET_ALL))
                input("\n"+ "Pulsa Enter para continuar..")
                os.system("cls")

            elif donde_ir_biblioteca == 2:
                os.system("cls")
                print(leer_texto_lento(Fore.CYAN+ "Empiezas a buscar en la mesa, para ver si puedes encontrar algo que te sea de utilidad.."))
                time.sleep(2)
                print(leer_texto_lento("\n"+ Fore.GREEN +"""De repente..\
Encuentras un recorte con un texto cuidadosamente colocado, pero ves que le faltan letras.."""))
#todo te has quedado por aqui, tienes preguntarle al usuario la palabra, y decirle que se la guarde para mas tarde:
                img = Image.open("imagenes\palabra_biblioteca.png")
                img.show()
                print(leer_texto_lento("\n"+"La imagen guarda la palabra necesaria. Has visto la imagen, guardate la para mas tarde.."))
                acertijo1_biblioteca = input(leer_texto_lento(Fore.WHITE +"Cual es la palabra: "+ Style.RESET_ALL)).lower()

                if acertijo1_biblioteca == "cuidado":
                    print(leer_texto_lento("✨ +15 puntos — Has leído la advertencia"))
                    puntos += 15
                    print(leer_texto_lento(f"♦ Tienes: {puntos} puntos"))
                input("\n"+Fore.YELLOW +"Pulsa Enter para continuar..")
                os.system("cls")
                
            elif donde_ir_biblioteca == 3:
                os.system("cls")
                print(leer_texto_lento(Fore.CYAN + "Sales de la Biblioteca. El pueblo sigue igual, pero la nota de Mateo te empuja a continuar la búsqueda."))
                input("\n"+Fore.YELLOW +"Pulsa Enter para continuar.."+ Style.RESET_ALL)
                break
            else:
                print(Fore.RED+ "ERROR: tienes que elegir entre 1 | 2 | 3")
        break


def estacion_subterranea_vieja():
    global puntos, objetos
    os.system("cls")
    print(leer_texto_lento(Fore.MAGENTA +"\n"+"El eco de la biblioteca se desvanece tras de ti. La noche es más fría, y el suelo parece guiarte hacia una entrada olvidada. Entre la niebla, descubres una vieja boca de metro, cubierta de óxido y polvo. Las luces parpadean débilmente, como si el lugar aún respirara. Bajas los escalones con cautela… un cartel desgastado te recibe: “Estación Subterránea Vieja”"+"\n"+ Style.RESET_ALL))
    input("Pulsa Enter para Continuar..")
    os.system("cls")
    #todo IMAGEN ASCII

    while True:
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠞⣿⣇⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣤⠀⠀⠀⠀⢺⡃⣀⣤⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣾⣷⣦⣴⠋⠉⠉⠁⠀⠀⠀⠀⠈⠙⠛⠙⠛⠉⣉⣽⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠄⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠶⠖⠒⠒⠒⠶⠶⢶⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠋⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⣀⣀⣠⡀⣀⣀⣀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠖⠀⠀⠀⠀⠀⠀⣀⡶⠺⣷⠤⢶⣾⠷⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⠛⠁⠀⠀⠀⣿⡆⣸⠟⠁⠀⢰⣶⠀⠀⠀⠘⣿⢽⡿⢿⣿⢷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡼⠟⠤⠏⠀⠀⣴⡖⠋⠉⣁⣠⣤⣤⣼⣿⣤⡴⡶⢾⣿⣿⣷⠋⠉⢳⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢞⠒⠾⠀⠀⠀⠀⣖⣲⣤⠞⣡⡶⣋⣽⣿⣿⣿⣷⣾⣯⠿⠿⠿⣿⣹⣿⣄⣀⡼⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣤⠀⣾⠀⠀⣀⣴⣶⣶⣿⣷⣶⣾⣿⣿⣿⢹⠖⡿⣿⠉⠈⣿⣀⣀⣼⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣶⠾⣿⣯⠯⣀⣀⣠⣿⣿⠿⣿⡿⠿⣯⠉⢻⣿⣿⢸⠀⣷⢿⡿⠛⠿⢻⢿⣿⢯⡼⠋⠉⠹⡿⡛⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣾⣿⠟⢋⣡⣴⣿⣿⣿⣯⣴⡖⣿⣇⢀⣺⣠⣾⣿⣿⢈⣶⢃⡎⠀⠀⢠⠇⣾⢉⠏⠀⠀⣠⢴⣇⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⠿⢟⣤⣾⣿⣿⣭⣶⣿⣿⡇⣼⣷⣿⣿⡟⠉⠉⣹⠀⢸⣾⣇⣼⣀⣀⣀⣼⣶⣇⢸⠀⠀⠀⢇⢸⡿⢀⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠷⠞⠛⣿⣿⡇⠀⢠⣿⣶⣾⣯⣿⣽⣯⣉⣉⣩⣯⣻⡌⢦⡀⠀⢀⡼⢁⣾⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡟⠛⣿⡇⠀⠀⣾⣿⠀⠀⠀⣿⡟⠓⣤⣸⣿⣿⣿⣿⣻⣧⣈⣉⣉⣉⣉⣩⣿⣧⣝⣂⣾⣶⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡁⢀⣿⣇⣀⣀⣽⣿⣀⣀⣠⡇⠀⠘⣧⡾⠀⠙⠻⡶⣧⣿⣿⠟⠛⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀
⢀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠓⠀⠰⠛⠀⠀⠀⠀⠀⠉⠈⣿⠀⢻⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⠼⣆⢀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣨⣿⡾⣷⣿⢻⣿⣇⢹⣹⢿⠘⣿⡯⡏⣿⣿⢻⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢄⣀⣠⣀⣀⠀⢀⣀⣸⣿⣿⣿⣗⣿⣏⠈⢿⣹⣸⣽⠰⡆⡟⢧⢸⣼⡿⣾⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠛⠉⠉⠉⠙⠛⠿⠿⣯⣍⣛⣻⣿⣿⣷⠷⢯⣽⣘⣾⣷⣿⣿⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⣿⣧⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣷⣿⡛⠛⠉⠉⠉⠉⠉⠉⠛⠲""")
        print(leer_texto_lento("\n"+Fore.CYAN + "Bajas por la escalera hacia la estación vieja. La luz proviene de anuncios antiguos y un reloj detenido. Al fondo hay taquillas y un panel con palabras incompletas." + Style.RESET_ALL))
        donde_ir_estacion = input("""Opciones
1| Revisar taquillas
2| Leer el panel
3| Ir al pueblo

Cual eliges 1 | 2 | 3: """)
        if donde_ir_estacion == "1":
            os.system("cls")
            print(leer_texto_lento(Fore.GREEN + "Abres una taquilla y encuentras un croquis con tres palabras y una nota:"))
            print(leer_texto_lento(Fore.WHITE + "Nota: Primero el que mira atrás."))
            print("\n"+Fore.CYAN + "💎 Has obtenido: Croquis de Mateo.")
            print("✨ +12 puntos — Resolviendo la lógica del croquis.")
            puntos += 12
            croquis = {"Croquis de Mateo"}
            objetos.append(croquis)
            print(f"♦ Tienes: {puntos} puntos")
            input("\n"+Fore.YELLOW +"Pulsa Enter para continuar.." + Style.RESET_ALL)
            os.system("cls")
        
        elif donde_ir_estacion == "2":
            os.system("cls")
            while True:
                print(leer_texto_lento(Fore.GREEN+ "Lees el panel, y muestra: [_aza] [c_nta] [s_llo] [_esa] [_ato] [pyth_n]"+ Style.RESET_ALL))
                acertijo1_estacion = input(leer_texto_lento("Teclea la palabra que completa el panel y encenderá la luz que revela la salida: ")).lower()
                if acertijo1_estacion == "tiempo":
                    print("✨ +15 puntos — Resolviendo la lógica del croquis.")
                    puntos += 15
                    print(f"♦ Tienes: {puntos} puntos")
                    print(Fore.LIGHTCYAN_EX + "💬 Y una nota que pone el codigo: 4317"+ Style.RESET_ALL)
                    print(leer_texto_lento("No sabes para que es el codigo, pero te lo guardas para adelante.."))

                    time.sleep(2)
                    os.system("cls")
                    print("De la nada, sale una figura que no sabes lo que es.")
                    print(leer_texto_lento(Fore.RED+"Tu: "+Fore.MAGENTA+ "¿Quién eres?"))
                    print(leer_texto_lento(Fore.RED+"Figura translucida: "+Fore.MAGENTA+ "Alguien que ha caminado por estos túneles mucho antes que tú. No todos los que bajan aquí regresan…"))
                    print(leer_texto_lento(Fore.RED+"Tu: "+Fore.MAGENTA+ "¿Qué es este lugar?"))
                    print(leer_texto_lento(Fore.RED+"Figura translucida: "+Fore.MAGENTA+ "Una estación olvidada, donde el tiempo se detuvo y los recuerdos se esconden entre las sombras."))
                    print(leer_texto_lento(Fore.RED+"Figura translucida: (Pista sobre Mateo) "+Fore.MAGENTA+ "Tu amigo está más cerca de lo que imaginas. Busca donde las luces parpadean y los rieles se cruzan…"))
                    print(leer_texto_lento(Fore.RED+"Figura translúcida: "+ Fore.CYAN+ "La casa del acantilado. ALLI ESTA MATEO."))
                    input("\n"+Fore.YELLOW +"Pulsa Enter para continuar.." + Style.RESET_ALL)
                    os.system("cls")
                    break

                else:
                    print(leer_texto_lento(Fore.RED + "Ha fallado.."))
                    print(leer_texto_lento(Fore.CYAN + "Pista: " + Fore.WHITE + "Es lo que da Roberto Brasero en Antena 3.."))
        
        elif donde_ir_estacion == "3":
            os.system("cls")
            print(leer_texto_lento("""Abandonas la estación subterránea y decides ir a la plaza del pueblo.
Subes los escalones de la estación y el aire se vuelve más ligero, aunque algo en ti sabe que nada es igual."""))
            input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
            os.system("cls")
            break
        
        else:
            print(Fore.RED+ "ERROR: tienes que elegir entre 1 | 2 | 3"+"\n")


def plaza_pueblo():
    print(leer_texto_lento(Fore.CYAN + "Llegas a la plaza, vacía y silenciosa. Los ecos de tu pasado resuenan entre los adoquines."))
    print(Fore.MAGENTA + "Voz interior:" + Fore.LIGHTCYAN_EX + "Félix… es hora de mirar dentro")
    input(Fore.YELLOW + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
    
    os.system("cls")
    print(leer_texto_lento(Fore.RED +"Tu interior: "+ Fore.MAGENTA + "¿Qué es lo que más temo perder?"))
    print(leer_texto_lento("Opcion A: "+ "El tiempo… siento que se escapa y no puedo recuperarlo."))
    print(leer_texto_lento("Opcion B: "+ "A las personas que amo… temo que se vayan y no pueda encontrarlas de nuevo."))
    input(leer_texto_lento("Respuestas A o B: "))
    time.sleep(2)
    print(leer_texto_lento(Fore.RED +"Tu interior: "+ Fore.MAGENTA + "¿Qué me retiene de perdonar a quien dejé atrás?"))
    print(leer_texto_lento("Opcion A: "+ "El orgullo… no quiero admitir que fui herido."))
    print(leer_texto_lento("Opcion B: "+ "El miedo a volver a sufrir… aún no estoy listo para confiar otra vez."))
    input(leer_texto_lento("Respuestas A o B: "))
    time.sleep(2)
    print(leer_texto_lento(Fore.RED +"Tu interior: "+ Fore.MAGENTA + "¿Puedo aceptarme tal como soy, con mis errores?"))
    print(leer_texto_lento("Opcion A: "+ "Sí… cada error me ha enseñado algo y forma parte de mí."))
    print(leer_texto_lento("Opcion B: "+ "No… siento que debería ser diferente, mejor, más fuerte."))
    input(leer_texto_lento("Respuestas A o B: "))
    
    time.sleep(2)
    print(leer_texto_lento("Has respondido correctamente a las preguntas. Y sientes que estás listo para enfrentar lo que hay dentro de ti."))
    os.system("cls")
    input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)


def cripta_del_espejo():
    os.system("cls")
    print(leer_texto_lento(Fore.MAGENTA+"Sales de la plaza del pueblo y avanzas por las calles vacías.."))
    print(leer_texto_lento("\n"+Fore.GREEN+"""Entre la niebla y las sombras, notas una entrada oculta que nunca habías visto antes: La Cripta del Espejo.
Un escalofrío recorre tu espalda mientras te acercas, sintiendo que algo importante te espera dentro."""+Style.RESET_ALL))
    input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
    os.system("cls")
    print(leer_texto_lento(Fore.LIGHTRED_EX + "Decides intentar entrar, pero una puerta te interrumpe el paso.."))

    input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
    os.system("cls")
    print(leer_texto_lento(Fore.LIGHTMAGENTA_EX + "Te fijas bien y ves que hay algo para meter un codigo, en el que un poco mas arriba, pone:"))
    print(leer_texto_lento(Fore.LIGHTWHITE_EX + "Si bien quieres entrar, el codigo correcto deberas poner.."+ Style.RESET_ALL))

    while True:
        pregunta_codigo_secreto = input(Fore.WHITE + "Codigo: ")
        if pregunta_codigo_secreto == "4317":
            os.system("cls")
            print("""
      ░▒▒▒▒▒░░  ░▒▒▒▒▒░    ░▒▒▒▒░   ░▒▒▒▒▒░   ░▒▒▒▒▒░       
      ░▓▓▓▓▓▓░  ░▒▒▒▒▒▒    ▒▒▒▒▒░   ▒▒▒▒▒▒░   ▒▓▓▓▓▓░       
      ░▓▓▓▓▓▓░  ░▓▒▒▒▒▒    ▒▒▒▒▒░   ▒▒▒▒▒▒░   ▒▓▓▓▓▓▒░      
    ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓░    
   ░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓█░    
   ░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓░░   
    ░▒▒▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░   
      ░▒▓▓▓▒▒▓▓▓▒▒░░░░▒▒▓▓░░░░░░░▒▓▓░░░░▒▒▒▓▓▓▓▒▓▓▓▒░░      
       ▒▓▓▓▓▒▓▓▓▒▒▒▒░░░▒▓▓▒▒▒▒░░░▒▓▓░░░▒▒▒▒▓▓▓▓▓▓▓▓▓░░░     
       ▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓░       
       ▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░▒░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓░       
      ░▒▓▓▓▓▒▒▒▒▒▒▒░░░░░░░▒▒▓▓▓▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█░       
       ▓▓▓▓▒▒▒▒▓▓▓▓▒▒░░▒▒▓▓██▓▓██▓▒▒▒░▒▒▓▓▓▓▓▓▓▓▓▓▓█░       
      ░▓▓▓▓▓▓▓▓▓▓▓▒░░▒▓▓▓▓▓▒▒▓▒▒▒▓▓▓▓▒▒░▒▓▓▓▓▓▓▓▓▓▓█░       
      ░▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▒░░░▒░░░▒▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▒       
      ░▓▓▓▓▓▓▓▓▒▒▒▒▓▓█▓▒░░░░░▒░░░░░▒▓██▓▓▒▒▓▓▒▒▒▓▓▓▓▒       
      ░▓▓▓▓▓▓▓▓▒▒▒▓▓▓▒▓▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓█▒       
      ░▓▓▓▓▓▓▓▒▒▒▓▓▓▒░▒▒░░░░░▒▒░░ ░▒▒░░▓▓▓▓▒▒▓▓▓▓▓▓█▓░      
      ▒▓▓▓▓▒▒▒▒▒▓▒▓▒░░▒▒░░ ░▒▒▒░  ░▓▓░░░▓▓▓▓▒▒▓▓▓▓▓▓▓░      
      ▒▓▓▓▓▓▓▒▒▓▓▓▒░  ░░░   ░░░    ░░░ ░▒▓▓▓▓▒▓▓▓▓▓▓▓░      
      ▒█▓▓▓▓▓▒▒▓▓▓░                     ░▓▓▓▓▒▒▓▓▓▓▓▓░░     
      ▒█▓▓▓▓▒▒▓█▓▒                       ▒▓▓▓▒▒▓▓▓▓▓▓░      
     ░▓█▓▓▓▓▒▒▓█▓░                       ░▓▓▓▒▒▓▓▓▓▓█░░     
      ▓▓▓▓▓▓▒▒▓█▓░                       ░▓▓▓▓▒▓▓▓▓██▒░     
      ▓▓▓▓▓▓▒▒▓█▓░                       ░▓▓█▓▒▓▓▓▓▓█▒░     
     ░▓▓▓▓▓▒▒▒▓█▓░                        ▓██▓▒▒▓▓▓▓█▒░     
     ░█▓▓▓▓▓▒▒██▓░                        ▓██▓▒▓▓▓▓▓▓▓░     
     ░█▓▓▓▓▓▒▒██▓░                        ▓██▓▒▓▓▓▓▓▓▓░     
     ░▓▓▓▓▓▒▒▒██▓░                        ▒██▓▒▒▓▓▓▓█▓░     
     ▒██▓▓▓▓▒▒██▓░                        ▒██▓▒▓▓▓▓███░  ░  
░░░░░▒█▓▓▓▓▓▒▒██▓░░░░░░░░░░░░░░░░░░░░░░░░░▒██▓▒▓▓▓▓▓██░░░░░░
░░░▒▒▓█▓▓▓▓▒▒▒██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▒▒▓▓▓▓██▒▒░░░░
▒▒▒▒▒▓▓▓▓▓▓▓▒▓██▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓██▓▒▓▓▓▓▓▓█▓▒▒▒▒▒
▒▒▒▒▒▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░""")

            print(leer_texto_lento("\n"+Fore.GREEN+"Entrada secreta revelada por el código. La Cripta del Espejo se abre lentamente.."))
            time.sleep(2)
            print(leer_texto_lento("\n"+Fore.LIGHTMAGENTA_EX+"Dentro, observas que hay demasiados reflejos. Te fijas bien y ves que son cristales.."))
            print(leer_texto_lento("Tu voz interior, te grita: Felix, toca los cristales.."))
            input(Fore.CYAN+ "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
            os.system("cls")
            print(leer_texto_lento(Fore.LIGHTCYAN_EX + "Cristal 1"))
            print(leer_texto_lento(Fore.LIGHTGREEN_EX + "Tocaste el primer cristal y sientes cómo un calor reconfortante recorre tu pecho; por primera vez en mucho tiempo, tu miedo parece disminuir."))
            input(Fore.CYAN+ "\n"+"Pulsa Enter para seguir tocando los cristales.." + Style.RESET_ALL)
            os.system("cls")
            
            print(leer_texto_lento(Fore.LIGHTCYAN_EX + "Cristal 2"))
            print(leer_texto_lento(Fore.LIGHTGREEN_EX + "Al rozar el segundo cristal, una claridad invade tu mente y recuerdas que siempre has tenido la fuerza para seguir adelante, incluso en la oscuridad."))
            input(Fore.CYAN+ "\n"+"Pulsa Enter para seguir tocando los cristales.." + Style.RESET_ALL)
            os.system("cls")

            print(leer_texto_lento(Fore.LIGHTCYAN_EX + "Cristal 3"))
            print(leer_texto_lento(Fore.LIGHTGREEN_EX + "El tercer cristal vibra bajo tus dedos, y una sensación de calma te envuelve; cada sombra que temías se vuelve más pequeña ante tu determinación."))
            input(Fore.CYAN+ "\n"+"Pulsa Enter para seguir tocando los cristales.." + Style.RESET_ALL)
            os.system("cls")

            print(leer_texto_lento(Fore.LIGHTCYAN_EX + "Cristal 4"))
            print(leer_texto_lento(Fore.LIGHTGREEN_EX + "Tocaste el cuarto cristal y todo tu ser se llena de energía; sabes que ahora puedes enfrentar lo que venga sin dejar que el miedo te controle."))
            input(Fore.CYAN+ "\n"+"Pulsa Enter para seguir tocando los cristales.." + Style.RESET_ALL)
            os.system("cls")

            print(leer_texto_lento(Fore.LIGHTGREEN_EX + "Al tocar el último cristal, una corriente cálida cruzó tu pecho y cada sombra perdió peso. Las dudas se volvieron recuerdo y en su lugar nació una convicción serena. Ahora caminas con paso firme: la cripta no solo te mostró reflejos, te devolvió la fuerza para buscar a Mateo y enfrentar lo que venga."))
            
            input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
            os.system("cls")
            break

        else:
            print(Fore.LIGHTRED_EX+"Incorrecto: ese no es el código")
            print(leer_texto_lento(Fore.WHITE + "Pista: Puede que antes te dieran un codigo, pruebalo.."))
            pregunta_salir_cripta = input("\n"+"¿Quieres salir de la cripta? (Si/No): ").lower()
            if pregunta_salir_cripta == "si":
                print(Fore.LIGHTRED_EX + "Decides irte de la cripta antes de probar el código. Al subir las escaleras el silencio pesa distinto; sabes que volviste con menos respuestas de las que traías..")
                print(Fore.LIGHTRED_EX + "Te vas con mala sensacion pero con la cabeza bien alta, para poder seguir con la busqueda")
                input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
                os.system("cls")
                break

            elif pregunta_salir_cripta == "no":
                print("Tienes otra oportunidad..")
            
            else:
                print("Tienes otra oportunidad..")

    #todo salida de la cripta
    print(leer_texto_lento(Fore.LIGHTMAGENTA_EX+"""Caminas fuera de la cripta. El aire de la noche es más denso, como si te observara.
A lo lejos, un banco solitario te invita a sentarte. Cada paso que das se mezcla con un murmullo bajo.
Te sientas. El silencio te envuelve.
Entonces… algo cambia. 
Una presencia se filtra en tu mente, una voz conocida y distante a la vez.
Félix..
No sabes si es un recuerdo, una advertencia o algo que intenta liberarte."""+"\n"+"\n"+
Fore.LIGHTYELLOW_EX+"""Tu respiración se entrecorta. Las sombras a tu alrededor se mueven… y entiendes que no es el mundo exterior el que debes enfrentar esta vez.
Ha comenzado la lucha contra tu propio miedo."""+Style.RESET_ALL))


def boss_final():
    print("""
░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░▒▒░▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▓▒▒░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓▒░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▓▓▓▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓█▓▓▓▓░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▓▒▒▓▒▓▓▓▒▒▓▒▓▓▓▓▒▓▓▓▓▓▓██▓░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▓▓▓▓▒▓▓▓██▓█▓▓██▓▓▓░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▓▓▓▓▓█████▓▓▓▓▓██████████▒░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▒▓▓███████▓▓▓███████████▓░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▒▒▓▓█▓▓▓▓▓▓▓▒▓█████████▓▓░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓███▓█▒░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒▓▒▒▓▓▓▓▓▓▓██████▓░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▓▓▓▒▓▓▓▓█████▓▓██████▒░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▒▓█▓▓███████████████▓░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▓██████████████████░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░▓█▓▓▓██████████████░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░▒█▓▓▓▓▓▓▓██████████▓▒▒░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▒▒▓█████▓▓▓██████████████▓▓▒░░░░░░░░░░░░░░░░░
░▒▒░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓███████████████████████▓▓▓▒░░░░░░░░▒▒░░░░
░▒░▒░░░░░░░░░░▒▓▓▓▓▓▓▓████████████████████████████▓▓▓▒▒▒░░░░▒▓▒░░░
▒▒▓▒▒░░░▒▒▒▒▒▓▓██▓█████████████████████████████▓▓████▓▓█▓▒▒▒░▒█▓▓▓
▒▒▓▒▒▒▒▒▒▒█▓▓████▓████████████▓██████████████▓████████▓█▓▒▒▒▒▒▒▒▓▓
▒▒▓▒▒▒▒▓█▓█████████████████▓▓▓▓▒▒▓▒▓▓▓█████████████████▓▓▓▓▒▒▒▒▒██
▒▓▓▒▒▒▓██▓█▓█▓████████████▓▓▓▓▒▒▒▒▒▓▒▓▓██████████████▓███▓▒█▓▓████
█▓▓▓▒▒▒▓██████▓████████████▓▓██▒▒▒▒▓▓▓▓▓█████████████▓███████████▒
█▓▓▒▒▓███▓███▓██▓██████████▓▓█▓▓▓▓▓▓▒▓██████████████████████▓████▓
███▓▓█▓█████▓██▓████████████████▓▓███████████████████▓▓█▓████▓▓███
█▓█████████▓▓▓█████████████████████████████████████████▓▓██▓██████
▓██▓▓▓▓█▓▓███▓▓▓█████████████████████████████████████████▓█▓▓▓▓█▓█
▓███▓▓▓▓██▓▓██▓████████████████████████████████████████▓▓▓▓▓▓▓▓██▓
████▓▓▓▓▓██▓▓█████████████████████████████████████████████▓▓▓▓▓███""")

    print(leer_texto_lento("\n"+Fore.RED + "Eco: "+Fore.LIGHTGREEN_EX +"¿Crees que puedes seguir adelante sin aceptar lo que dejaste atrás?"))
    print(leer_texto_lento(Fore.RED + "Eco: "+Fore.LIGHTGREEN_EX +"Cada paso que diste te alejó de lo que amabas… ¿por qué sigues fingiendo que aún puedes salvarlo?"))
    print(leer_texto_lento(Fore.RED + "Eco: "+Fore.LIGHTGREEN_EX +"Yo no soy tu enemigo. Soy tú… el tú que nunca quiso mirar atrás."))
    input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
    os.system("cls")

    print(leer_texto_lento(Fore.WHITE + "Notas como los recuerdos donde has buscado, se hacen uno.."))
    print(leer_texto_lento(Fore.LIGHTMAGENTA_EX + "\n" + "La voz de Félix aparece intermitente, intentando ayudar:"))
    print(leer_texto_lento(Fore.LIGHTRED_EX + "    No luches contra él… acéptalo."))
    print(leer_texto_lento("\n" + Fore.LIGHTMAGENTA_EX + """El Eco del Olvido se materializa frente a ti, una sombra cambiante de todos tus temores.
Sientes cómo el miedo intenta paralizarte, pero recuerdas la fuerza que despertaste en la cripta."""))
    input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
    os.system("cls")


    print(Fore.LIGHTMAGENTA_EX + """
    ░▓▓▒░              ░▒▓▓░   
    ░░▓▓▓▓▒          ░▓▓▓▓░░   
        ░▓▓░▒█▓░    ░▒█▒░▓▓░     
        ░▒█░░░▓▓░░▒▓▒░░█▒░      
            ░▓█░░▒██▒░░█▓░        
            ░░▓▓░░▒██▓░░         
            ░▒▒█▓▓▓░ ▒█▒▒░        
        ▓▓░░▒█▓██▓█▒░ ▓▓       
        ░░▓▓█▒░▒▓  ▓▒░▒█▒░       
    ░░▓▓░░▒███▒  ▒███▒░░▒▓░░   
    ▒▓▒░▒█▒          ▒█▒░░▓▒░  
    ░▒▓▓▒░░           ░▒▓▓▓░""")
    print(Fore.LIGHTRED_EX + """
██╗     ██╗   ██╗ ██████╗██╗  ██╗ █████╗      ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  █████╗ 
██║     ██║   ██║██╔════╝██║  ██║██╔══██╗    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗
██║     ██║   ██║██║     ███████║███████║    ██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝███████║
██║     ██║   ██║██║     ██╔══██║██╔══██║    ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██╔══██║
███████╗╚██████╔╝╚██████╗██║  ██║██║  ██║    ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                 
███████╗██╗         ██████╗  ██████╗ ███████╗███████╗                                            
██╔════╝██║         ██╔══██╗██╔═══██╗██╔════╝██╔════╝                                            
█████╗  ██║         ██████╔╝██║   ██║███████╗███████╗                                            
██╔══╝  ██║         ██╔══██╗██║   ██║╚════██║╚════██║                                            
███████╗███████╗    ██████╔╝╚██████╔╝███████║███████║                                            
╚══════╝╚══════╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                                            """)
    print(Fore.LIGHTMAGENTA_EX + """
    ░▓▓▒░              ░▒▓▓░   
    ░░▓▓▓▓▒          ░▓▓▓▓░░   
        ░▓▓░▒█▓░    ░▒█▒░▓▓░     
        ░▒█░░░▓▓░░▒▓▒░░█▒░      
            ░▓█░░▒██▒░░█▓░        
            ░░▓▓░░▒██▓░░         
            ░▒▒█▓▓▓░ ▒█▒▒░        
        ▓▓░░▒█▓██▓█▒░ ▓▓       
        ░░▓▓█▒░▒▓  ▓▒░▒█▒░       
    ░░▓▓░░▒███▒  ▒███▒░░▒▓░░   
    ▒▓▒░▒█▒          ▒█▒░░▓▒░  
    ░▒▓▓▒░░           ░▒▓▓▓░""")
    time.sleep(4)
    input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
    os.system("cls")
    
    ascii_lucha_boss = Fore.LIGHTRED_EX +"""
    ░█░░░█░█░█▀▀░█░█░█▀█░░░█▀▀░█▀█░█▀█░▀█▀░█▀▄░█▀█░░░█▀▀░█░░░░░█▀▄░█▀█░█▀▀░█▀▀
    ░█░░░█░█░█░░░█▀█░█▀█░░░█░░░█░█░█░█░░█░░█▀▄░█▀█░░░█▀▀░█░░░░░█▀▄░█░█░▀▀█░▀▀█
    ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀░▀░░░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░▀▀▀░▀▀▀"""
    #todo te has quedado por aqui. tienes que continuar de la lucha del usuario con el boss
    while True:
        print(ascii_lucha_boss)
        print(leer_texto_lento("\n"+"\n" + Fore.LIGHTRED_EX + "Frente a la sombra, Decide:"))
        print(leer_texto_lento(Fore.LIGHTMAGENTA_EX + "1| Respirar profundo y concentrarte en tus recuerdos de fuerza"))
        print(leer_texto_lento(Fore.LIGHTMAGENTA_EX + "2| Gritar tu miedo y desafiarlo"))
        respuesta1_lucha = input(leer_texto_lento(Fore.LIGHTRED_EX + "Respuesta “1” o “2” para luchar contra el BOSS: " + Style.RESET_ALL))
        if respuesta1_lucha == "1":
            print(leer_texto_lento("\n" + Fore.LIGHTGREEN_EX + "| Sientes cómo la sombra retrocede un instante; tu interior se calma y recuerda que has superado dificultades antes." + Style.RESET_ALL))
            break
        elif respuesta1_lucha == "2":
            print(leer_texto_lento("\n" + Fore.LIGHTGREEN_EX + "| La sombra se estremece con tu desafío, y una oleada de determinación recorre tu cuerpo. Sabes que no estás solo." + Style.RESET_ALL))
            break
        else:
            print(leer_texto_lento("\n" + Fore.LIGHTGREEN_EX + "Tienes que responder 1 o 2.."))
            time.sleep(3)
            os.system("cls")
    print(leer_texto_lento("""La sombra se vuelve más intensa, mezclando voces y recuerdos que intentan confundirte.
Pero ahora tienes la opción de usar tu fuerza interior para aceptarlo o enfrentarlo directamente."""))

    while True:
        print(ascii_lucha_boss)
        print(leer_texto_lento("\n"+"\n" + Fore.LIGHTRED_EX + "Dominando el miedo, Decide:"))
        print(leer_texto_lento(Fore.LIGHTMAGENTA_EX + "1| Aceptar tu miedo y dejar que exista"))
        print(leer_texto_lento(Fore.LIGHTMAGENTA_EX + "2| Enfrentar tu miedo con decisión y valor"))
        respuesta1_lucha = input(leer_texto_lento(Fore.LIGHTRED_EX + "Respuesta “1” o “2” para luchar contra el BOSS: " + Style.RESET_ALL))
        if respuesta1_lucha == "1":
            print(leer_texto_lento("\n" + Fore.LIGHTGREEN_EX + "| La sombra empieza a desvanecerse lentamente; cada miedo reconocido se convierte en fuerza. Te sientes más claro y firme." + Style.RESET_ALL))
            break
        elif respuesta1_lucha == "2":
            print(leer_texto_lento("\n" + Fore.LIGHTGREEN_EX + "| Cada paso que das hacia la sombra la debilita; tu coraje ilumina el espacio y el Eco del Olvido empieza a desmoronarse." + Style.RESET_ALL))
            break
        else:
            print(leer_texto_lento("\n" + Fore.LIGHTGREEN_EX + "Tienes que responder 1 o 2.."))
            time.sleep(3)
            os.system("cls")
    
    print(leer_texto_lento("""La sombra finalmente desaparece y el silencio regresa.
Tu respiración se calma, tu mente se siente más ligera y tu fuerza interior ha crecido.
Frente a ti, el banco vuelve a ser solo un banco… pero ahora sabes que puedes enfrentar lo que venga."""))
    input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)
    os.system("cls")


def finales():
    os.system("cls")
    while True:
        print(leer_texto_lento(Fore.LIGHTMAGENTA_EX + """El corazón de la reliquia palpita frente a ti.
Sabes que esta decisión cambiará todo."""))
        print(leer_texto_lento("\n"+Fore.LIGHTGREEN_EX + """1| Usar mi alma para sellar la reliquia.  
2| Absorber su poder y rehacer el mundo"""))
        decide_final = input(leer_texto_lento(Fore.LIGHTYELLOW_EX+"Escribe “1” o “2” para decidir tu destino: "))
        if decide_final == "1":
            os.system("cls")
            #Cargamos la cancion
            pygame.mixer.music.stop()
            pygame.mixer.music.load(r"musica\final_1.mp3")
            pygame.mixer.music.play()
            print(leer_texto_lento("""El aire vibra con la energía de la reliquia. Tus manos tiemblan mientras notas cómo tu fuerza se disuelve en la piedra. Cada respiración es más lenta, pero el caos se detiene. El mundo, por fin, queda en paz.

Antes de caer, sientes una voz suave: ‘Tu sacrificio no será olvidado.’

Cuando todo se apaga, una luz cálida te envuelve… y sonríes sabiendo que lo lograste."""))
            
            time.sleep(3)
            print(leer_texto_lento("\n"+"""Fin del Camino del Héroe.
Has entregado todo, y a cambio, el mundo respira un nuevo amanecer."""))
            input(Fore.LIGHTRED_EX + "\n"+"Pulsa Enter para Terminar tu aventura" + Style.RESET_ALL)
            os.system("cls")
            break
        
        elif decide_final == "2":
            #Cargamos la cancion
            pygame.mixer.music.stop()
            pygame.mixer.music.load(r"musica\final_2.mp3")
            pygame.mixer.music.play()
            print(leer_texto_lento("""El fuego azul de la reliquia arde en tu pecho. Gritas, no de dolor, sino de fuerza. El poder fluye, tus ojos se iluminan como soles, y el suelo tiembla bajo tu voluntad.

Miras el horizonte: ruinas, cenizas… y posibilidades.

—‘Si nadie más puede proteger este mundo... lo haré a mi manera.’

La oscuridad se disipa. En su lugar, surge una nueva era, forjada por tus manos."""))
            
            time.sleep(3)
            print(leer_texto_lento("\n"+"""Fin del Camino del Dominio.
Has conquistado tu destino, y ahora el mundo te pertenece."""))
            input(Fore.LIGHTRED_EX + "\n"+"Pulsa Enter para Terminar tu aventura.." + Style.RESET_ALL)
            os.system("cls")
            break

        else:
            print(leer_texto_lento(Fore.LIGHTRED_EX + "Error: tienes que elegir entre 1 o 2.." + Style.RESET_ALL))
            time.sleep(3)
            os.system("cls")


def creditos():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(r"musica\creditos.mp3")
    pygame.mixer.music.play()
    #Lista de créditos
    creditos = [
        """ 
        EEEEEEEEEEEEEEEEEEEEEE  lllllll                                                                                   
        E::::::::::::::::::::E  l:::::l                                                                                   ""","""
        E::::::::::::::::::::E  l:::::l                                                                                   
        EE::::::EEEEEEEEE::::E  l:::::l                                                                                   ""","""
        E:::::E       EEEEEE   l::::l                                                                                   
        E:::::E                l::::l                                                                                   ""","""
        E::::::EEEEEEEEEE      l::::l                                                                                   
        E:::::::::::::::E      l::::l                                                                                   ""","""
        E:::::::::::::::E      l::::l                                                                                   
        E::::::EEEEEEEEEE      l::::l                                                                                   ""","""
        E:::::E                l::::l                                                                                   
        E:::::E       EEEEEE   l::::l                                                                                   ""","""
        EE::::::EEEEEEEE:::::E  l::::::l                                                                                  
        E::::::::::::::::::::E  l::::::l                                                                                  ""","""
        E::::::::::::::::::::E  l::::::l                                                                                  
        EEEEEEEEEEEEEEEEEEEEEE  llllllll                                                                                  ""","""
                                                                                                                        
                                                                                                                        ""","""
                                                                                                                        
                                                                                                                        ""","""
                                                                                                                        
                                                                                                                        ""","""
                                                                                                                        
                                                                                                                        ""","""
                                                                                                                        
                                                                                                                        ""","""
                                                    ffffffffffffffff     lllllll                           jjjj                    
                                                    f::::::::::::::::f   l:::::l                          j::::j                   ""","""
                                                    f::::::::::::::::::f  l:::::l                          jjjj                    
                                                    f::::::fffffff:::::f  l:::::l                                                  ""","""
        rrrrr   rrrrrrrrr         eeeeeeeeeeee       f:::::f       ffffff   l::::l       eeeeeeeeeeee     jjjjjjj     ooooooooooo   
        r::::rrr:::::::::r      ee::::::::::::ee     f:::::f                l::::l     ee::::::::::::ee   j:::::j   oo:::::::::::oo ""","""
        r:::::::::::::::::r    e::::::eeeee:::::ee  f:::::::ffffff          l::::l    e::::::eeeee:::::ee  j::::j  o:::::::::::::::o
        rr::::::rrrrr::::::r  e::::::e     e:::::e  f::::::::::::f          l::::l   e::::::e     e:::::e  j::::j  o:::::ooooo:::::o""","""
        r:::::r     r:::::r  e:::::::eeeee::::::e  f::::::::::::f          l::::l   e:::::::eeeee::::::e  j::::j  o::::o     o::::o
        r:::::r     rrrrrrr  e:::::::::::::::::e   f:::::::ffffff          l::::l   e:::::::::::::::::e   j::::j  o::::o     o::::o""","""
        r:::::r              e::::::eeeeeeeeeee     f:::::f                l::::l   e::::::eeeeeeeeeee    j::::j  o::::o     o::::o
        r:::::r              e:::::::e              f:::::f                l::::l   e:::::::e             j::::j  o::::o     o::::o""","""
        r:::::r              e::::::::e            f:::::::f              l::::::l  e::::::::e            j::::j  o:::::ooooo:::::o
        r:::::r               e::::::::eeeeeeee    f:::::::f              l::::::l   e::::::::eeeeeeee    j::::j  o:::::::::::::::o""","""
        r:::::r                ee:::::::::::::e    f:::::::f              l::::::l    ee:::::::::::::e    j::::j   oo:::::::::::oo 
        rrrrrrr                  eeeeeeeeeeeeee    fffffffff              llllllll      eeeeeeeeeeeeee    j::::j     ooooooooooo   ""","""
                                                                                                          j::::j                 
                                                                                                jjjj      j::::j                 ""","""
                                                                                                j::::jj   j:::::j                 
                                                                                                j::::::jjj::::::j                 ""","""
                                                                                                jj::::::::::::j                  
                                                                                                jjj::::::jjj                   ""","""
                                                                                                    jjjjjj                      
                                                                                                                        ""","""
                                                                                                                        
                                                                                                                        ""","""
                                                         tttt                                                              
                                                       ttt:::t                                                              ""","""
                                                       t:::::t                                                              
                                                       t:::::t                                                              ""","""
        rrrrr   rrrrrrrrr        ooooooooooo     ttttttt:::::ttttttt         ooooooooooo                                      
        r::::rrr:::::::::r     oo:::::::::::oo   t:::::::::::::::::t       oo:::::::::::oo                                    ""","""
        r:::::::::::::::::r   o:::::::::::::::o  t:::::::::::::::::t      o:::::::::::::::o                                   
        rr::::::rrrrr::::::r  o:::::ooooo:::::o  tttttt:::::::tttttt      o:::::ooooo:::::o                                   ""","""
        r:::::r     r:::::r  o::::o     o::::o        t:::::t            o::::o     o::::o                                   
        r:::::r     rrrrrrr  o::::o     o::::o        t:::::t            o::::o     o::::o                                   ""","""
        r:::::r              o::::o     o::::o        t:::::t            o::::o     o::::o                                   
        r:::::r              o::::o     o::::o        t:::::t    tttttt  o::::o     o::::o                                   ""","""
        r:::::r              o:::::ooooo:::::o        t::::::tttt:::::t  o:::::ooooo:::::o                                   
        r:::::r              o:::::::::::::::o        tt::::::::::::::t  o:::::::::::::::o                                   ""","""
        r:::::r               oo:::::::::::oo           tt:::::::::::tt   oo:::::::::::oo                                    
        rrrrrrr                 ooooooooooo               ttttttttttt       ooooooooooo                                      ""","""
                                                                                                                            
                                                                                                                        ""","""
                                                                                                                        
                                                                                                                        """,
                                                                                                                        
    "Proyecto: El Reflejo Roto",
    "Desarrollador: Gualdo",
    "Música: Perico Rojas",
    "Arte: Hugo Crespino",
    "Pruebas: Juan",

    "Director: Pedro Almodóvar",
    "Productor: Esther García",
    "Guionista: Rafael Azcona",
    "Director de Fotografía: Álex Catalán",
    "Director de Arte: Félix Murcia",
    "Director de Producción: Paula Martínez",
    "Editor (Montaje): José Salcedo",
    "Sonidista: Oriol Tarragó",
    "Compositor: Fernando Velázquez",
    "Diseñador de Sonido: Oriol Tarragó",
    "Supervisor de Efectos Visuales (VFX): Marta Ramos",
    "Supervisor de Efectos Especiales (SFX): Joaquín Ortiz",
    "Diseñador de Vestuario: Paco Delgado",
    "Maquillador: Luis Vázquez",
    "Peinador: Alberto Maestre",
    "Director de Casting: Fernando Gallardo",
    "Actores Principales: Antonio Banderas, Penélope Cruz",
    "Actores Secundarios: Carmen Maura, José Coronado",
    "Doblaje: Constantino Romero",
    "Script: Gualdo",
    "Coordinador de Postproducción: Teresa Sánchez",
    "Animador 3D (ASCII): Lucía Gómez",
    "Modelador 3D (ASCII): Daniel Domínguez",

                                                                                                                                
                                                                                                                            """,
    ██████╗   ██████╗   █████╗   ██████╗ ██╗  █████╗  ███████╗                   ""","""
    ██╔════╝  ██╔══██╗ ██╔══██╗ ██╔════╝ ██║ ██╔══██╗ ██╔════╝                   ""","""
    ██║  ███╗ ██████╔╝ ███████║ ██║      ██║ ███████║ ███████╗                   ""","""
    ██║   ██║ ██╔══██╗ ██╔══██║ ██║      ██║ ██╔══██║ ╚════██║                   ""","""
    ╚██████╔╝ ██║  ██║ ██║  ██║ ╚██████╗ ██║ ██║  ██║ ███████║                   ""","""
    ╚═════╝  ╚═╝  ╚═╝╚ ═╝  ╚═╝  ╚═════╝╚ ═╝╚ ═╝  ╚═╝╚ ══════╝                   ""","""

    ██████╗   ██████╗  ██████╗           ██╗ ██╗   ██╗  ██████╗   █████╗  ██████╗ ""","""
    ██╔══██╗ ██╔═══██╗ ██╔══██╗          ██║ ██║   ██║ ██╔════╝  ██╔══██╗ ██╔══██╗""","""
    ██████╔╝ ██║   ██║ ██████╔╝          ██║ ██║   ██║ ██║  ███╗ ███████║ ██████╔╝""","""
    ██╔═══╝  ██║   ██║ ██╔══██╗     ██   ██║ ██║   ██║ ██║   ██║ ██╔══██║ ██╔══██╗""","""
    ██║      ╚██████╔╝ ██║  ██║     ╚█████╔╝ ╚██████╔╝ ╚██████╔╝ ██║  ██║ ██║  ██║""","""
    ╚═╝       ╚═════╝  ╚═╝  ╚═╝      ╚════╝   ╚═════╝   ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝""",
    ]

    #Esperar que el usuario pulse Enter
    input(Fore.LIGHTCYAN_EX + "\n"+"Pulsa Enter para Continuar..." + Style.RESET_ALL)

    #Configurar velocidad (segundos entre cada "frame")
    velocidad = 0.7

    #Altura de la "pantalla" simulada
    altura_pantalla = 55

    #Inicializar buffer vacío
    buffer = [""] * altura_pantalla

    #Obtener ancho de la terminal
    ancho_terminal = shutil.get_terminal_size().columns

    #Scroll de créditos
    for linea in creditos + [""]*altura_pantalla:  #Añadimos líneas vacías para que suba
        #Centrar la línea
        buffer.append(linea.center(ancho_terminal))
        buffer.pop(0)  #Sacamos la primera línea para simular movimiento hacia arriba
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n".join(buffer))
        time.sleep(velocidad) 



intro()
inicio_habitacion()
faro_abandonado()
biblioteca_municipal()
estacion_subterranea_vieja()
plaza_pueblo()
cripta_del_espejo()
boss_final()
finales()
creditos()
input()
