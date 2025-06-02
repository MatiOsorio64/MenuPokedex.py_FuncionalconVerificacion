#Se pide crear un programa para almacenar pokemones.
#La información del pokemon debe ser número, nombre y altura.

import os,time,msvcrt  #limpiar pantalla, pausar, esperar tecla
#MENÚ
os.system('cls')
menu = """ --- |MENU| --- 
1. Agregar pokemon
2. Ver pokemon
3. Salir
"""
ListaPokemon = []  #Lista que guarda los pokémon
while True:
    os.system('cls')
    print(menu)
    opc = (input("Ingrese una opción: "))
    os.system('cls')

    if opc == '1': #Agregar pokémon
        print("AGREGAR POKEMON")

        #Valide el nombre primero
        while True:
            nombre = input("Ingrese el nombre de su pokémon: ").strip().title()
            if len(nombre)>=3 and nombre.isalpha():
                break
            else:
                print("❎ Nombre inválido. Debe tener al menos 3 letras y solo letras.")
        #Valide número y altura con try dentro del bloque
        try:
            número = (input("Ingrese el número de su pokémon (ej. pikachu N.° 0025): "))
            altura = float(input("Ingrese la altura de su pokemon ('en metros, con punto decimal.'): "))
        except:
            print("❎ Número o altura inválidos. Asegúrate de usar números y punto decimal.")
            print("\n...presione una tecla para continuar...")
            msvcrt.getch() 
            continue  #Vuelve al menú sin guardar
        #Cree el dicciónario 
        Ingresar_Pokemon = {
            "nombre": nombre,
            "número": número,
            "altura": altura
        }
        ListaPokemon.append(Ingresar_Pokemon)  #Guardar en la lista
        print("✅ Pokemon guardado con éxito!")
    
    elif opc == '2':  #Mostrar pokémons 
        print("VER POKEMONS")
        if not ListaPokemon:
            print(" No hay pokémons registrados.")
        else:
            for pokemon in ListaPokemon:  #Recorre la lista y muestra los pokémon
                print(f"|pokémon: {pokemon["nombre"]} | N.° {pokemon["número"]} | Mide {pokemon["altura"]} m de altura")

    elif opc == '3':  #Salir del programa
        print("👋 Gracias, Adios!")
        break
    else:
        print("   ❎  Opción incorrecta!  (Elige 1, 2 o 3)   ")
    print("\n...presione una tecla para continuar...")
    msvcrt.getch() 