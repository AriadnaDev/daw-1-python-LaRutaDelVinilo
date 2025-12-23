#Proyecto 2: Tienda de música (CD y vinilos)

#Importo los módulos
#Hace falta instalar el módulo tabulate, progressbar adicionales
import os
import colorama
from colorama import *
import pygame
import time
from tabulate import tabulate
import progressbar
import random


#Inicializo los módulos instalados
colorama.init(autoreset=True)
pygame.init()
pygame.mixer.init()


#Pantalla de carga y registro de usuarios


#Lista para almacenar usuarios
usuarios = []


pygame.mixer.music.load("audio/xp.mp3")
pygame.mixer.music.play(1)
pygame.mixer_music.set_volume(0.1)

print(Fore.LIGHTCYAN_EX + '''
 ███████████   ███                                                       ███      █████                      ███          
░░███░░░░░███ ░░░                                                       ░░░      ░░███                     ███░           
 ░███    ░███ ████   ██████  ████████   █████ █████  ██████  ████████   ████   ███████   ██████          ███░     ██████  
 ░██████████ ░░███  ███░░███░░███░░███ ░░███ ░░███  ███░░███░░███░░███ ░░███  ███░░███  ███░░███       ███░      ░░░░░███ 
 ░███░░░░░███ ░███ ░███████  ░███ ░███  ░███  ░███ ░███████  ░███ ░███  ░███ ░███ ░███ ░███ ░███     ███░         ███████ 
 ░███    ░███ ░███ ░███░░░   ░███ ░███  ░░███ ███  ░███░░░   ░███ ░███  ░███ ░███ ░███ ░███ ░███   ███░          ███░░███ 
 ███████████  █████░░██████  ████ █████  ░░█████   ░░██████  ████ █████ █████░░████████░░██████  ███░           ░░████████
░░░░░░░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░    ░░░░░     ░░░░░░  ░░░░ ░░░░░ ░░░░░  ░░░░░░░░  ░░░░░░  ░░░              ░░░░░░░░       
      
      
      
      ''')


print(Fore.LIGHTBLUE_EX + "Antes de ingresar a la tienda tiene que registrarse, por favor escriba sus credenciales")

#Pido al usuario que ingrese nombre y contraseña
nombre_usuario = input("\nUsuario: ")
empresa_usuario = input("\nEmpresa a la que pertenece: ")

#Almacenar los datos en una lista de tuplas
usuarios.append((nombre_usuario, empresa_usuario))


bienve = "\n\nLe damos la Bienvenida a nuestro programa de gestión: 'Netsuite'"

#Bucle para mostrar poco a poco
for letra in bienve:
    print(letra, end="", flush=True)
    time.sleep(0.01)


input()
os.system("cls")


#Cargo la canción para acceder a la tienda
pygame.mixer.music.load("audio/campana.mp3")
pygame.mixer.music.play(1)


#Muestro la pantalla de carga para acceder a la página
pantalla = '''\n\nRedirigiendo a la página web https://RutaDelVinilo.es/admin...\n\nEsta operación tardará unos segundos...
\n\nGracias por su paciencia...\n'''


#Añado un bucle para que se muestre poco a poco la pantalla
for letra in pantalla:
    print(letra, end="", flush=True)
    time.sleep(0.01)


#Barra de carga
print("\n\n")
tiempo = progressbar.ProgressBar()
for i in tiempo(range(100)):
    time.sleep(0.02)

pygame.mixer.music.load("audio/bien.mp3")
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.1)


pulgar = chr(0x1F44D)


print(Fore.GREEN + f"\n{pulgar}  Carga completada,\nPulse ENTER para continuar ")

input()
os.system("cls")




#lista del menú principal usando el módulo tabulate para almacenar las columnas

menu_opciones = [["1", "Registro de venta de discos"], ["2", "Registro de venta de vinilos"], ["3", "Reponer discos / vinilos"], ["4", "Compras de segunda mano"], ["5", "Catálogo"], ["6", "Facturación"], ["7", "Clientes"], ["8", "Salir"]]



#Almaceno el inventario que tengo disponible en diferentes listas

#Listas de cd
pop = [
   ["Let Go", "Avril Lavigne", 13.90, 5],
   ["Thriller", "Michael Jackson", 15.50, 3]]

rock = [
   ["Nevermind", "Nirvana", 12.5, 1],
   ["London Calling", "The Clash", 14.0, 4]
]

hiphop = [
   ["The Marshall Mathers", "Eminem", 14.50, 6],
   ["Blurryface", "TwentyOnePilots", 11.00, 2]
]

#Lista de cds que engloba las anteriores
discos = [pop, rock, hiphop]


#Lista de vinilos
jazz = [
   ["Ella and Louis", "Ella Fitzegarld & Louis Armstrong", 20.50, 5],
   ["A Love Supreme", "John Coltrane", 22.0, 2]
]

bso = [
   ["Titanic", "James Horner", 23.0, 2],
   ["Interestellar", "Hans Zimmer", 21.0, 3]
]

importado = [
   ["Modern Times", "IU", 25.50, 4],
   ["Feel Special", "Twice", 27.90, 2]
]



#Lista de vinilos que engloba las anteriores
vinilos = [jazz, bso, importado]


#inicializo de las opciones 1 y 2: ventas
ventas_cd = 0
ventas_vinilo = 0


#inicializo de la opción 3: reponer
discos_repuestos = 0
vinilos_repuestos = 0
unidades_a_reponer_cd = 0
unidades_a_reponer_vinilo = 0


#inicializo de la opción 4: venta segunda mano
precio_segunda_mano_total = 0
precio_segunda_mano_total = 0
clientes_venta_segunda_mano = []


#inicializo de la opción 6: facturación
beneficios_totales = 0


decoracion = Fore.LIGHTBLUE_EX + """
♪ ♫ ♩ ♬ 𝄞 𝄢 𝄡 𝄠 𝄆 𝄇 ♬ ♩ ♫ ♪♪ ♫ ♩ ♬  𝄞 𝄢 𝄡 𝄠  𝄆 𝄇  ♬ ♩ ♫ ♪ ♪ ♫ ♩ ♬ 𝄞 𝄢 
"""




#Creo el bucle en el que voy a trabajar todo el programa
while True:

    os.system("cls")

    print(decoracion)
    print(Fore.LIGHTBLUE_EX + '''
            ██╗      █████╗     ██████╗ ██╗   ██╗████████╗ █████╗ 
            ██║     ██╔══██╗    ██╔══██╗██║   ██║╚══██╔══╝██╔══██╗
            ██║     ███████║    ██████╔╝██║   ██║   ██║   ███████║          
            ██║     ██╔══██║    ██╔══██╗██║   ██║   ██║   ██╔══██║
            ███████╗██║  ██║    ██║  ██║╚██████╔╝   ██║   ██║  ██║          
            ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                                                
            ██████╗ ███████╗██╗                                   
            ██╔══██╗██╔════╝██║                                        
            ██║  ██║█████╗  ██║                                   
            ██║  ██║██╔══╝  ██║                                   
            ██████╔╝███████╗███████╗                              
            ╚═════╝ ╚══════╝╚══════╝                              
                                                                
            ██╗   ██╗██╗███╗   ██╗██╗██╗      ██████╗             
            ██║   ██║██║████╗  ██║██║██║     ██╔═══██╗            
            ██║   ██║██║██╔██╗ ██║██║██║     ██║   ██║            
            ╚██╗ ██╔╝██║██║╚██╗██║██║██║     ██║   ██║            
             ╚████╔╝ ██║██║ ╚████║██║███████╗╚██████╔╝            
              ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝ ╚═════╝             
                                    
          ''')
    print(decoracion)

 
   #Menú principal configurando las filas y formato
    print(Fore.LIGHTMAGENTA_EX + tabulate(menu_opciones, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))

   #Musica del menu principal
    pygame.mixer.music.load("audio/ambiente.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.1)
    

    eleccion = int(input("\n¿Qué opción vas a seleccionar? (1-8): "))

    disco_seleccionado = None
    vinilo_seleccionado = None

   #Opción 1: Comprar discos
    if eleccion == 1:
        pygame.mixer_music.stop()
        os.system("cls")
        print(Fore.LIGHTMAGENTA_EX + '''
         
        █████   █████                      █████                     █████         
       ░░███   ░░███                      ░░███                     ░░███          
        ░███    ░███   ██████  ████████   ███████    ██████       ███████   ██████ 
        ░███    ░███  ███░░███░░███░░███ ░░░███░    ░░░░░███     ███░░███  ███░░███
        ░░███   ███  ░███████  ░███ ░███   ░███      ███████    ░███ ░███ ░███████ 
         ░░░█████░   ░███░░░   ░███ ░███   ░███ ███ ███░░███    ░███ ░███ ░███░░░  
           ░░███     ░░██████  ████ █████  ░░█████ ░░████████   ░░████████░░██████ 
            ░░░       ░░░░░░  ░░░░ ░░░░░    ░░░░░   ░░░░░░░░     ░░░░░░░░  ░░░░░░                                                                                                                                                        
                                                                                    
             █████  ███                                                             
             ░░███  ░░░                                                              
           ███████  ████   █████   ██████   ██████   █████                           
         ███░░███ ░░███  ███░░   ███░░███ ███░░███ ███░░                            
        ░███ ░███  ░███ ░░█████ ░███ ░░░ ░███ ░███░░█████                           
        ░███ ░███  ░███  ░░░░███░███  ███░███ ░███ ░░░░███                          
        ░░████████ █████ ██████ ░░██████ ░░██████  ██████                           
        ░░░░░░░░ ░░░░░ ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░░                            
         ''')

        discos = [
        [Fore.BLUE + "Pop" + Fore.RESET, pop[0][0], pop[0][1], f"{pop[0][2]}€", pop[0][3]],
        [Fore.BLUE + "Pop" + Fore.RESET, pop[1][0], pop[1][1], f"{pop[1][2]}€", pop[1][3]],
        [Fore.RED + "Rock" + Fore.RESET, rock[0][0], rock[0][1], f"{rock[0][2]}€", rock[0][3]],
        [Fore.RED + "Rock" + Fore.RESET, rock[1][0], rock[1][1], f"{rock[1][2]}€", rock[1][3]],
        [Fore.MAGENTA + "Hip-Hop" + Fore.RESET, hiphop[0][0], hiphop[0][1], f"{hiphop[0][2]}€", hiphop[0][3]],
        [Fore.MAGENTA + "Hip-Hop" + Fore.RESET, hiphop[1][0], hiphop[1][1], f"{hiphop[1][2]}€", hiphop[1][3]],]

        #Imprimo por pantalla los discos disponibles
        print(Fore.LIGHTMAGENTA_EX + "\n\nLos discos disponibles actualmente son:\n")
        print(tabulate(discos, headers=["Género", "Título", "Artista", "Precio", "Unidades"], tablefmt="fancy_grid"))

        
    
        #Seleccionar el disco que se ha vendido
        while True: 
            print("\n¡ATENCIÓN! ¡Recuerde Los discos están enumerados en orden ascendente!")
            genero_discos = input(Fore.LIGHTMAGENTA_EX + "\n\n¿Qué CD se ha vendido? (pulsa '7' si quieres volver al menú principal): ")

            if genero_discos == "7":
                print("Redirigiendo al menú principal...")
                input()
                break

            #Disco 1
            elif genero_discos == "1":
                disco_seleccionado = pop[0]
                
                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()
                        pygame.mixer.music.load("audio/Avril.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Disco 2
            elif genero_discos == "2":
                disco_seleccionado = pop[1]

                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()
                        pygame.mixer.music.load("audio/Michael.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Disco 3
            elif genero_discos == "3":
                disco_seleccionado = rock[0]
                
                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()
                        pygame.mixer.music.load("audio/Nirvana.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Disco 4
            elif genero_discos == "4":
                disco_seleccionado = rock[1]

                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()
                        pygame.mixer.music.load("audio/Clash.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Disco 5
            elif genero_discos == "5":
                disco_seleccionado = hiphop[0]
                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()
                        pygame.mixer.music.load("audio/Eminem.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Disco 6
            elif genero_discos == "6":
                disco_seleccionado = hiphop[1]

                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()
                        pygame.mixer.music.load("audio/Twenty.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            else:
                print("El número de disco que has seleccionado no es válido, por favor, inténtalo de nuevo ")
                input()
                os.system("cls")
            
            
            #Comprobar si hay unidades del disco seleccionado
            if disco_seleccionado is None:
                print("No ha seleccionado un disco válido. Por favor, inténtelo de nuevo.")
            
            elif disco_seleccionado[3] > 0:
                os.system("cls")
                print(f"\nHas seleccionado el disco: {disco_seleccionado[0]}")
                print(f"\nPrecio: {disco_seleccionado[2]}€")
                cantidad = int(input("\n¿Cuántos discos se han vendido?: "))
                
                #Se varían las unidades y se almacenan para los beneficios de facturación
                if cantidad <= disco_seleccionado[3]:
                    disco_seleccionado[3] -= cantidad
                    beneficio = cantidad * disco_seleccionado[2]
                    beneficios_totales += beneficio
                    ventas_cd += cantidad 
                    
                    print(f"\nSe han vendido {cantidad} discos de {disco_seleccionado[0]}")
                    input()
                    break
                else:
                    print(f"\nNo hay suficientes unidades de este disco")
                    input()
                    break
            else:
                print("\nLo siento, este disco está fuera de stock, necesita ponerse en contacto con su distribuidor")
                input()
                
    #Opción 2: Venta de vinilos
    
    elif eleccion == 2:
        pygame.mixer_music.stop()
        os.system("cls")
        print(Fore.LIGHTMAGENTA_EX + '''
         
        █████   █████                      █████                     █████         
       ░░███   ░░███                      ░░███                     ░░███          
        ░███    ░███   ██████  ████████   ███████    ██████       ███████   ██████ 
        ░███    ░███  ███░░███░░███░░███ ░░░███░    ░░░░░███     ███░░███  ███░░███
        ░░███   ███  ░███████  ░███ ░███   ░███      ███████    ░███ ░███ ░███████ 
         ░░░█████░   ░███░░░   ░███ ░███   ░███ ███ ███░░███    ░███ ░███ ░███░░░  
           ░░███     ░░██████  ████ █████  ░░█████ ░░████████   ░░████████░░██████ 
            ░░░       ░░░░░░  ░░░░ ░░░░░    ░░░░░   ░░░░░░░░     ░░░░░░░░  ░░░░░░                                                                                                                                                        
                                                                                            
                          ███              ███  ████                                    
                         ░░░              ░░░  ░░███                                    
             █████ █████ ████  ████████   ████  ░███   ██████   █████                   
            ░░███ ░░███ ░░███ ░░███░░███ ░░███  ░███  ███░░███ ███░░                    
             ░███  ░███  ░███  ░███ ░███  ░███  ░███ ░███ ░███░░█████                   
             ░░███ ███   ░███  ░███ ░███  ░███  ░███ ░███ ░███ ░░░░███                  
              ░░█████    █████ ████ █████ █████ █████░░██████  ██████                   
                ░░░░░    ░░░░░ ░░░░ ░░░░░ ░░░░░ ░░░░░  ░░░░░░  ░░░░░░                                                                                                                                                                                                                  
         ''')

        vinilos = [
            [Fore.BLUE + "Jazz" + Fore.RESET, jazz[0][0], jazz[0][1], f"{jazz[0][2]}€", jazz[0][3]],
            [Fore.BLUE + "Jazz" + Fore.RESET, jazz[1][0], jazz[1][1], f"{jazz[1][2]}€", jazz[1][3]],
            [Fore.RED + "BSO" + Fore.RESET, bso[0][0], bso[0][1], f"{bso[0][2]}€", bso[0][3]],
            [Fore.RED + "BSO" + Fore.RESET, bso[1][0], bso[1][1], f"{bso[1][2]}€", bso[1][3]],
            [Fore.MAGENTA + "Importado" + Fore.RESET, importado[0][0], importado[0][1], f"{importado[0][2]}€", importado[0][3]],
            [Fore.MAGENTA + "Importado" + Fore.RESET, importado[1][0], importado[1][1], f"{importado[1][2]}€", importado[1][3]],
        ]

        print(Fore.LIGHTMAGENTA_EX + "\n\nLos vinilos disponibles actualmente son:\n")
        print(tabulate(vinilos, headers=["Género", "Título", "Artista", "Precio", "Unidades"], tablefmt="fancy_grid"))

        while True:
            print("\nATENCIÓN! ¡Recuerde Los vinilos están enumerados en orden ascendente!")
            genero_vinilos = input(Fore.LIGHTMAGENTA_EX + "\n¿Qué vinilo se ha vendido? (pulsa 7 si quieres volver al menú principal): ")

            if genero_vinilos == "7":
                print("Redirigiendo al menú principal...")
                input()
                break

            #Vinilo 1
            if genero_vinilos == "1":
                vinilo_seleccionado = jazz[0]
                
                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()

                        pygame.mixer.music.load("audio/Ella.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Vinilo 2
            elif genero_vinilos == "2":
                vinilo_seleccionado = jazz[1]

                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()

                        pygame.mixer.music.load("audio/John.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Vinilo 3
            elif genero_vinilos == "3":
                vinilo_seleccionado = bso[0]

                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()

                        pygame.mixer.music.load("audio/Titanic.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Vinilo 4
            elif genero_vinilos == "4":
                vinilo_seleccionado = bso[1]

                while True:
                        sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                        if sonido == "1":
                            pygame.mixer_music.stop()

                            pygame.mixer.music.load("audio/Interestellar.mp3")
                            pygame.mixer.music.play(1)
                            pygame.mixer.music.set_volume(0.3)

                            time.sleep(1)
                            print("\n\nAhora podrá continuar con su venta ")
                            input()
                            break 
                        
                        elif sonido == "2":
                            break  

                        else:
                            print("Elija un número adecuado, por favor")  

            #Vinilo 5
            elif genero_vinilos == "5":
                vinilo_seleccionado = importado[0]

                while True:
                    sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                    if sonido == "1":
                        pygame.mixer_music.stop()

                        pygame.mixer.music.load("audio/IU.mp3")
                        pygame.mixer.music.play(1)
                        pygame.mixer.music.set_volume(0.3)

                        time.sleep(1)
                        print("\n\nAhora podrá continuar con su venta ")
                        input()
                        break 
                    
                    elif sonido == "2":
                        break  

                    else:
                        print("Elija un número adecuado, por favor")  

            #Vinilo 6
            elif genero_vinilos == "6":
                vinilo_seleccionado = importado[1]
                
                while True:
                        sonido = input("\n\n¿Desea escuchar un adelanto para confirmar su venta? (1.Si, 2.No): ")

                        if sonido == "1":
                            pygame.mixer_music.stop()

                            pygame.mixer.music.load("audio/Twice.mp3")
                            pygame.mixer.music.play(1)
                            pygame.mixer.music.set_volume(0.3)

                            time.sleep(1)
                            print("\n\nAhora podrá continuar con su venta ")
                            input()
                            break 
                        
                        elif sonido == "2":
                            break  

                        else:
                            print("Elija un número adecuado, por favor")  

            else:
                print("El número de vinilo que has seleccionado no es válido, por favor, inténtalo de nuevo ")
                input()
                os.system("cls")
                

            #Compruebo la disponibilidad de los vinilos
            
            
            if vinilo_seleccionado is None:
                print("No ha seleccionado un vinilo válido. Por favor, inténtelo de nuevo.")
            
            elif vinilo_seleccionado[3] > 0:
                pygame.mixer_music.stop()
                os.system("cls")
                print(f"\nHas seleccionado el vinilo: {vinilo_seleccionado[0]}")
                print(f"\nPrecio: {vinilo_seleccionado[2]}€")
                cantidad = int(input("\n¿Cuántos vinilos se han vendido?: "))

                if cantidad <= vinilo_seleccionado[3]:
                    vinilo_seleccionado[3] -= cantidad
                    beneficio = cantidad * vinilo_seleccionado[2]
                    beneficios_totales += beneficio
                    ventas_vinilo += cantidad
                    print(f"\nSe han vendido {cantidad} vinilos de {vinilo_seleccionado[0]}")
                    input()
                    break
                else:
                    print(f"\nNo hay suficientes unidades de este vinilo")
                    input()
                    break
            else:
                print("\nLo siento, este vinilo está fuera de stock, necesita ponerse en contacto con su distribuidor")
                input()
                break
       
    #Opción 3: Reponer discos / vinilos
    elif eleccion == 3:
        pygame.mixer_music.stop()
        os.system("cls")
        print(Fore.YELLOW + '''
                    
          ███████████                                                            
         ░░███░░░░░███                                                           
          ░███    ░███   ██████  ████████   ██████  ████████    ██████  ████████ 
          ░██████████   ███░░███░░███░░███ ███░░███░░███░░███  ███░░███░░███░░███
          ░███░░░░░███ ░███████  ░███ ░███░███ ░███ ░███ ░███ ░███████  ░███ ░░░ 
          ░███    ░███ ░███░░░   ░███ ░███░███ ░███ ░███ ░███ ░███░░░   ░███     
         █████   █████░░██████  ░███████ ░░██████  ████ █████░░██████  █████    
        ░░░░░   ░░░░░  ░░░░░░   ░███░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     
                                ░███                                            
                                █████                                           
                                ░░░░░                                             
              ''')
    
        while True:
            print("\n\nATENCIÓN! Los discos y vinilos están enumerados en orden ascendente.")
            print("\nElige qué disco o vinilo desea reponer:")
            eleccion_reponer = input("\nPulsa 1 para reponer un disco o 2 para reponer un vinilo (pulsa 7 para volver al menú principal): ")

            # Muestro los discos y vinilos disponibles
            if eleccion_reponer == "7":
                print("Redirigiendo al menú principal...")
                break
            elif eleccion_reponer == "1":
                os.system("cls")
                print(Fore.CYAN + "\n\nLos discos disponibles actualmente son:\n")

                discos = [
                    [Fore.BLUE + "Pop" + Fore.RESET, pop[0][0], pop[0][1], f"{pop[0][2]}€", pop[0][3]],
                    [Fore.BLUE + "Pop" + Fore.RESET, pop[1][0], pop[1][1], f"{pop[1][2]}€", pop[1][3]],
                    [Fore.RED + "Rock" + Fore.RESET, rock[0][0], rock[0][1], f"{rock[0][2]}€", rock[0][3]],
                    [Fore.RED + "Rock" + Fore.RESET, rock[1][0], rock[1][1], f"{rock[1][2]}€", rock[1][3]],
                    [Fore.MAGENTA + "Hip-Hop" + Fore.RESET, hiphop[0][0], hiphop[0][1], f"{hiphop[0][2]}€", hiphop[0][3]],
                    [Fore.MAGENTA + "Hip-Hop" + Fore.RESET, hiphop[1][0], hiphop[1][1], f"{hiphop[1][2]}€", hiphop[1][3]],
                ]

                print(tabulate(discos, headers=["Género", "Título", "Artista", "Precio", "Unidades"], tablefmt="fancy_grid"))

                # Asigno cada respuesta al disco correspondiente
                disco_a_reponer = input("\n¿Qué disco deseas reponer? (pulsa 7 para volver): ")

                # Inicializo disco_seleccionado en None
                disco_seleccionado = None

                if disco_a_reponer == "7":
                    break
                elif disco_a_reponer == "1":
                    disco_seleccionado = pop[0]
                elif disco_a_reponer == "2":
                    disco_seleccionado = pop[1]
                elif disco_a_reponer == "3":
                    disco_seleccionado = rock[0]
                elif disco_a_reponer == "4":
                    disco_seleccionado = rock[1]
                elif disco_a_reponer == "5":
                    disco_seleccionado = hiphop[0]
                elif disco_a_reponer == "6":
                    disco_seleccionado = hiphop[1]
                else:
                    print("Número de disco no válido.")
                
                # Si no se seleccionó un disco válido, salta el resto del código
                if disco_seleccionado is None:
                    continue

                # Almaceno las cantidades para luego contarlas en facturación, reponer lo escrito por el usuario
                unidades_a_reponer_1 = int(input(f"\n¿Cuántas unidades deseas reponer de {disco_seleccionado[0]}?: "))
                disco_seleccionado[3] += unidades_a_reponer_1
                print(f"\nSe han repuesto {unidades_a_reponer_1} unidades de {disco_seleccionado[0]}.\n")
                unidades_a_reponer_cd += unidades_a_reponer_1
                break

            elif eleccion_reponer == "2":
                os.system("cls")
                print(Fore.CYAN + "\n\nLos vinilos disponibles actualmente son:\n")

                vinilos = [
                    [Fore.BLUE + "Jazz" + Fore.RESET, jazz[0][0], jazz[0][1], f"{jazz[0][2]}€", jazz[0][3]],
                    [Fore.BLUE + "Jazz" + Fore.RESET, jazz[1][0], jazz[1][1], f"{jazz[1][2]}€", jazz[1][3]],
                    [Fore.RED + "BSO" + Fore.RESET, bso[0][0], bso[0][1], f"{bso[0][2]}€", bso[0][3]],
                    [Fore.RED + "BSO" + Fore.RESET, bso[1][0], bso[1][1], f"{bso[1][2]}€", bso[1][3]],
                    [Fore.MAGENTA + "Importado" + Fore.RESET, importado[0][0], importado[0][1], f"{importado[0][2]}€", importado[0][3]],
                    [Fore.MAGENTA + "Importado" + Fore.RESET, importado[1][0], importado[1][1], f"{importado[1][2]}€", importado[1][3]],
                ]

                print(tabulate(vinilos, headers=["Género", "Título", "Artista", "Precio", "Unidades"], tablefmt="fancy_grid"))

                # Reponer los vinilos
                vinilo_a_reponer = input("\n¿Qué vinilo deseas reponer? (pulsa 7 para volver): ")

                # Inicializo vinilo_seleccionado en None
                vinilo_seleccionado = None

                # Asigno los vinilos
                if vinilo_a_reponer == "7":
                    break
                elif vinilo_a_reponer == "1":
                    vinilo_seleccionado = jazz[0]
                elif vinilo_a_reponer == "2":
                    vinilo_seleccionado = jazz[1]
                elif vinilo_a_reponer == "3":
                    vinilo_seleccionado = bso[0]
                elif vinilo_a_reponer == "4":
                    vinilo_seleccionado = bso[1]
                elif vinilo_a_reponer == "5":
                    vinilo_seleccionado = importado[0]
                elif vinilo_a_reponer == "6":
                    vinilo_seleccionado = importado[1]
                else:
                    print("Número de vinilo no válido.")
                
                # Si no se seleccionó un vinilo válido, salta el resto del código
                if vinilo_seleccionado is None:
                    continue

                # Almaceno las cantidades para luego contarlas en facturación, reponer lo escrito por el usuario
                unidades_a_reponer_2 = int(input(f"\n¿Cuántas unidades deseas reponer de {vinilo_seleccionado[0]}?: "))
                vinilo_seleccionado[3] += unidades_a_reponer_2
                print(f"\nSe han repuesto {unidades_a_reponer_2} unidades de {vinilo_seleccionado[0]}.\n")
                unidades_a_reponer_vinilo += unidades_a_reponer_2
                break
            else:
                print("\n\nOpción no válida. Por favor, elige 1 o 2.")
            
            input()
            os.system("cls")
            
       
    #Opción 4: venta de segunda mano   
    elif eleccion == 4:
        pygame.mixer_music.stop()
        os.system("cls")
        print(Fore.LIGHTGREEN_EX +'''
                    
         █████████                                              █████              ██████   ██████                              
        ███░░░░░███                                            ░░███              ░░██████ ██████                               
       ░███    ░░░   ██████   ███████ █████ ████ ████████    ███████   ██████      ░███░█████░███   ██████   ████████    ██████ 
       ░░█████████  ███░░███ ███░░███░░███ ░███ ░░███░░███  ███░░███  ░░░░░███     ░███░░███ ░███  ░░░░░███ ░░███░░███  ███░░███
        ░░░░░░░░███░███████ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███   ███████     ░███ ░░░  ░███   ███████  ░███ ░███ ░███ ░███
        ███    ░███░███░░░  ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███  ███░░███     ░███      ░███  ███░░███  ░███ ░███ ░███ ░███
       ░░█████████ ░░██████ ░░███████ ░░████████ ████ █████░░████████░░████████    █████     █████░░████████ ████ █████░░██████ 
        ░░░░░░░░░   ░░░░░░   ░░░░░███  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░░░    ░░░░░     ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░  
                             ███ ░███                                                                                           
                            ░░██████                                                                                            
                            ░░░░░░                                                                                             
              ''')
        print("\nEn este espacio podrá registrar los discos que la tienda ha comprado de segunda mano de clientes, así como el precio que la tienda le ofreció al cliente.")

        #Lista temporal para almacenar los discos de segunda mano introducidos
        discos_segunda_mano = []

        while True:
                tipo = input("\n\n¿Qué ha adquirido, un Disco o un Vinilo?: ")
                tipo = tipo.lower()

                #coincidencias exactas
                if tipo not in ["disco", "vinilo"]:
                    print("Opción inválida, regresará al menú...")
                    input()
                    break
                else:
                    #se almacenan para mostrar por pantalla y luego en facturación el precio
                    genero = input("\n\nIntroduzca el género (pop, rock, hiphop, jazz, BSO, importado u otro) del disco o vinilo: ")
                    genero = genero.lower()
                    titulo = input("\n\nIntroduzca el título del disco/vinilo: ")
                    titulo = titulo.title()
                    artista = input("\n\nIntroduzca el nombre del artista o banda: ")
                    artista = artista.title()
                    cantidad = int(input("\n\nIntroduzca la cantidad de discos o vinilos: "))
                    cliente = input("\n\nIntroduzca el nombre del cliente que ha vendido el disco/vinilo: ")
                    cliente= cliente.title()

                    #Genero un precio aleatorio entre 0 y 8 euros
                    precio = round(random.uniform(0, 8), 2)
                    
                    total_compra = precio * cantidad
                    precio_segunda_mano_total += total_compra 
                    
                    
                    #muestro por pantalla
                    nuevo_item = [tipo.capitalize(), genero.capitalize(), titulo, artista, cantidad, f"{precio}€", cliente]
                    discos_segunda_mano.append(nuevo_item)
                    
                    #Añado los clientes para el apartado clientes
                    clientes_venta_segunda_mano.append([cliente, tipo.capitalize(), genero, titulo, artista, cantidad])


                    os.system("cls")  

                    #Tabla con los discos introducidos
                    print(Fore.LIGHTMAGENTA_EX + "\nRegistro de Discos/Vinilos de Segunda Mano")
                    print(tabulate(discos_segunda_mano, headers=["Tipo", "Género", "Título", "Artista", "Cantidad", "Precio", "Cliente"], tablefmt="fancy_grid"))

                    #Pregunto si desea añadir más o volver al menú
                    opcion = input("\n¿Desea añadir otro disco/vinilo? (Si / No): ")
                    opcion= opcion.lower()
                    
                    if opcion != "si":
                        print("\nRegresando al menú principal...")
                        break 
                    
                    
       
    #Opción 5: Catálogo
    elif eleccion == 5:
        pygame.mixer_music.stop()
        os.system("cls")
        print(Fore.LIGHTMAGENTA_EX + '''
                    
           █████████             █████              ████                            
          ███░░░░░███           ░░███              ░░███                            
         ███     ░░░   ██████   ███████    ██████   ░███   ██████   ███████  ██████ 
        ░███          ░░░░░███ ░░░███░    ░░░░░███  ░███  ███░░███ ███░░███ ███░░███
        ░███           ███████   ░███      ███████  ░███ ░███ ░███░███ ░███░███ ░███
        ░░███     ███ ███░░███   ░███ ███ ███░░███  ░███ ░███ ░███░███ ░███░███ ░███
         ░░█████████ ░░████████  ░░█████ ░░████████ █████░░██████ ░░███████░░██████ 
         ░░░░░░░░░   ░░░░░░░░    ░░░░░   ░░░░░░░░ ░░░░░  ░░░░░░   ░░░░░███ ░░░░░░  
                                                                  ███ ░███         
                                                                 ░░██████          
                                                                ░░░░░░             
              ''')
        print("\n\nCatálogo completo de discos y vinilos disponibles:")

        #Muestro todos los CDs ordenados alfabéticamente
        discos.sort()
        vinilos.sort()

        #Muestro la lista de discos disponibles
        print(Fore.LIGHTMAGENTA_EX + "\n\t------ Catálogo de Discos (CD) ------")
        print(tabulate([
            [pop[0][0], pop[0][1], pop[0][2]],
            [pop[1][0], pop[1][1], pop[1][2]],
            [rock[0][0], rock[0][1], rock[0][2]],
            [rock[1][0], rock[1][1], rock[1][2]],
            [hiphop[0][0], hiphop[0][1], hiphop[0][2]],
            [hiphop[1][0], hiphop[1][1], hiphop[1][2]]
        ], headers=["Título", "Artista", "Precio"], tablefmt="rounded_grid"))

        # Muestro la lista de vinilos disponibles
        print(Fore.LIGHTMAGENTA_EX + "\n\t------ Catálogo de Vinilos ------")
        print(tabulate([
            [jazz[0][0], jazz[0][1], jazz[0][2]],
            [jazz[1][0], jazz[1][1], jazz[1][2]],
            [bso[0][0], bso[0][1], bso[0][2]],
            [bso[1][0], bso[1][1], bso[1][2]],
            [importado[0][0], importado[0][1], importado[0][2]],
            [importado[1][0], importado[1][1], importado[1][2]]
        ], headers=["Título", "Artista", "Precio"], tablefmt="rounded_grid"))
        input()
        os.system("cls")
        
    #Opción 6: Facturación
    
    elif eleccion == 6:
            pygame.mixer_music.stop()
            os.system("cls")
            print(Fore.LIGHTBLUE_EX + '''
                        
          ███████████                     █████                                             ███                     
         ░░███░░░░░░█                    ░░███                                             ░░░                      
          ░███   █ ░   ██████    ██████  ███████   █████ ████ ████████   ██████    ██████  ████   ██████  ████████  
          ░███████    ░░░░░███  ███░░███░░░███░   ░░███ ░███ ░░███░░███ ░░░░░███  ███░░███░░███  ███░░███░░███░░███ 
          ░███░░░█     ███████ ░███ ░░░   ░███     ░███ ░███  ░███ ░░░   ███████ ░███ ░░░  ░███ ░███ ░███ ░███ ░███ 
          ░███  ░     ███░░███ ░███  ███  ░███ ███ ░███ ░███  ░███      ███░░███ ░███  ███ ░███ ░███ ░███ ░███ ░███ 
          █████      ░░████████░░██████   ░░█████  ░░████████ █████    ░░████████░░██████  █████░░██████  ████ █████
          ░░░░░        ░░░░░░░░  ░░░░░░     ░░░░░    ░░░░░░░░ ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░  
                  
                  ''')
         

            #Costo de reposición: 3€ por unidad
            costo_reposicion = (unidades_a_reponer_cd + unidades_a_reponer_vinilo) * 3

            #Registro de discos y vinilos repuestos
            discos_repuestos += unidades_a_reponer_cd
            vinilos_repuestos += unidades_a_reponer_vinilo

            #Pérdidas
            perdidas_totales = costo_reposicion + precio_segunda_mano_total

            #Balance
            total_facturado = beneficios_totales - perdidas_totales

            print(Fore.LIGHTBLUE_EX + "\n\tBENEFICIOS TOTALES:")
            print(f"Total de beneficios por venta de discos: {beneficios_totales}€")
            print(f"Total de unidades de discos vendidos: {ventas_cd}")
            print(f"Total de unidades de vinilos vendidos: {ventas_vinilo}")

            print(Fore.LIGHTBLUE_EX + "\n\tPÉRDIDAS TOTALES:")
            print(f"Gasto en compras de segunda mano: {precio_segunda_mano_total}€")
            print(f"Reposición de {discos_repuestos} discos y {vinilos_repuestos} vinilos a 3€ cada uno: {costo_reposicion}€")

            print(Fore.LIGHTBLUE_EX + "\n\tBALANCE:")
            print(f"Total final: {round(total_facturado, 2)}€")

            input()
            os.system("cls")
    
    
    #Opción 7: Clientes

    elif eleccion == 7:
        pygame.mixer_music.stop()
        os.system("cls")
        print(Fore.LIGHTRED_EX + '''
                        
                        
               █████████  ████   ███                       █████                    
              ███░░░░░███░░███  ░░░                       ░░███                     
             ███     ░░░  ░███  ████   ██████  ████████   ███████    ██████   █████ 
            ░███          ░███ ░░███  ███░░███░░███░░███ ░░░███░    ███░░███ ███░░  
            ░███          ░███  ░███ ░███████  ░███ ░███   ░███    ░███████ ░░█████ 
            ░░███     ███ ░███  ░███ ░███░░░   ░███ ░███   ░███ ███░███░░░   ░░░░███
             ░░█████████  █████ █████░░██████  ████ █████  ░░█████ ░░██████  ██████ 
              ░░░░░░░░░  ░░░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░    ░░░░░   ░░░░░░  ░░░░░░  
              
              ''')

        #Tabla de administradores
        print(Fore.LIGHTRED_EX + "\nAdministradores Registrados:")
        print(tabulate(usuarios, headers=["Usuario", "Empresa"], tablefmt="fancy_grid"))

        #Tabla de clientes de segunda mano
        if clientes_venta_segunda_mano:
            print(Fore.LIGHTRED_EX + "\nClientes que han vendido discos o vinilos de segunda mano:")
            print(tabulate(clientes_venta_segunda_mano, headers=["Cliente", "Tipo", "Género", "Título", "Artista", "Cantidad"], tablefmt="fancy_grid"))
        else:
            print("\nNo hay registros de ventas de segunda mano.")

        input()
        os.system("cls")
            
    
    #Opción 8: salir
    elif eleccion == 8:
       pygame.mixer_music.stop()
       break
       
    else:
       print("Escoja una opción válida por favor")
       input()
       os.system("cls")
       

#Pantalla de despedida
os.system("cls")
print(Fore.LIGHTCYAN_EX + '''
            
          █████████       █████  ███                  
         ███░░░░░███     ░░███   ░░░                   
        ░███    ░███   ███████  ████   ██████   █████ 
        ░███████████  ███░░███ ░░███  ███░░███ ███░░  
        ░███░░░░░███ ░███ ░███  ░███ ░███ ░███░░█████ 
        ░███    ░███ ░███ ░███  ░███ ░███ ░███ ░░░░███
        █████   █████░░████████ █████░░██████  ██████ 
        ░░░░░   ░░░░░  ░░░░░░░░ ░░░░░  ░░░░░░  ░░░░░░  
            
      ''')
print("\n\n\tGracias por confiar en nuestros servicios, ¡hasta la próxima!")


input()